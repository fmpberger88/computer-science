from node import Node
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def visualize(self):
        fig, ax = plt.subplots(figsize=(5, 10))
        current_item = self.top_item
        position = 0

        while current_item:
            rect = patches.FancyBboxPatch((0.1, position - 0.4), 0.8, 0.8, boxstyle="round,pad=0.1", facecolor="#f5f5f5", edgecolor="black")
            ax.add_patch(rect)
            plt.text(0.5, position, current_item.get_value(), ha='center', va='center', fontsize=12, fontweight='bold')
            position -= 1
            current_item = current_item.get_next_node()

        plt.xlim(0, 1)
        plt.ylim(position, + 1)
        plt.axis('off')
        plt.title("Stack Visualization", fontsize=15)
        plt.show()


# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

pizza_stack.visualize()

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
