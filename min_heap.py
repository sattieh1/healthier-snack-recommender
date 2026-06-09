class MinHeap:
    def __init__(self, key):
        self.heap = []
        self.key = key                  

    def add(self, snack):
        self.heap.append(snack)         
        i = len(self.heap) - 1          

        
        while i > 0:
            parent = (i - 1) // 2
            if self.key(self.heap[i]) < self.key(self.heap[parent]):
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break   

