#!/usr/bin/python3

class Fish:
    """
    Represents a generic fish with swimming capabilities.
    """

    def swim(self):
        """
        Simulates the fish swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Displays the natural habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a generic bird with flying capabilities.
    """

    def fly(self):
        """
        Simulates the bird flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Displays the natural habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A hybrid class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """
        Simulates the flying fish soaring above the water.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Simulates the flying fish swimming under the water.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Displays the dual habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
