class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None ):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

    def print(self):
        # for item in self._items:
        #     print(item)
        print(self._items)

def test_array():
    size = 10
    a = Array(size)
    for _ in range(0,10):
        a[_]=[_]
    # assert a[0] == 0
    # assert len(a) == 10
    a.print()
    print(a[3])
test_array()