import sys

class AbsHeap:
    def __init__(self):
        self.heap = [None]

    def _is_smaller(self, a, b):
        if abs(a) < abs(b):
            return True
        if abs(a) == abs(b) and a < b:
            return True
        return False

    def push(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1
        
        while idx > 1:
            parent_idx = idx // 2
            if self._is_smaller(self.heap[idx], self.heap[parent_idx]):
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
            if right_child < len(self.heap) and self._is_smaller(self.heap[right_child], self.heap[left_child]):
                smallest = right_child
            
            if self._is_smaller(self.heap[smallest], self.heap[idx]):
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break
                
        return root_data

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    abs_heap = AbsHeap()
    results = []

    for i in range(1, n + 1):
        x = int(input_data[i])
        if x == 0:
            results.append(str(abs_heap.pop()))
        else:
            abs_heap.push(x)

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()