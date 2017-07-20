from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class MachineDetail(Model):
    __tablename__ = 'machinedetails'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    value = Column(String(100))
    #
    # Reference for the machine
    #
    machine = Column(Integer, ForeignKey('machines.id'))
    #
    # Reference for the machineattribute
    #
    attribute = Column(Integer, ForeignKey('machineattributes.id'))

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "value": self.value,
            "machine_id": self.machine,
            "attribute_id": self.attribute
        }
