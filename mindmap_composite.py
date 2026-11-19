import os

class MindMapComposite:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def get_shape_representation(self):
        shapes = {"circle": "(({}))", "oval": "({})", "square": "[{}]", "cloud": "){}(", "hexagon": "{{{{{}}}}}","bang": ")){}(("}
        return shapes.get(self.shape, "{}")

    def display(self, indent=0):
        print(" " * indent + f"{self.name} {self.shape}")
        for child in self.children:
            child.display(indent + 1)
