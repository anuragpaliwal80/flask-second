from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Models.cloud import Cloud
from Models.ossupport import OSSupport
from Models.test import Test
from Models.machine import Machine
from Models.machineattribute import MachineAttribute
from Models.machinedetail import MachineDetail
from Models.machinetestresult import MachineTestResult

from Models.InitDB import init_database

import datetime


class DataProviderService:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DataProviderService class
        :type engine: string
        """
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

    # Cloud functions

    def add_cloud(self, name):
        """
        Creates and saves a new cloud to the database.

        :param name: Name of the cloud
        :return: The id of the new Candidate
        """

        new_cloud = Cloud(name=name)

        self.session.add(new_cloud)
        self.session.commit()

        return new_cloud.id

    def get_cloud(self, id=None, name=None, serialize=False):
        """
        If the id parameter is  defined then it looks up the cloud with the given id,
        otherwise it loads all the clouds

        :param id: The id of the cloud which needs to be loaded (default value is None)
        :return: The cloud or clouds.
        """

        all_clouds = []

        if id:
            all_clouds = self.session.query(Cloud).filter(Cloud.id == id).all()
        elif name:
            all_clouds = self.session.query(Cloud).filter(Cloud.name == name).all()
        else:
            all_clouds = self.session.query(Cloud).order_by(Cloud.name).all()

        if serialize:
            return [cand.serialize() for cand in all_clouds]
        else:
            return all_clouds

    # ossupport functions
    def get_ossupport(self, id=None, name=None, cloud_id=None, serialize=False):
        """
        If the id parameter is  defined then it looks up the ossupport with the given id,
        otherwise it loads all the ossupports

        :param id: The id of the ossupports which needs to be loaded (default value is None)
        :return: The ossupport or ossupports.
        """

        all_ossupoorts = []

        if id:
            all_ossupoorts = self.session.query(OSSupport).filter(OSSupport.id == id).all()
        elif name:
            all_ossupoorts = self.session.query(OSSupport).filter(OSSupport.name == name).all()
        elif cloud_id:
            all_ossupoorts = self.session.query(OSSupport).filter(OSSupport.cloud == cloud_id).all()
        else:
            all_ossupoorts = self.session.query(OSSupport).order_by(OSSupport.name).all()

        if serialize:
            return [cand.serialize() for cand in all_ossupoorts]
        else:
            return all_ossupoorts

    def add_ossupport(self, name, version,cloud_id):
        """
        Creates and saves a new ossupport to the database.

        :param name: Name of the ossupport
        :return: The id of the new OSSupport
        """

        new_ossupport = OSSupport(name=name,version=version,cloud=int(cloud_id))

        self.session.add(new_ossupport)
        self.session.commit()

        return new_ossupport.id
    # test functions
    def get_test(self,id=None,name=None,serialize=False):
        """
        If the id parameter is  defined then it looks up the test with the given id,
        otherwise it loads all the tests

        :param id: The id of the tests which needs to be loaded (default value is None)
        :return: The test or tests.
        """

        all_tests = []

        if id:
            all_tests = self.session.query(Test).filter(Test.id == id).all()
        elif name:
            all_tests = self.session.query(Test).filter(Test.name == name).all()
        else:
            all_tests = self.session.query(Test).order_by(Test.name).all()

        if serialize:
            return [cand.serialize() for cand in all_tests]
        else:
            return all_tests

    def add_test(self, name):
        """
        Creates and saves a new test to the database.

        :param name: Name of the test
        :return: The id of the new test
        """

        new_test = Test(name=name)

        self.session.add(new_test)
        self.session.commit()

        return new_test.id
    # Machine functions
    def get_machine(self, id=None,name=None,ossupport_id=None,cloud_id=None,serialize=False):
        """
        If the id parameter is  defined then it looks up the machine with the given id,
        otherwise it loads all the machies

        :param id: The id of the machine which needs to be loaded (default value is None)
        :return: The machine or machines.
        """

        all_machines = []
        if id == None and name == None and ossupport_id == None and cloud_id:
            all_ossupoorts = self.get_ossupport(cloud_id=cloud_id)
        if id:
            all_machines = self.session.query(Machine).filter(Machine.id == id).all()
        elif name:
            all_machines = self.session.query(Machine).filter(Machine.name == name).all()
        elif ossupport_id:
            all_machines = self.session.query(Machine).filter(Machine.ossupport == ossupport_id).all()
        elif cloud_id:
            for s in all_ossupoorts:
                all_machines += self.session.query(Machine).filter(Machine.ossupport == s.id).all()
        else:
            all_machines = self.session.query(Machine).order_by(Machine.name).all()
        if serialize:
            return [cand.serialize() for cand in all_machines]
        else:
            return all_machines

    def add_machine(self, name, version, status, released_date, ossupport_id):
        """
        Creates and saves a new machine to the database.

        :param name: Name of the machine
        :return: The id of the new machine
        """
        released_date = datetime.datetime.strptime(released_date, '%d-%m-%Y')
        new_machine = Machine(name=name,version=version,status=status,
                        released_date=released_date,ossupport=int(ossupport_id))

        self.session.add(new_machine)
        self.session.commit()
        return new_machine.id

    # MachineAttributes functions
    def get_machineattribute(self,id=None,name=None,serialize=False):
        """
        If the id parameter is  defined then it looks up the machine with the given id,
        otherwise it loads all the machies

        :param id: The id of the machine which needs to be loaded (default value is None)
        :return: The machine or machines.
        """

        all_machineattributes = []

        if id:
            all_machineattributes = self.session.query(MachineAttribute).filter(MachineAttribute.id == id).all()
        elif name:
            all_machineattributes = self.session.query(MachineAttribute).filter(MachineAttribute.name == name).all()
        else:
            all_machineattributes = self.session.query(MachineAttribute).order_by(MachineAttribute.name).all()

        if serialize:
            return [cand.serialize() for cand in all_machineattributes]
        else:
            return all_machineattributes

    def add_machineattribute(self, name):
        """
        Creates and saves a new new_machineattribute to the database.

        :param name: Name of the new_machineattribute
        :return: The id of the new new_machineattribute
        """

        new_machineattribute = MachineAttribute(name=name)

        self.session.add(new_machineattribute)
        self.session.commit()
        return new_machineattribute.id

    # MachineDetails functions
    def get_machinedetail(self,id=None,machine_id=None,serialize=False):
        """
        If the id parameter is  defined then it looks up the machine with the given id,
        otherwise it loads all the machinedetails

        If the machine_id parameter is  defined then it looks up the machine with the given
        machine_id, otherwise it loads all the machinedetails

        :param id: The id of the machine which needs to be loaded (default value is None)
        :return: The machinedetail or machinedetails.
        """

        all_machindetails = []

        if id:
            all_machindetails = self.session.query(MachineDetail).filter(MachineDetail.id == id).all()
        elif machine_id:
            all_machindetails = self.session.query(MachineDetail).filter(MachineDetail.machine == machine_id).all()
        else:
            all_machindetails = self.session.query(MachineDetail).order_by(MachineDetail.value).all()

        if serialize:
            return [cand.serialize() for cand in all_machindetails]
        else:
            return all_machindetails

    def add_machinedetail(self, value, attribute_id, machine_id):
        """
        Creates and saves a new new_machinedetail to the database.

        :param value: Value of the new_machinedetail
        :param attribute_id: Attribute id of the new_machinedetail
        :param machine_id: Machine id of the new_machinedetail
        :return: The id of the new new_machinedetail
        """

        new_machinedetail = MachineDetail(value=value,attribute=attribute_id,machine=machine_id)

        self.session.add(new_machinedetail)
        self.session.commit()
        return new_machinedetail.id

    # MachineTestResults functions
    def get_machinetestresult(self,id=None,machine_id=None,serialize=False):
        """
        If the id parameter is  defined then it looks up the machine with the given id,
        otherwise it loads all the machinedetails

        :param id: The id of the machine which needs to be loaded (default value is None)
        :return: The machinedetail or machinedetails.
        """

        all_machinetestresults = []

        if id:
            all_machinetestresults = self.session.query(MachineTestResult).filter(MachineTestResult.id == id).all()
        elif machine_id:
            all_machinetestresults = self.session.query(MachineTestResult).filter(MachineTestResult.machine == machine_id).all()
        else:
            all_machinetestresults = self.session.query(MachineTestResult).order_by(MachineTestResult.status).all()

        if serialize:
            return [cand.serialize() for cand in all_machinetestresults]
        else:
            return all_machinetestresults

    def add_machinetestresult(self, status, machine_id, test_id):
        """
        Creates and saves a new new_machinetestresult to the database.

        :param status: Status of the new_machinetestresult
        :param test_id: Test id of the new_machinetestresult
        :param machine_id: Machine id of the new_machinetestresult
        :return: The id of the new new_machinetestresult
        """

        new_machinetestresult = MachineTestResult(test=int(test_id),
                                                    status=status,machine=int(machine_id))

        self.session.add(new_machinetestresult)
        self.session.commit()
        return new_machinetestresult.id

    def machinetestresult_update_status(self, id, new_status):
        nr_of_updated_items = 0

        for m in self.MACHINETESTRESULTS:
            if id == str(m.id):
                m.status = new_status
                nr_of_updated_items += 1
                break

        return nr_of_updated_items

    def delete_machinetestresult(self, id):
        result_for_delete = None
        for m in self.MACHINETESTRESULTS:
            if id == str(m.id):
                result_for_delete = m
                break
        if result_for_delete is not None:
            self.MACHINETESTRESULTS.remove(result_for_delete)
            return True
        else:
            return False
