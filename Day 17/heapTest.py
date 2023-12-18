from enum import Enum
import heapq
input = open("Day 17/input.txt", "r").read().split("\n")
input = [list(map(int, line)) for line in input]

nodes : dict = {}

class direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
#Basically going to do Dijkstra's algorithm
#But I will use direction and steps as a two extra dimensions to the graph as well
#This will allow me to keep track of the direction the path is going
#And the number of steps it has taken
#Additionally I will not represent the nodes as objects, but just use a tuple for 
current = (0,0,direction.RIGHT.value,0) # (x, y, direction, steps):cost
queue = [[0,0,current]] #Queue will be a list of tuples (node, cost) so that I can sort it by cost
visited = {} #Visited will be a dictionary of nodes and their costs So I can check if a node has been visited before and if it has been visited with a lower cost
nodes = {current:0} #I do not know if I will need this, but I will keep track of the nodes and their costs
#current = (0,0,direction.DOWN.value,0)
#queue.append([0,0,current])
goal = (len(input) - 1, len(input[0]) - 1)
#print(queue[0])
min_length = 4
def find_connected_nodes(node, min_beforeturn = 4, max_beforeturn = 10):
    cost = node[1]
    node = node[2]
    connected_nodes = []
    steps_left = node[3] + 1 if node[2] == direction.LEFT.value else 1
    steps_right = node[3] + 1 if node[2] == direction.RIGHT.value else 1
    steps_up = node[3] + 1 if node[2] == direction.UP.value else 1
    steps_down = node[3] + 1 if node[2] == direction.DOWN.value else 1
    steps = node[3] + 1 
    if node[0] > 0 and node[2] != direction.DOWN.value and (steps_up <= max_beforeturn and (steps > min_beforeturn or node[2] == direction.UP.value)):
        connected_nodes.append([0, 0,(node[0] - 1, node[1], direction.UP.value, steps_up)])
        connected_nodes[-1][1] = cost + input[node[0] - 1][node[1]]
        connected_nodes[-1][0] += connected_nodes[-1][1] + (abs(goal[0] - connected_nodes[-1][2][0]) + abs(goal[1] - connected_nodes[-1][2][1]))
        #[-1][1] += (abs(goal[0] - connected_nodes[-1][0][0]) + abs(goal[1] - connected_nodes[-1][0][1])*1)

    if node[0] < len(input) - 1 and node[2] != direction.UP.value and (steps_down <= max_beforeturn and (steps > min_beforeturn or node[2] == direction.DOWN.value)):
        connected_nodes.append([0, 0,(node[0] + 1, node[1], direction.DOWN.value, steps_down)])
        connected_nodes[-1][1] = cost + input[node[0] + 1][node[1]]
        connected_nodes[-1][0] += connected_nodes[-1][1] + (abs(goal[0] - connected_nodes[-1][2][0]) + abs(goal[1] - connected_nodes[-1][2][1]))

    if node[1] > 0 and node[2] != direction.RIGHT.value and (steps_left <= max_beforeturn and (steps > min_beforeturn or node[2] == direction.LEFT.value)):
        connected_nodes.append([0, 0,(node[0], node[1] - 1, direction.LEFT.value, steps_left)])
        connected_nodes[-1][1] = cost + input[node[0]][node[1]-1]
        connected_nodes[-1][0] += connected_nodes[-1][1] + (abs(goal[0] - connected_nodes[-1][2][0]) + abs(goal[1] - connected_nodes[-1][2][1]))

    if node[1] < len(input[0]) - 1 and node[2] != direction.LEFT.value and (steps_right <= max_beforeturn and (steps > min_beforeturn or node[2] == direction.RIGHT.value)):
        connected_nodes.append([0, 0,(node[0], node[1] + 1, direction.RIGHT.value, steps_right)])
        connected_nodes[-1][1] = cost + input[node[0]][node[1]+1]
        connected_nodes[-1][0] += connected_nodes[-1][1] + (abs(goal[0] - connected_nodes[-1][2][0]) + abs(goal[1] - connected_nodes[-1][2][1]))
    #for nodes in connected_nodes:
        #if nodes[0] in visited:
            #connected_nodes.remove(nodes)
    return connected_nodes


count = 0
import time
start = time.time()
start2 = time.time()
time_sum = 0
while len(queue) > 0:
    max_cost = 10000000
    start_for = time.time()
    #try:
    current_node = heapq.heappop(queue)
    '''except:
        print(count)
        print(queue)
        break'''
    #print(current_node)
    end_for = time.time()
    time_sum += end_for - start_for
    #current_node = queue.pop(current_x)
    if current_node[2] in visited:
        #print("Already visited", visited[current_node[0]], current_node[1])
        continue
    #print(current_node)
    if current_node[2][0] == goal[0] and current_node[2][1] == goal[1] and current_node[2][3] >= min_length:
        print(goal)
        print("Found goal")
        print(current_node)
        break
    visited[current_node[2]] = current_node[1]
    #print(current_node)
    new_q = find_connected_nodes(current_node)
    for node in new_q:
        heapq.heappush(queue, node)
    count += 1

#404.774453163147
print(time.time() - start2)
#print(input[1][10])