from typing import List

class reverseList(object):
    def __init__(self, l: List[str]):
        self.l = l
    
    def reverse_list(self):
        self.l.reverse()

    def reverse_list_idx(self):
        self.l = self.l[-1::-1]

    def reverse_list_iter(self):
        for i in range(len(self.l) // 2):
            self.l[i], self.l[-i-1] = self.l[-i-1], self.l[i]

    def reverse_list_rec(self):
        def rec_func(left=0, right=len(self.l)-1):
            if left < right:
                self.l[left], self.l[right] = self.l[right], self.l[left]
                rec_func(left + 1, right - 1)
        rec_func()
    
