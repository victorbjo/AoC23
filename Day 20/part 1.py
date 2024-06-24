import enum

input = open("Day 20/input.txt", "r").read().split("\n")


class Type(enum.Enum):
    flip_flop = enum.auto()
    conjunction = enum.auto()
    broadcast = enum.auto()


type_map = {"%": Type.flip_flop, "&": Type.conjunction, "b": Type.broadcast}
pulses = []
lows = [0]
highs = [0]


class Node:
    def __init__(self, type, id, next):
        self.type = type_map[type]
        self.id = id
        self.next = next
        self.state_current = 0
        self.memory = {}

    def __str__(self):
        return f"{self.type} {self.id} {self.next}"

    def __repr__(self):
        return f"{self.type} {self.id} {self.next}"

    def receive(self, value, sender):
        if self.type == Type.flip_flop:
            if value == 1:
                pass
            else:
                if self.state_current == 0:
                    self.state_current = 1
                    self.send(1)
                else:
                    self.state_current = 0
                    self.send(0)
        elif self.type == Type.conjunction:
            self.memory[sender] = value
            if all(value == 1 for value in self.memory.values()):
                self.send(0)
            else:
                self.send(1)
        elif self.type == Type.broadcast:
            self.send(0)

    def send(self, pulse):
        for receiver in self.next:
            pulses.append({"receiver": receiver, "pulse": pulse, "sender": self.id})
            # if self.type != Type.broadcast:
            if pulse == 1:
                highs[0] += 1
            else:
                lows[0] += 1


nodes = {}
for line in input:
    node_data, receivers = line.split(" -> ")
    receivers = receivers.split(", ")
    new_node = Node(node_data[0], node_data[1:], receivers)
    nodes[node_data[1:]] = new_node
for node in nodes.values():
    for receiver in node.next:
        if receiver not in nodes.keys():
            pass
        else:
            nodes[receiver].memory[node.id] = 0


button_pushes = 1000
ptype = {0: "low", 1: "high"}
for x in range(button_pushes):
    lows[0] += 1
    nodes["roadcaster"].receive(0, "start")
    while pulses:
        pulse = pulses.pop(0)
        # print(f'{pulse["sender"]} -{ptype[pulse["pulse"]]} -> {pulse["receiver"]}')
        if pulse["receiver"] in nodes.keys():
            nodes[pulse["receiver"]].receive(pulse["pulse"], pulse["sender"])

print(f"Highs: {highs}, Lows: {lows}")
print(highs[0] * lows[0])
