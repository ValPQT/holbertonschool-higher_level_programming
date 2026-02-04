#!/usr/bin/python3

class VerboseList(list):
    """
    A subclass of the built-in list that prints a message to the console
    whenever the list is modified.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a confirmation.

        Args:
            item: The object to be added to the list.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extends the list by appending all items from the given iterable.

        Args:
            iterable: A collection of elements to add.
        """
        size = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {size} items.")

    def remove(self, value):
        """
        Removes the first occurrence of a value and prints a confirmation.

        Args:
            value: The element to search for and remove.

        Raises:
            ValueError: If the value is not found in the list.
        """
        super().remove(value)
        print(f"Removed {value} from the list.")

    def pop(self, index=-1):
        """
        Removes and returns the element at the specified index.

        Args:
            index (int): The position of the element to remove. Defaults to -1.

        Returns:
            The element that was removed from the list.
        """
        value = super().pop(index)
        print(f"Popped {value} from the list.")
        return value
