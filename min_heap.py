# Implement a min heap data structure

class binary_min_heap:
    def __init__(self):
        self.heap_list = []
        self.current_len = 0

    def shift_up(self, size):
        while size // 2 > 0:
            if self.heap_list[size] < self.heap_list[size//2]:
                self.heap_list[size] , self.heap_list[size//2] = self.heap_list[size//2] , self.heap_list[size]
            size = size // 2

    def shift_down(self, size):
        while (size * 2) <= self.current_len:
            mc = self.min_child(size)
            if self.heap_list[size] > self.heap_list[mc]:
                self.heap_list[size], self.heap_list[mc] = self.heap_list[mc], self.heap_list[size]
            size = mc

    def min_child(self, ind):
        if ind * 2 + 1 > self.current_len:
            return ind * 2
        else:
            if self.heap_list[ind * 2] < self.heap_list[ind * 2 + 1]:
                return ind * 2
            else:
                return ind * 2 + 1
    def insert_child(self, ele):
        self.heap_list.append(ele)
        self.current_len += 1
        self.shift_up(self.current_len)

    def del_min_child(self):
        temp = self.heap_list[1]
        self.heap_list[self.current_len]
        self.current_len -= 1
        self.heap_list.pop()
        self.shift_down(1)
        print(temp)

    def build_min_heap(self, h_list):
        mid = len(h_list) // 2
        self.current_len = len(h_list)
        self.heap_list = [0] + h_list[:]
        while(mid > 0):
            self.shift_down(mid)
            mid -= 1

    def print_heap(self):
        for i in range(1,len(self.heap_list)):
            print(self.heap_list[i])

mh = binary_min_heap()
a_list = [12,11,13,1,6,7]
mh.build_min_heap(a_list)
mh.print_heap()
















