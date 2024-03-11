import csv
import sys
from util import Node, StackFrontier, QueueFrontier, PriorityQueueFrontier, PriorityQueueFrontierDijkstra

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors

def generic_search(source, target, frontier_type, cost_function=lambda cost: 1):
    start = Node(state=source, parent=None, action=None, cost=0)
    frontier = frontier_type()
    frontier.add(start)

    explored = set()

    while True:
        if frontier.empty():
            raise Exception("no solution")

        node = frontier.remove()

        if node.state == target:
            solution = []
            while node.parent is not None:
                solution.append((node.action, node.state))
                node = node.parent

            solution.reverse()
            return solution

        explored.add(node.state)

        for action, state in neighbors_for_person(node.state):
            cost = cost_function(node.cost)
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action, cost=node.cost + cost)
                frontier.add(child)

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        sys.exit("Usage: python degrees.py [directory] [algorithm]")

    directory = sys.argv[1] if len(sys.argv) == 2 else "small"
    algorithm = sys.argv[2].lower() if len(sys.argv) == 3 else "dijkstra"

    # Load data from files into memory
    print("Loading data...")
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    if algorithm == "dfs":
        path = generic_search(source, target, StackFrontier)
    elif algorithm == "bfs":
        path = generic_search(source, target, QueueFrontier)
    elif algorithm == "ucs":
        path = generic_search(source, target, PriorityQueueFrontier)
    elif algorithm == "dijkstra":
        path = generic_search(source, target, PriorityQueueFrontierDijkstra)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path

        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]

if __name__ == "__main__":
    main()
