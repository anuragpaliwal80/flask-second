import uuid

class MachineTestResults:
    __id = None
    __test = None
    __status = None
    __machine = None

    def __init__(self, test, status, machine):
		self.__id = uuid.uuid4()
		self.__test = test
		self.__status = status
		self.__machine = machine

	#
	# PROPERTIES
	#

    @property
    def id(self):
		return self.__id

    @property
    def test(self):
		return self.__test

    @test.setter
    def test(self, value):
		self.__test = value

    @property
    def status(self):
		return self.__status

    @status.setter
    def status(self, value):
		self.__status = value

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
			"test": self.test.serialize(),
			"status": self.status,
			"machine": self.machine.serialize()
		}
	# def serialize(self):
	# 	return {
    #         "id": self.id,
	# 		"test": [t.serialize() for t in self.test],
	# 		"status": self.status,
	# 		"machine": [m.serialize() for m in self.machine]
	# 	}
