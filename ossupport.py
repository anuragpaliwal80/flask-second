import uuid

class OSSupport:
    __id = None
    __name = None
    __version = None
    __cloud = None

    def __init__(self, name, version, cloud):
		self.__id = uuid.uuid4()
		self.__name = name
		self.__version = version
		self.__cloud = cloud

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
    def cloud(self):
		return self.__cloud

    @cloud.setter
    def cloud(self, value):
		self.__cloud = value

	#
	# METHODS
	#

    def serialize(self):
		return {
            "id": self.id,
			"name": self.name,
			"version": self.version,
			"cloud": self.cloud.serialize()
		}
