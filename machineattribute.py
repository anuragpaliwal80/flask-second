import uuid


class MachineAttribute:
    __id = None
    __name = ""

    def __init__(self, name):
        self.__id = uuid.uuid4()
        self.__name = name

    #
    # PROPERTIES
    #

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            }
