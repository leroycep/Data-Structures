class Heap:
    def __init__(self):
        self.storage = []

    """
    Add a value to the heap
    """
    def insert(self, value):
        new_index = len(self.storage)
        self.storage.append(value)
        self._bubble_up(new_index)

    """
    Removes the greatest value in the heap and returns it
    """
    def delete(self):
        if len(self.storage) == 0:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        max = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return max

    """
    Returns the greatest value in the heap
    """
    def get_max(self):
        return self.storage[0]

    """
    Returns how many elements are in the heap
    """
    def get_size(self):
        return len(self.storage)

    """
    Moves the value up until it is either at the top, or it's parent has a greater
    value than it does. For internal use only.
    """
    def _bubble_up(self, index):
        currentidx = index
        while currentidx != 0:
            parentidx = self._parent(currentidx)
            if self.storage[parentidx] < self.storage[currentidx]:
                self._swap(parentidx, currentidx)
            currentidx = parentidx

    """
    Move the value at the index down, if either of it's children is greater than it.
    For internal use only.
    """
    def _sift_down(self, index):
        val = self.storage[index]
        left = self._get_idx(self._left_child(index))
        if left:
            max_idx = index
            if left > self.storage[max_idx]:
                max_idx = self._left_child(index)

            right = self._get_idx(self._right_child(index))
            if right and right > self.storage[max_idx]:
                max_idx = self._right_child(index)

            if max_idx != index:
                self._swap(max_idx, index)
                self._sift_down(max_idx)

    """
    Get the index of the parent of this index. For internal use only.
    """
    def _parent(self, index):
        return (index - 1) // 2

    """
    Returns the value at the index unless it is out of bounds. Then it returns none.
    """
    def _get_idx(self, index):
        if index < len(self.storage):
            return self.storage[index]
        return None

    """
    Get the index of the left child of this index. For internal use only.
    """
    def _left_child(self, index):
        return 2 * index + 1

    """
    Get the index of the right child of this index. For internal use only.
    """
    def _right_child(self, index):
        return 2 * index + 2

    """
    Swap the two given indexes
    """
    def _swap(self, a, b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]
