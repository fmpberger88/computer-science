import heapq
import networkx as nx
import matplotlib.pyplot as plt
class MinHeap:
    def __init__(self):
        self.heap_list = []
        self.count = 0

    def parent_idx(self, idx):
        return (idx - 1) // 2

    def left_child_idx(self, idx):
        return idx * 2 + 1

    def right_child_idx(self, idx):
        return idx * 2 + 2

    def child_present(self, idx):
        return self.left_child_idx(idx) < self.count

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.count - 1]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) >= self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count - 1 # Start am zuletzt hinzugefügten Element
        while self.parent_idx(idx) >= 0 and \
              self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
            self.heap_list[self.parent_idx(idx)], self.heap_list[idx] = \
            self.heap_list[idx], self.heap_list[self.parent_idx(idx)]
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 0
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                self.heap_list[idx], self.heap_list[smaller_child_idx] = \
                self.heap_list[smaller_child_idx], self.heap_list[idx]
            idx = smaller_child_idx

# Rest des Codes bleibt gleich


def visualize_heap(heap):
    G = nx.DiGraph()

    for i, value in enumerate(heap):
        G.add_node(i, label=str(value))

        parent = (i - 1) // 2
        if i > 0:
            G.add_edge(parent, i)

    pos = hierarchy_pos(G, 0)
    labels = nx.get_node_attributes(G, 'label')

    options = {
        "node_color": 'lightblue',
        "node_size": 2000,
        "font_size": 10,
        "labels": labels,
        "with_labels": True,
        "arrows": False,
    }

    nx.draw(G, pos, **options)
    plt.show()

# Funktion zur Positionierung der Knoten hierarchisch
def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)
    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
    return pos

# Hier kommt Ihre MinHeap-Implementierung

# Beispiel-Nutzung der MinHeap-Klasse
if __name__ == "__main__":
    min_heap = MinHeap()

    # Fügen Sie Elemente zum Min-Heap hinzu
    elements = [4, 8, 2, 6, 10, 1]
    for element in elements:
        min_heap.add(element)

    print("Min-Heap nach dem Einfügen:")
    print(min_heap.heap_list)  # Zeigen Sie den eigentlichen Heap an

    # Entfernen Sie das kleinste Element
    min_element = min_heap.retrieve_min()
    print(f"Entferntes kleinstes Element: {min_element}")

    print("Min-Heap nach der Entfernung:")
    print(min_heap.heap_list)

    # Entfernen Sie das nächste kleinste Element
    min_element = min_heap.retrieve_min()
    print(f"Entferntes kleinstes Element: {min_element}")

    print("Min-Heap nach der weiteren Entfernung:")
    print(min_heap.heap_list)

    min_heap.add(50)
    min_heap.add(26)
    min_heap.add(45)
    min_heap.add(8)
    min_heap.add(13)
    min_heap.add(47)
    min_heap.add(32)
    min_heap.add(18)
    min_heap.add(19)
    min_heap.add(17)
    print("Min-Heap:")
    print(min_heap.heap_list)

    # Hier wird die visualize_heap-Funktion aufgerufen
    visualize_heap(min_heap.heap_list)







