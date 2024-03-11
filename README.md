# Six Degrees of Kevin Bacon

Welcome to the Six Degrees of Kevin Bacon project repository! This Python project explores the concept of connecting actors in the Hollywood film industry through a series of movies, inspired by the popular game "Six Degrees of Kevin Bacon." The program uses various search algorithms, including Depth-First Search (DFS), Breadth-First Search (BFS), Uniform-Cost Search (UCS), and Dijkstra's Algorithm, to find the shortest path between any two actors.

## Features:

- Find the shortest path between two actors in the Hollywood film industry.
- Utilize different search algorithms to connect actors efficiently.
- Explore and understand the relationships between actors through shared movie appearances.
- Conveniently switch between search algorithms to observe different approaches.

## Getting Started:

1. Download the orginal version of the project from [degrees.zip](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip) and unzip it.
2. Or clone this version which support multiple algorithms.

## Available Algorithms:

- **Depth-First Search (DFS):** Explore the search space by going as deep as possible before backtracking. This algorithm is implemented to find the shortest path between actors.

- **Breadth-First Search (BFS):** Explore the search space level by level, ensuring the shortest path is found first. This algorithm efficiently discovers connections between actors.

- **Uniform-Cost Search (UCS):** An extension of BFS that considers different costs for actions. It guarantees to find the lowest-cost path between two actors.

- **Dijkstra's Algorithm:** Similar to UCS but focuses on finding the shortest paths in a graph. This algorithm considers the total distance traveled so far.

## How to Use:

1. Run the `degrees.py` script with your preferred algorithm as a command-line argument. For example:

    ```bash
    python degrees.py BFS
    ```
    Supported algorithms: `DFS`, `BFS`, `UCS`, `Dijkstra`.

2. Follow the on-screen instructions to input two actor names.
3. Discover the shortest path between the two actors and the movies connecting them.

## Additional Enhancements:

Feel free to explore the code and contribute any additional enhancements or improvements. Share your ideas and collaborate to make this Six Degrees of Kevin Bacon project even more exciting!

## Credits:

This project is based on the Harvard CS50 AI course and has been enhanced with additional features and improvements.

## License:

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact Information:

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Email:** [khdertaleb1@gmail.com](mailto:khdertaleb1@gmail.com)
