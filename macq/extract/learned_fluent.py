from typing import List

class LearnedFluent:
    def __init__(self, name: str, objects: List):
        self.name = name
        self.objects = objects

    def __eq__(self, other):
        if not isinstance(other, LearnedFluent):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        # Order of objects is important!
        return hash(self.details())

    def __str__(self):
        return self.details()

    def details(self):
        # objects can be either a list of strings or a list of PlanningObject depending on the token type and extraction method used to learn the fluent
        try:
            string = f"{self.name} {' '.join([o for o in self.objects])}"
        except TypeError:
            string = f"{self.name} {' '.join([o.details() for o in self.objects])}"
        string = f"({string})"

        return string

    def _serialize(self):
        return str(self)