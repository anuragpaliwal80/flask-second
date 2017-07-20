from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class MachineTestResult(Model):
    __tablename__ = 'machinetestresults'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column(String(100))
    #
    # Reference for the machine
    #
    machine = Column(Integer, ForeignKey('machines.id'))
    #
    # Reference for the test
    #
    test = Column(Integer, ForeignKey('tests.id'))

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "machine_id": self.machine,
            "test_id": self.test
        }
