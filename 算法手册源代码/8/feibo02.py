import random,time

class Search:
    def sequentialSearch(self, array, key):
        # 顺序查找
        for i in range(len(array)):
            if array[i] == key:
                return i
        return None

    def binarySearch(self, array, key):
        # 有序表查找——折半查找
        left = 0
        right = len(array) - 1
        while left < right:
            if key >= array[left] and key <= array[right]:
                mid = (left + right) // 2
                if array[mid] > key:
                    right = mid
                elif array[mid] < key:
                    left = mid
                else:
                    return mid
                continue

    def interpolationSearch(self, array, key):
        # 有序表查找——插值查找
        left = 0
        right = len(array) - 1
        while left < right:
            if key >= array[left] and key <= array[right]:
                mid = left + int((right - left) * (key - array[left]) / (array[right] - array[left]))
                if array[mid] > key:
                    right = mid
                elif array[mid] < key:
                    left = mid
                else:
                    return mid

    def fibonacciSearch(self, array, key):
        # 有序表查找——斐波那契查找
        fibonacci_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233, 377, 610, 987,
                          1597, 2584, 4181, 6765,10946, 17711, 28657, 46368]
        n = len(array)
        for i in range(len(fibonacci_list)):
            if fibonacci_list[i] >= n:
                ind = i
                break

        if fibonacci_list[ind] > n:
            array.extend([array[-1]] * (fibonacci_list[ind] - n))

        left = 0
        right = fibonacci_list[ind] - 1
        while left < right and ind - 1 >= 0 and ind - 2 >= 0:
            mid = left + fibonacci_list[ind - 1]
            if array[mid] < key:
                left = mid
                ind -= 2
            elif array[mid] > key:
                right = mid
                ind -= 1
            else:
                return mid

if __name__ == '__main__':
    list = [random.randint(0,999) for i in range(10000)]
    s = Search()
    key = random.randint(0,999)

    start = time.perf_counter()
    index = s.sequentialSearch(list, key)
    end = time.perf_counter()
    print('顺序查找             ', end - start, '\n','结果：              ', key == list[index])

    list1 = sorted(list.copy())
    start = time.perf_counter()
    index = s.binarySearch(list1, key)
    end = time.perf_counter()
    print('二分查找             ', end - start, '\n', '结果：              ', key == list1[index])

    list2 = sorted(list.copy())
    start = time.perf_counter()
    index = s.interpolationSearch(list2, key)
    end = time.perf_counter()
    print('插值查找             ', end - start, '\n', '结果：              ', key == list2[index])

    list3 = sorted(list.copy())
    start = time.perf_counter()
    index = s.fibonacciSearch(list3, key)
    end = time.perf_counter()
    print('Fibonacci查找        ', end - start, '\n', '结果：              ', key == list3[index])
