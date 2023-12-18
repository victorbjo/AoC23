from enum import Enum
input = open("Day 17/input.txt", "r").read().split("\n")
input = [list(map(int, line)) for line in input]

nodes : dict = {}

class direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
class node():
    def __init__(self, x, y, directions = [], input = input, nodes = nodes):
        self.x = x
        self.y = y
        self.input = input
        self.nodes = nodes
        self.nodes[(x, y)] = self
        self.cost = self.get_cost()
        self.neighbors = self.get_neighbors()
        self.intrinsic_cost = 10000000
        self.directions = []
        self.previous_node = None
    def get_cost(self):
        return self.input[self.x][self.y]
    def get_neighbors(self):
        neighbors = {"UP": None, "DOWN": None, "LEFT": None, "RIGHT": None}
        if self.x > 0:
            neighbors["UP"] = (node(self.x - 1, self.y, self.input) if nodes.get((self.x - 1, self.y)) == None else nodes[(self.x - 1, self.y)])
        if self.x < len(self.input) - 1:
            neighbors["DOWN"] = (node(self.x + 1, self.y, self.input) if nodes.get((self.x + 1, self.y)) == None else nodes[(self.x + 1, self.y)])
        if self.y > 0:
            neighbors["LEFT"] = (node(self.x, self.y - 1, self.input) if nodes.get((self.x, self.y - 1)) == None else nodes[(self.x, self.y - 1)])
        if self.y < len(self.input[0]) - 1:
            neighbors["RIGHT"] = (node(self.x, self.y + 1, self.input) if nodes.get((self.x, self.y + 1)) == None else nodes[(self.x, self.y + 1)])
        return neighbors
    def __repr__(self):
        return f"[({self.x}, {self.y}) {self.cost, self.intrinsic_cost}] "
current_node = node(0, 0)
current_node.intrinsic_cost = current_node.cost
print(nodes[(1,0)].neighbors)
#nodes[(0,0)] = current_nodequeue
queue = []
queue.append(current_node)
visited = [current_node]
goal = nodes[(len(input) - 1, len(input[0]) - 1)]
#print(goal)

directions = []
import time
while len(queue) > 0:
    #time.sleep(len(queue)+2)
    cost = 1000000
    x = 0
    for x, node in enumerate(queue):
        if node.intrinsic_cost < cost:
            print(node.intrinsic_cost, "intrinsic cost", x)
            cost = node.intrinsic_cost
            nodeIndex = x
    current_node = queue.pop(nodeIndex)
    print(current_node.intrinsic_cost, "current node intrinsic cost")
    if current_node == goal:
        print(current_node.intrinsic_cost)
        print(current_node.directions)
        print("found goal")
        break
    for direction in current_node.neighbors.keys():
        neighbor = current_node.neighbors[direction]
        if neighbor != None:
            if neighbor.intrinsic_cost >= current_node.intrinsic_cost + neighbor.cost:
                if len(current_node.directions) ==3:
                    if current_node.directions[0] == current_node.directions[1] == current_node.directions[2] == direction:
                        continue
                neighbor.intrinsic_cost = min(current_node.intrinsic_cost + neighbor.cost, neighbor.intrinsic_cost)
                neighbor.directions = current_node.directions[-2:] + [direction]
                neighbor.previous_node = current_node
                queue.append(neighbor)
    #print(current_node, queue)


    
#print(current_node.neighbors)
dirs = []
current = goal
while current.directions != []:
    dirs = [current.directions[-1]] + dirs
    #print(current.directions[-1])
    current = current.previous_node
print(dirs)