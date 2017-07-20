from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model


class MachineAttribute(Model):
    __tablename__ = 'machineattributes'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    machinedetails = relationship("MachineDetail")

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nr_of_machinedetails": len(self.machinedetails)
        }
