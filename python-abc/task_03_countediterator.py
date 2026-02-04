#!/usr/bin/python3

class CountedIterator:
    """
    An iterator wrapper that keeps track of the number of items yielded.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator with a given iterable.

        Args:
            iterable: Any object that supports iteration.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Return the current number of items that have been iterated over.

        Returns:
            int: The total count of items yielded so far.
        """
        return self.count

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the original iterable.

        Raises:
            StopIteration: When there are no more items to yield.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """
        Return the iterator object itself, as per the iterator protocol.

        Returns:
            CountedIterator: The current instance.
        """
        return self
