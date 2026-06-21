
class MinHeap:
    def __init__(self, key):
        """Initialize a min heap with a key function.
        
        Args:
            key: Function that extracts the comparable value from each item.
        """
        self.heap = []
        self.key = key                  

    def add(self, item):
        """Add an item to the heap and maintain min-heap property via sift-up."""
        self.heap.append(item)         
        i = len(self.heap) - 1          

        
        while i > 0:
            parent = (i - 1) // 2
            if self.key(self.heap[i]) < self.key(self.heap[parent]):
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break   

    def remove_min(self):
        """Remove and return the minimum item from the heap, maintaining min-heap property via sift-down."""
        if not self.heap:                   # edge case: empty heap
            return None
        min_item = self.heap[0]             # step 1: save the min to return
        last = self.heap.pop()              # remove the last element
        if self.heap:                       # anything left? refill root + sift down
            self.heap[0] = last             # step 2: move last element to the root
            # step 3: sift down from index 0
            i = 0
            n = len(self.heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i                # assume parent is smallest, then test children
                # 1. if LEFT exists (left < n) AND heap[left] is smaller than heap[smallest]:
                if left < n and self.key(self.heap[left]) < self.key(self.heap[smallest]):
                    smallest = left
                # 2. if RIGHT exists (right < n) AND heap[right] is smaller than heap[smallest]:
                if right < n and self.key(self.heap[right]) < self.key(self.heap[smallest]):
                    smallest = right
                # 3. if smallest is STILL i  →  parent already beats both kids, so break
                if smallest == i:
                    break
                # 4. else  →  swap heap[i] with heap[smallest], then set i = smallest
                else:
                    self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                    i = smallest
        return min_item
    
    def is_empty(self):
        """Return True if the heap is empty, False otherwise."""
        return not self.heap

if __name__ == "__main__":
    h = MinHeap(key=lambda x: x)       
    for n in [50, 30, 40, 10, 20]:
        h.add(n)
    print(h.heap)