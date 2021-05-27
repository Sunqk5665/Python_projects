import random
import string
from timeit import default_timer as timer

class SelectionSort(object):
    items=[]
    def __init__(self,items):
        self.items = items

    def sort(self):
        print("iten len: %d" % len(self.items))
        for i in range(len(self.items)-1,0,-1):
            maximum = i
            for j in range(0,i):
                if (self.items[i] < self.items[j]):
                    maximum = j
            self.items[i],self.items[maximum]=self.swap(self.items[i],self.items[maximum])
    def swap(self,i,j):
        temp = j
        j = i
        i = temp
        return i,j

print("-"*10 + "sorting numbers" + "_"*10)
items = []
# generate random numbers and put in items
for i in range(0,10):
    items.append(random.randint(2,999))
print("original items: %r" % items)

ssort = SelectionSort(items)

# calculate execution time for our selection sort method
start = timer()
ssort.sort()
end = timer()
duration1 = end - start
# calculate execution time for python built-in sort method
start = timer()
items.sort()
end = timer()
duration2 = end - start

assert ssort.items == items
print("sorted items: %r" % ssort.items)
print("Duration: our selection sort method - %ds, python builtin sort - %ds" % (duration1, duration2))