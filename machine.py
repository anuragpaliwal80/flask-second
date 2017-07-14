import uuid

class Machine:
    __id = None
    __name = None
    __version = None
    __status = None
    __released_date = None
    __ossupport = None

    def __init__(self, name, version, status, released_date,ossupport):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__version = version
        self.__status = status
        self.__released_date = released_date
        self.__ossupport = ossupport

	#
	# PROPERTIES
	#

    @property
    def id(self):
		return self.__id

    @property
    def name(self):
		return self.__name

    @name.setter
    def name(self, value):
		self.__name = value

    @property
    def version(self):
		return self.__version

    @version.setter
    def version(self, value):
		self.__version = value

    @property
    def status(self):
		return self.__status

    @status.setter
    def status(self, value):
		self.__status = value

    @property
    def released_date(self):
		return self.__released_date

    @released_date.setter
    def released_date(self, value):
		self.__released_date = value

    @property
    def ossupport(self):
        return self.__ossupport

    @ossupport.setter
    def ossupport(self,ossupport):
        self.__ossupport = ossupport

	#
	# METHODS
	#

    def serialize(self):
		return {
            "id": self.id,
			"name": self.name,
			"version": self.version,
			"status": self.status,
			"released_date": self.released_date,
            "ossupport": self.ossupport.serialize()
		}
