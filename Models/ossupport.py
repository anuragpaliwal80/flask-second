from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class OSSupport(Model):
    __tablename__ = 'ossupports'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100))
    version = Column(String(10))

    machines = relationship("Machine")

    #
    # Reference for the cloud
    #
    cloud = Column(Integer, ForeignKey('clouds.id'))

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "cloud_id": self.cloud,
            "nr_of_machines": len(self.machines)
        }
