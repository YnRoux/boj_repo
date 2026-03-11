import sys

class MinHeap:
    def __init__(self):
        self.heap = [None]

    def push(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1
        
        while idx > 1:
            parent_idx = idx // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def pop(self):
        if len(self.heap) <= 1:
            return 0
        
        if len(self.heap) == 2:
            return self.heap.pop()

        root_data = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        idx = 1
        while idx * 2 < len(self.heap):
            left_child = idx * 2
            right_child = idx * 2 + 1
            smallest = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smallest = right_child
            
            if self.heap[idx] > self.heap[smallest]:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break
                
        return root_data

input = sys.stdin.read
data = input().split()
n = int(data[0])
min_heap = MinHeap()
results = []

for i in range(1, n + 1):
    x = int(data[i])
    if x == 0:
        results.append(str(min_heap.pop()))
    else:
        min_heap.push(x)

print("\n".join(results))