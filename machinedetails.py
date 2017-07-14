import uuid

class MachineDetails:
    __id = None
    __attribute = None
    __value = None
    __machine = None

    def __init__(self, value, attribute=[], machine=[]):
		self.__id = uuid.uuid4()
		self.__attribute = attribute
		self.__value = value
		self.__machine = machine

	#
	# PROPERTIES
	#

    @property
    def id(self):
		return self.__id

    @property
    def attribute(self):
		return self.__attribute

    @attribute.setter
    def attribute(self, value):
		self.__attribute = value

    @property
    def value(self):
		return self.__value

    @value.setter
    def value(self, value):
		self.__value = value

    @property
    def machine(self):
		return self.__machine

    @machine.setter
    def machine(self, value):
		self.__machine = value

	#
	# METHODS
	#
    def serialize(self):
		return {
          "id": self.id,
			"attribute": self.attribute.serialize(),
			"value": self.value,
			"machine": self.machine.serialize()
		}
    # def serialize(self):
	# 	return {
    #       "id": self.id,
	# 		"attribute": [a.serialize() for a in self.attribute],
	# 		"value": self.value,
	# 		"machine": [m.serialize() for m in self.machine]
	# 	}
