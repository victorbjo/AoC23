input = open("Day 20/input.txt", "r").read().split("\n")
class OpNode():
    def __init__(self,operation_details) -> None:
        self.op_type = operation_details[0][:1]
        self.op_letter = operation_details[0][1:]
        self.op_args = operation_details[2:]
        self.op_args = [arg.replace(",","") for arg in self.op_args]
        self.input = {}
    def update_input(self, input, letter) -> None:
        self.input[letter] = input
    def __repr__(self) -> str:
        return f"OpNode: {self.op_type}{self.op_letter} {self.op_args}, {self.input}"
operations = {}
queue = []
for operation in input:
    operation_node = OpNode(operation.split(" "))
    operations[operation_node.op_letter] = operation_node
    queue.append(operation_node)
    #operations
for node in operations.values():
    for arg in node.op_args:
        queue.append(operations[arg])
for q in queue:
    print(q)
