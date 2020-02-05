# sort-visualizer
This project visualizes the sorting of colors using various sorting algorithms. The workloads are also multithreaded so you can see the algorithm working in multiple lines (Multi-Algorithm Searching visualizes the differences pretty nicely). So far the algorithms implemented are Insertion, Selection, Bubble, and Merge Sorts. (Multi Algorithm Sorting uses the algorithms in this order: Bubble, Insertion, Merge, Selection)

## Setting Up
You must have a python environment with [PyGame](https://www.pygame.org/) and the [NumPy](https://numpy.org/) modules.

This install line should do the trick: ```pip install pygame numpy```

After that you can just run the main.py file and get started

## Controls
Randomize the colors - F5

Start Algorithm - Return or Enter

Change Algorithm - Left/Right Arrow Keys

Change Increment Size - Up/Down Arrow Keys

Toggle step timer (Fast Step): s

## Problems
* The algorithm times are relatively inaccurate. Selection sort is blazingly fast (Probably because it doesn't require copying as much data) while the other sorts seem slow in comparison. I need to find a way to accurately represent each algorithm's strengths

## Future Goals
* Add Play/Pausing (Probably not going to happen atm b/c requires complete rewrite)
* More Algorithms

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used
* [PyGame](https://www.pygame.org/) - Visuals
* [NumPy](https://numpy.org/) - Grid System

## Authors

* **Vel0ciTy** - *Main Author* - [Website (WIP)](https://lecongkhoiviet.netlify.com/) 😁

## Acknowledgments

* StackOverflow 😀
* [Geeks for Geeks](https://www.geeksforgeeks.org/sorting-algorithms/) Huge help with learning about and visualizing the algorithms. The difference in data structures made it difficult to implement the algorithms at first but this site made it really easy to learn
