class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    @staticmethod
    def heapsort(input_list):
        sort_list = []
        max_heap = MaxHeap()
        for index in input_list:
            max_heap.add(index)
        # Add your code here:

        while len(max_heap.heap_list ) > 1:
            max_value = max_heap.retrieve_max()
            sort_list.append(max_value)

        sort_list.reverse()
        return sort_list

    def retrieve_max(self):
        if self.count == 0:
            return None
        max = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return max

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] < self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            if self.heap_list[idx] < self.heap_list[larger_child_idx]:
                tmp = self.heap_list[larger_child_idx]
                self.heap_list[larger_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = larger_child_idx

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count


# Leave this for testing:
my_list = [42, 70, 38, 12, 94, 28]
sorted_list = MaxHeap.heapsort(my_list)
print(sorted_list)