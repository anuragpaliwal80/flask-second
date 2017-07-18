from clouddatagenerator import CloudDataGenerator

from cloud import Cloud
from ossupport import OSSupport
from test import Test
from machine import Machine
from machineattribute import MachineAttribute
from machinedetails import MachineDetails
from machinetestresults import MachineTestResults

import datetime


class DataProviderService:
    def __init__(self, nr_of_items):
        self.CLOUDS = None
        self.OSSUPPORTS = None
        self.MACHINES = None
        self.MACHINEATTRIBUTES = None
        self.TESTS = None

        self.MACHINEDETAILS = None
        self.MACHINETESTRESULTS = None

        self.cloud_data_generator = CloudDataGenerator()
        self.MACHINEDETAILS = self.cloud_data_generator.generate_machinedetails()
        self.MACHINETESTRESULTS = self.cloud_data_generator.generate_machinetestresults()

        self.CLOUDS = self.cloud_data_generator.generate_clouds()
        self.OSSUPPORTS = self.cloud_data_generator.generate_ossupports()
        self.MACHINES = self.cloud_data_generator.generate_machines()
        self.MACHINEATTRIBUTES = self.cloud_data_generator.generate_machineattributes()
        self.TESTS = self.cloud_data_generator.generate_tests()

        # self.data_generator = DataGenerator()
        # self.CANDIDATES = self.data_generator.generate_candidates(nr_of_items)

    # Cloud functions
    def get_clouds(self):
        return self.CLOUDS

    def get_cloud(self, id):
        result = None
        if id and self.CLOUDS:
            for c in self.CLOUDS:
                if id == str(c.id):
                    result = c
                    break
        return result

    def get_cloud_by_name(self,name):
        result = None
        if name and self.CLOUDS:
            for m in self.CLOUDS:
                if name == str(m.name):
                    result = m
                    break
        return result

    def add_cloud(self, name):
        c = Cloud(name)
        if self.CLOUDS == None:
            self.CLOUDS = []
        self.CLOUDS.append(c)
        return str(c.id)

    def ossupports_by_cloudid(self,id):
        result = None
        if self.get_cloud(id) == None:
            return result
        result = []
        if id and self.OSSUPPORTS:
            for c in self.OSSUPPORTS:
                if id == str(c.cloud.id):
                    result.append(c)
        return result
    def machines_by_cloudid(self,id):
        result = None
        if self.get_cloud(id) == None:
            return result
        result = []
        for m in self.MACHINES:
            if id == str(m.ossupport.cloud.id):
                result.append(m)
        return result
    # ossupport functions
    def get_ossupports(self):
        return self.OSSUPPORTS

    def get_ossupport(self, id):
        result = None
        if id and self.OSSUPPORTS:
            for c in self.OSSUPPORTS:
                if id == str(c.id):
                    result = c
                    break
        return result

    def get_ossupport_by_name(self,name):
        result = None
        if name and self.OSSUPPORTS:
            for m in self.OSSUPPORTS:
                if name == str(m.name):
                    result = m
                    break
        return result

    def add_ossupport(self, name):
        c = OSSupport(name)
        if self.OSSUPPORTS == None:
            self.OSSUPPORTS = []
        self.OSSUPPORTS.append(c)
        return str(c.id)
    # test functions
    def get_tests(self):
        return self.TESTS

    def get_test(self, id):
        result = None
        if id and self.TESTS:
            for c in self.TESTS:
                if id == str(c.id):
                    result = c
                    break
        return result

    def get_test_by_name(self,name):
        result = None
        if name and self.TESTS:
            for m in self.TESTS:
                if name == str(m.name):
                    result = m
                    break
        return result

    def add_test(self, name):
        c = Test(name)
        if self.TESTS == None:
            self.TESTS = []
        self.TESTS.append(c)
        return str(c.id)
    # Machine functions
    def get_machines(self):
        return self.MACHINES

    def get_machine(self, id):
        result = None
        if id and self.MACHINES:
            for m in self.MACHINES:
                if id == str(m.id):
                    result = m
                    break
        return result
    def get_machine_by_name(self,name):
        result = None
        if name and self.MACHINES:
            for m in self.MACHINES:
                if name == str(m.name):
                    result = m
                    break
        return result

    def add_machine(self, name, version, status, released_date):
        m = Machine(name, version, status, released_date)
        if self.MACHINES == None:
            self.MACHINES = []
        self.MACHINES.append(m)
        return str(m.id)
    def machinetestresults_by_machineid(self,id):
        result = None
        if self.get_machine(id) == None:
            return result
        result = []
        for m in self.MACHINETESTRESULTS:
            if id == str(m.machine.id):
                result.append(m)
        return result
    def machinedetails_by_machineid(self,id):
        result = None
        if self.get_machine(id) == None:
            return result
        result = []
        for m in self.MACHINEDETAILS:
            if id == str(m.machine.id):
                result.append(m)
        return result
    # MachineAttributes functions
    def get_machineattributes(self):
        return self.MACHINEATTRIBUTES

    def get_machineattribute(self, id):
        result = None
        if id and self.MACHINEATTRIBUTES:
            for m in self.MACHINEATTRIBUTES:
                if id == str(m.id):
                    result = m
                    break
        return result
    def get_machineattribute_by_name(self,name):
        result = None
        if name and self.MACHINEATTRIBUTES:
            for m in self.MACHINEATTRIBUTES:
                if name == str(m.name):
                    result = m
                    break
        return result

    def add_machineattribute(self, name):
        m = MachineAttribute(name)
        if self.MACHINEATTRIBUTES == None:
            self.MACHINEATTRIBUTES = []
        self.MACHINEATTRIBUTES.append(m)
        return str(m.id)
    # MachineDetails functions
    def get_machinedetails(self):
        return self.MACHINEDETAILS

    def get_machinedetail(self, id):
        result = None
        if id and self.MACHINEDETAILS:
            for m in self.MACHINEDETAILS:
                if id == str(m.id):
                    result = m
                    break
        return result

    def add_machinedetail(self, value, attribute, machine):
        m = MachineDetails( value,attribute, machine)
        if self.MACHINEDETAILS == None:
            self.MACHINEDETAILS = []
        self.MACHINEDETAILS.append(m)
        return str(m.id)

    # MachineTestResults functions
    def get_machinetestresults(self):
        return self.MACHINETESTRESULTS

    def get_machinetestresult(self, id):
        result = None
        if id and self.MACHINETESTRESULTS:
            for m in self.MACHINETESTRESULTS:
                if id == str(m.id):
                    result = m
                    break
        return result

    def add_machinetestresult(self, test, status, machine):
        m = MachineTestResults( test, status, machine)
        if self.MACHINETESTRESULTS == None:
            self.MACHINETESTRESULTS = []
        self.MACHINETESTRESULTS.append(m)
        return str(m.id)

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

    # Rest of the code
    def get_candidates(self):
        return self.CANDIDATES

    def get_candidate(self, id):
        result = None
        if id:
            for cand in self.CANDIDATES:
                if id == str(cand["id"]):
                    result = cand
                    break
        return result

    def get_random_candidates(self, nr_of_candidates):
        return self.data_generator.generate_candidates(nr_of_candidates)

    def update_name(self, id, new_name):
        nr_of_updated_items = 0

        for cand in self.CANDIDATES:
            if id == str(cand["id"]):
                cand["first_name"] = new_name
                nr_of_updated_items += 1
                break

        return nr_of_updated_items

    def delete_candidate(self, id):
        cand_for_delete = None
        for cand in self.CANDIDATES:
            if id == str(cand["id"]):
                cand_for_delete = cand
                break

        if cand_for_delete is not None:
            self.CANDIDATES.remove(cand_for_delete)
            return True
        else:
            return False

    def add_candidate(self, first_name, last_name):
        cand = Candidate(first_name, last_name, [])
        self.CANDIDATES.append(cand.serialize())
        return str(cand.id)

    def add_project(self, project_name, project_description):
        new_project = Project(project_name, datetime.datetime.utcnow(), datetime.datetime.utcnow(), project_description)

        self.CANDIDATES[0]['experience'][0]['projects'].append(new_project.serialize())
        return str(new_project.id)


    def get_random_projects(self, nr_of_projects):
        return self.data_generator.generate_projects(nr_of_projects, True)
