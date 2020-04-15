# Student Assigner

Algorithmically divides a pool of students into classes, considering as many of their preferences as possible while balancing class size and optionally other attributes.

The repository includes both the script and a flask app and UI currently running on [https://student-assigner.herokuapp.com/](https://student-assigner.herokuapp.com/).

This project was made by [xabepa](https://github.com/xabepa/) and [psaniko](https://github.com/psaniko/). It also served as xabepa's first project to learn programming. As such expect some rough edges :)


## Getting Started

These instructions will teach you how to run the basic script in `solver.py` on your machine.

### Prerequisites

You'll need to have [METIS](http://glaros.dtc.umn.edu/gkhome/metis/metis/download) installed on your system.

[Graphviz](https://graphviz.gitlab.io/download/) is needed if you want to draw the DOT file. On Mac:

```
brew install graphviz
```

### Installing

Install Python requirements

```
pip3 install -r requirements.txt
```

Run the script

```
python3 solver.py
```

### Usage

To generate an image from the DOT file use Graphviz, e.g.

```
dot -Tpng graph.dot -o graph.png
```

## Deployment

To run this on Heroku, fork the repository, push it to Heroku, and install the METIS buildpack

```
heroku buildpacks:add https://github.com/psaniko/heroku-buildpack-metis
```

Add the METIS lib to the Heroku config vars:

```
METIS_DLL = /app/vendor/metis/metis-5.1.0/build/Linux-x86_64/libmetis/libmetis.so
```

## Built With

* [METIS](http://glaros.dtc.umn.edu/gkhome/metis/metis/overview) - The graph partitioning algorithms
* [Graphviz](https://www.graphviz.org/) - Graph visualization
* [d3-graphviz](https://github.com/magjac/d3-graphviz) - JS library to visualize the DOT files

## Contributing

Pull requests welcome!

## License

This project is licensed under the ? - see the [LICENSE.md](LICENSE.md) file for details

