class Node():
    def __init__(self, state, parent, action, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class PriorityQueueFrontier(StackFrontier):
    def add(self, node):
        if not any(n.state == node.state and n.cost <= node.cost for n in self.frontier):
            self.frontier.append(node)
            self.frontier = sorted(self.frontier, key=lambda x: x.cost)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class PriorityQueueFrontierDijkstra(StackFrontier):
    def add(self, node):
        if not any(n.state == node.state and n.cost <= node.cost for n in self.frontier):
            self.frontier.append(node)
            self.frontier = sorted(self.frontier, key=lambda x: x.cost)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

