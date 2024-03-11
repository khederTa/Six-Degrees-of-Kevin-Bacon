# Six Degrees of Kevin Bacon

Welcome to the Six Degrees of Kevin Bacon project repository! This Python project explores the concept of connecting actors in the Hollywood film industry through a series of movies, inspired by the popular game "Six Degrees of Kevin Bacon." The program uses various search algorithms, including Depth-First Search (DFS), Breadth-First Search (BFS), Uniform-Cost Search (UCS), and Dijkstra's Algorithm, to find the shortest path between any two actors.

## Features:

- Find the shortest path between two actors in the Hollywood film industry.
- Utilize different search algorithms to connect actors efficiently.
- Explore and understand the relationships between actors through shared movie appearances.
- Conveniently switch between search algorithms to observe different approaches.

## Getting Started:

1. Download the project code from [degrees.zip](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip) and unzip it.
2. Open a terminal and navigate to the project directory.

## Available Algorithms:

- **Depth-First Search (DFS):** Explore the search space by going as deep as possible before backtracking. This algorithm is implemented to find the shortest path between actors.

- **Breadth-First Search (BFS):** Explore the search space level by level, ensuring the shortest path is found first. This algorithm efficiently discovers connections between actors.

- **Uniform-Cost Search (UCS):** An extension of BFS that considers different costs for actions. It guarantees to find the lowest-cost path between two actors.

- **Dijkstra's Algorithm:** Similar to UCS but focuses on finding the shortest paths in a graph. This algorithm considers the total distance traveled so far.

## Setting Up a Virtual Environment:

It's recommended to use a virtual environment to isolate your project's dependencies. Follow these steps to set up a virtual environment using `venv`:

### Install Virtualenv:

If you haven't installed `venv` (virtualenv), run the following command:

```bash
pip install virtualenv
```

### Create a Virtual Environment:

Navigate to your project folder in the terminal and run:

```bash
python -m venv env
```

### Activate the Virtual Environment:

On Mac:

```bash
source env/bin/activate
```

On Windows (CMD):

```bash
env\Scripts\activate.bat
```

On Windows (PowerShell):

```bash
env\Scripts\Activate.ps1
```

### Install Project Dependencies:

Install the required dependencies for the Six Degrees of Kevin Bacon project:

```bash
pip install -r requirements.txt
```

### Create a Requirements File:

Generate a requirements.txt file to document your project's dependencies:

```bash
pip freeze > requirements.txt
```

## How to Use:

1. Run the `degrees.py` script with your preferred algorithm as a command-line argument. For example:

    ```bash
    python degrees.py BFS
    ```

    Supported algorithms: `DFS`, `BFS`, `UCS`, `Dijkstra`.

2. Follow the on-screen instructions to input two actor names.
3. Discover the shortest path between the two actors and the movies connecting them.

## Additional Enhancements:

Feel free to explore the code and contribute any additional enhancements or improvements. Share your ideas and collaborate to make this Tic-Tac-Toe project even more exciting!

## Credits:

This project is based on the Harvard CS50 AI course and has been enhanced with additional features and improvements.

## License:

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact Information:

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Email:** [khdertaleb1@gmail.com](mailto:khdertaleb1@gmail.com)
