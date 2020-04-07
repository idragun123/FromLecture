import time


class RangeIterator:
    def __init__(self,size):
        self.x = 0
        self.size = size

    def __next__(self):
        self.x += 1
        if self.x > self.size:
            raise StopIteration
        return '#' * self.x


class RangeIterable:
    def __init__(self,size):
        self.size = size

    def __iter__(self):
        return RangeIterator(self.size)


if __name__ == '__main__':
    main_iter = RangeIterable(32)
    for line in main_iter:
        print(line)
        time.sleep(0.25)