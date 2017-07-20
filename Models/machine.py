from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Machine(Model):
    __tablename__ = 'machines'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100))
    version = Column(String(10))
    status = Column(String(10))
    released_date = Column(Date)

    machinetestresults = relationship("MachineTestResult")
    machinedetails = relationship("MachineDetail")

    #
    # Reference for the ossupport
    #
    ossupport = Column(Integer, ForeignKey('ossupports.id'))

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "status": self.status,
            "ossupport_id": self.ossupport,
            "released_date": self.released_date,
            "nr_of_machinetestresults": len(self.machinetestresults),
            "nr_of_machinedetails": len(self.machinedetails)
        }
