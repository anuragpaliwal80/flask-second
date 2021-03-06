from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model


class Test(Model):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    machinetestresults = relationship("MachineTestResult")

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nr_of_machinetestresults": len(self.machinetestresults)
        }
