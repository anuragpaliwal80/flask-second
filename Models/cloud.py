from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model


class Cloud(Model):
    __tablename__ = 'clouds'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    ossupports = relationship("OSSupport")

    #
    # METHODS
    #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nr_of_ossupports": len(self.ossupports)
        }
