from typing import List


class PlanningObject:
    """Objects of a planning domain.

    Attributes:
        obj_type (str):
            The type of object in the problem domain.
            Example: "block".
        name (str):
            The name of the object.
            Example: "A"
    """

    def __init__(self, obj_type: str, name: str):
        """Initializes a PlanningObject with a type and a name.

        Args:
            obj_type (str):
                The type of object in the problem domain.
            name (str):
                The name of the object.
        """
        self.obj_type = obj_type
        self.name = name

    def __str__(self):
        return " ".join([self.obj_type, self.name])

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, PlanningObject) and self.name == other.name

    @classmethod
    def from_json(cls, data):
        """Converts a json object to a PlanningObject."""
        return cls(**data)


class Fluent:
    """Fluents of a planning domain.

    Attributes:
        name (str):
            The name of the fluent.
            Example: "holding".
        objects (list):
            The objects this fluent applies to.
            Example: Block A.
    """

    def __init__(self, name: str, objects: List[PlanningObject]):
        """Initializes a Fluent with a name and a list of objects.

        Args:
        name (str):
            The name of the fluent.
        objects (list):
            The objects this fluent applies to.
        """
        self.name = name
        self.objects = objects

    def __str__(self):
        return f"{self.name} {' '.join(map(str, self.objects))}"

    def __hash__(self):
        # Order of objects is important!
        return hash(str(self))

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.name == other.name and self.objects == other.objects
        else:
            return False

    @classmethod
    def from_json(cls, data):
        """Converts a json object to a Fluent."""
        objects = list(map(PlanningObject.from_json, data["objects"]))
        return cls(data["name"], objects)
