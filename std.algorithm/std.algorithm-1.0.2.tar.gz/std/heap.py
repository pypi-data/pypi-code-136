def HeapPermutation(k, A):
    '''
    https://en.wikipedia.org/wiki/Heap%27s_algorithm
    '''
    
    if k == 1:
        yield A
    else:
        # Generate permutations with kth unaltered, Initially k == length(A)
        yield from HeapPermutation(k - 1, A)
        
        # Generate permutations for kth swapped with each k-1 initial
        for i in range(k - 1):
            # Swap choice dependent on parity of k (even or odd)
            if k & 1:
                A[0], A[k - 1] = A[k - 1], A[0]
            else:
                A[i], A[k - 1] = A[k - 1], A[i]
            
            yield from HeapPermutation(k - 1, A)


def generate_all_permutation(A):
    yield from HeapPermutation(len(A), A)        

        
def skip_first_permutation(A):
    generator = HeapPermutation(len(A), A)
    next(generator)
    yield from generator


import heapq


class TopKHeap:

    def __init__(self, k):
        self.data = []
        self.k = k

    def __str__(self):
        return str(self.data)
    
    __repr__ = __str__
    
    def push(self, num):
        #internally, it is a minimum heap!
        if len(self.data) < self.k:
            heapq.heappush(self.data, num)
        elif num > self.data[0]:
            heapq.heapreplace(self.data, num)

    def topk(self):
        
        arr = []
        while self.data: 
            a = heapq.heappop(self.data)
            arr.append(a)
            
        arr.reverse()
        return arr
    

