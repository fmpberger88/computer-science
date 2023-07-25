from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for i in list_at_array:
            if i[0] == key:
                i[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_array = self.array[array_index]
        for node in list_at_array:
            if node[0] == key:
                return node[1]
            return None

    def get_all_items(self):
        all_items = []
        for linked_list in self.array:
            for node in linked_list:
                all_items.append(node)
        return all_items


blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])


print(blossom.retrieve('rose'))

all_items = blossom.get_all_items()

print(all_items)

for key, value in all_items:
    print("Key: " + key + " Value: " + value)
