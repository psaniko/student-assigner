import networkx as nx
import metis
import csv
from collections import Counter

# constants
RECOMMENDATIONS_TO_INT = {
    'HS': 1,
    'HS/RS': 2,
    'RS': 3,
    'RS/GY': 4,
    'GY': 5,
}

NUM_PARITIONS = 3

FRIENDSHIP_WEIGHT = 30
CLASSMATE_WEIGHT = 3
SCHOOLMATE_WEIGHT = 1

G = nx.Graph()
G.graph['edge_weight_attr'] = 'weight'
G.graph['node_weight_attr'] = ['always_one', 'gender_int', 'recommendation_int']

# helpers
name_to_index = {}
class_to_indices = {}
school_to_indices = {}


# helper function to add visuals to edges
def add_edge(G, node1, node2, weight):
    existing = G.edges.get((node1, node2))
    if existing and abs(existing['weight']) > abs(weight):
        return
    if existing and existing['weight'] < 0 and weight > 0:
        return

    G.add_edge(
        node1,
        node2,
        weight=weight,
        label=weight,
        penwidth=min(FRIENDSHIP_WEIGHT, abs(weight)) / 10,
        color='red' if weight < 0 else 'black',
    )


# add students as nodes
i = 0
with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        name = row['Vorname Mädchen'] + row['Vorname Junge'] + ' ' + row['Name']
        origin_class = row['Abgebende Schule'] + ' ' + row['Klasse']
        origin_school = row['Abgebende Schule']
        gender = 'f' if row['Vorname Mädchen'] else 'm'

        # gender_icon = '♂' if gender is 'm' else '♀'
        G.add_node(
            i,
            label=name + "\n" + origin_school + ' (' + row['SF-Emp-fehlung'] + ')',
            gender=gender,
            gender_int=1 if gender == 'f' else 0,
            origin_school=origin_school,
            origin_class=origin_class,
            recommendation_int=RECOMMENDATIONS_TO_INT[row['SF-Emp-fehlung']],
            preferences=row['Wunsch'],
            fillcolor='#FFFFFF' if row['Vorname Mädchen'] else '#E0E0E0',
            always_one=1,
            style='filled',
            penwidth=3,
        )
        name_to_index[name] = i
        if origin_class not in class_to_indices:
            class_to_indices[origin_class] = set()
        class_to_indices[origin_class].add(i)

        if origin_school not in school_to_indices:
            school_to_indices[origin_school] = set()
        school_to_indices[origin_school].add(i)

        i += 1

# add preferences as edges
for i, node in G.nodes.items():
    items = node['preferences'].split(',')
    items = [item.strip() for item in items]

    for item in items:
        if not item:
            continue

        multiplier = 1
        if item.startswith('!'):
            multiplier = -1
            item = item[1:]

        if item.startswith('*'):
            multiplier = multiplier * 100
            item = item[1:]

        (filter_attr, filter_value) = (None, None)
        if item.startswith('['):
            item_parts = item[1:].split(']')
            filter_parts = item_parts[0].split('=')
            assert len(filter_parts) == 2, 'Invalid filter: ' + item
            (filter_attr, filter_value) = filter_parts
            item = item_parts[1]

        schoolmates = school_to_indices.get(item, None)
        classmates = class_to_indices.get(item, None)
        friend = name_to_index.get(item, None)

        if schoolmates is not None:
            # apply optional filter
            if filter_attr:
                schoolmates = [
                    i for i, node in G.nodes.items()
                    if i in schoolmates and node[filter_attr] == filter_value
                ]

            for schoolmate in schoolmates:
                if i == schoolmate:
                    continue
                add_edge(G, i, schoolmate, weight=SCHOOLMATE_WEIGHT * multiplier)
        elif classmates is not None:
            # apply optional filter
            if filter_attr:
                classmates = [
                    i for i, node in G.nodes.items()
                    if i in classmates and node[filter_attr] == filter_value
                ]

            for classmate in classmates:
                if i == classmate:
                    continue
                add_edge(G, i, classmate, weight=CLASSMATE_WEIGHT * multiplier)
        elif friend is not None:
            add_edge(G, i, friend, weight=FRIENDSHIP_WEIGHT * multiplier)
        else:
            print('Unhandled preference: ' + item)

# partition graph
(total_volume, parts) = metis.part_graph(
    graph=G,
    nparts=NUM_PARITIONS,
    tpwgts=[
        (1 / NUM_PARITIONS, 1 / NUM_PARITIONS, 1 / NUM_PARITIONS) for i in range(0, NUM_PARITIONS)
    ],
    ubvec=[1.030, 1.200, 1.200],
    objtype='cut',
)

# calculate statistics
counter = Counter(parts)
print('total cost: ', total_volume)
print('group sizes: ', ','.join(str(count) for count in counter.values()))

colors = ['red', 'blue', 'green']
used_colors = set()
for i, p in enumerate(parts):
    G.node[i]['color'] = colors[p]
    used_colors.add(colors[p])

women_by_group = {used_color: 0 for used_color in used_colors}
for i, node in G.nodes.items():
    if node['gender'] == 'f':
        women_by_group[node['color']] += 1
print('women per group: ', ','.join(str(count) for count in women_by_group.values()))

# write to DOT file
nx.nx_pydot.write_dot(G, 'graph.dot')  # Requires pydot or pygraphviz
