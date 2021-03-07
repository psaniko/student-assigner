import random
import csv
import sys
from multiprocessing import Pool, TimeoutError

import networkx as nx
import metis
import pydot


def build_graph_from_file(filename='students.csv', *args, **kwargs):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        students = list(reader)
        return build_graph(students, *args, **kwargs)


def build_graph(
    students,
    num_partitions=3,
    friendship_weight=30,
    classmate_weight=3,
    schoolmate_weight=1,
    teacher_multiplier=100,
    node_weights_to_ubvec=None,
):
    G = nx.Graph()
    G.graph['edge_weight_attr'] = 'weight'
    G.graph['node_weight_attr'] = list(node_weights_to_ubvec.keys())

    # helper vars
    name_to_index = {}
    class_to_indices = {}
    school_to_indices = {}
    i = 0

    # add students as nodes
    for row in students:
        name = row['Name']
        origin_class = row['School'] + ' ' + row['Class']
        origin_school = row['School']
        gender = row.get('Gender')

        G.add_node(
            i,
            label=name + "\n" + origin_class,
            origin_school=origin_school,
            origin_class=origin_class,
            preferences=row['Preferences'],

            # styling
            shape='hexagon' if gender == 'm' else 'ellipse',
            penwidth=3,

            # node attributes
            total=1,  # used to balance total number of students
            gender=1 if gender == 'f' else 0,
            **{
                attribute: int(row[attribute.capitalize()])
                for attribute in node_weights_to_ubvec.keys()
                if attribute not in ('gender', 'total')
            },
        )

        # fill helper vars for preference parsing later on
        name_to_index[name] = i
        if origin_class not in class_to_indices:
            class_to_indices[origin_class] = set()
        class_to_indices[origin_class].add(i)

        if origin_school not in school_to_indices:
            school_to_indices[origin_school] = set()
        school_to_indices[origin_school].add(i)

        i += 1

    # add preferences as edges
    for student, node in G.nodes.items():
        items = node['preferences'].split(',')

        for item in items:
            item = item.strip()  # remove whitespace

            if not item:
                continue  # skip empty items

            # parse negation symbol
            multiplier = 1
            if item.startswith('!'):
                multiplier = -1
                item = item[1:]

            # parse teacher symbol
            if item.startswith('*'):
                multiplier = multiplier * teacher_multiplier
                item = item[1:]

            # parse filter
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

            # set targets and base weight
            if schoolmates is not None:
                targets = schoolmates
                base_weight = schoolmate_weight
            elif classmates is not None:
                targets = classmates
                base_weight = classmate_weight
            elif friend is not None:
                targets = [friend]
                base_weight = friendship_weight
            else:
                raise ValueError('Could not parse preference: ' + item)

            # apply filter
            if filter_attr:
                targets = [
                    i for i, node in G.nodes.items()
                    if i in targets and node[filter_attr] == filter_value
                ]

            # actually add edges
            for target in targets:
                if student != target:
                    add_edge(G, student, target, weight=base_weight * multiplier)

    # partition graph in async process because METIS will sometimes throw
    # a segmentation fault which we want to raise properly
    try:
        promise = Pool().apply_async(metis.part_graph, args=(), kwds={
            'graph': G,
            'nparts': num_partitions,
            'tpwgts': [
                tuple(
                    1 / num_partitions
                    for i in range(0, len(node_weights_to_ubvec))
                )
                for i in range(0, num_partitions)
            ],
            'ubvec': list(node_weights_to_ubvec.values()),
            'objtype': 'cut',
        })
        (total_volume, parts) = promise.get(timeout=3)
    except TimeoutError as e:
        raise ValueError('METIS failed to partition graph. Try fewer edges or partitions.') from e

    # assign colors according to assigned partition
    colors = get_color_list(num_partitions)
    for i, p in enumerate(parts):
        G.node[i]['color'] = colors[p]

    # remove low-weight and negative edges to clean up the painted graph
    edges = [e for e in G.edges.data()]
    for edge_obj in edges:
        edge_from, edge_to, edge_data = edge_obj
        if edge_data['weight'] < 30:
            G.remove_edge(edge_from, edge_to)

    # convert to pydot
    P = nx.drawing.nx_pydot.to_pydot(G)

    # create subgraphs to cluster students in same class together
    for color in colors:
        subgraph = pydot.Cluster(color, label='test 1', nodesep=7, ranksep=4)
        for node in P.get_node_list():
            if node.get_attributes()['color'] == color:
                subgraph.add_node(node)
        num_students = len(subgraph.get_node_list())
        subgraph.set_label(str(num_students) + ' students')
        P.add_subgraph(subgraph)

    return total_volume, P


# helper function to add visuals to edges
def add_edge(G, node1, node2, weight):
    existing = G.edges.get((node1, node2))

    # do not overwrite an existing edge with heigher weight
    if existing and abs(existing['weight']) > abs(weight):
        return

    # do not overwrite with positive weight if an existing is negative
    if existing and existing['weight'] < 0 and weight > 0:
        return

    G.add_edge(
        node1,
        node2,
        weight=weight,
        label=weight,
        penwidth=min(30, abs(weight)) / 10,
        color='red' if weight < 0 else 'black',
    )


# generate more colors depending on number of partitions
def get_color_list(n):
    colors = ['red', 'blue', 'green', 'magenta', 'yellow', 'teal']

    def r():
        return random.randint(0, 255)

    while n > len(colors):
        colors.append('#%02X%02X%02X' % (r(), r(), r()))
    return colors[:n]


def build_sample():
    return build_graph_from_file(
        filename='students.csv',
        num_partitions=3,
        friendship_weight=30,
        classmate_weight=3,
        schoolmate_weight=1,
        teacher_multiplier=100,
        node_weights_to_ubvec={
            'total': 1.05,
            'gender': 1.20,
            'recommendation_int': 1.40,
        },
    )


if __name__ == '__main__':
    try:
        cost, G = build_sample()
    except ValueError as e:
        print('Failed: ', e)
        sys.exit()

    print('Cost: ', cost)
    G.write('graph.dot')
    print('Written to graph.dot')
