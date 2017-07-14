import random
import datetime

from cloud import Cloud
from test import Test
from ossupport import OSSupport
from machine import Machine
from machineattribute import MachineAttribute
from machinedetails import MachineDetails
from machinetestresults import MachineTestResults

class CloudDataGenerator(object):
    """docstring for CloudDataGenerator."""

    __cloudnames = ['aws','azure']
    __osnames = [{'name':'AmazonLinux','version':'2016'},
                {'name':'CentOS','version':'7'},
                {'name':'Ubuntu','version':'14'},
                {'name':'Ubuntu','version':'16'},
                {'name':'Winodws','version':'2012 R2'},
                {'name':'Winodws','version':'2016'}]
    __machine_versions = ['1.0.0','1.0.2','1.0.3','1.0.4']
    __status = ['pass','fail','pending']
    __testnames = ['CP','Qualys','System']
    __machine_attributes = [
                            {'owner': '23456'},
                            {'arch':'x86_64'},
                            {'type':'machine'}
                            ]
    def __init__(self):
        self.CLOUDS = None
        self.TESTS = None
        self.MACHINEATTRIBUTES = None
        self.OSSUPPORTS = None
        self.MACHINES = None
        self.MACHINEDETAILS = None
        self.MACHINETESTRESULTS = None

    def generate_clouds(self):
        if self.CLOUDS:
            return self.CLOUDS
        if self.CLOUDS == None:
            self.CLOUDS = []
        for n in self.__cloudnames:
            c = Cloud(n)
            self.CLOUDS.append(c)
        return self.CLOUDS
    def generate_tests(self):
        if self.TESTS:
            return self.TESTS
        if self.TESTS == None:
            self.TESTS = []
        for n in self.__testnames:
            t = Test(n)
            self.TESTS.append(t)
        return self.TESTS
    def generate_machineattributes(self):
        if self.MACHINEATTRIBUTES:
            return self.MACHINEATTRIBUTES
        if self.MACHINEATTRIBUTES == None:
            self.MACHINEATTRIBUTES = []
        for n in self.__machine_attributes:
            name = n.keys()[0]
            a = MachineAttribute(name)
            self.MACHINEATTRIBUTES.append(a)
        return self.MACHINEATTRIBUTES
    def generate_ossupports(self):
        if self.OSSUPPORTS:
            return self.OSSUPPORTS
        if self.OSSUPPORTS == None:
            self.OSSUPPORTS = []
        for n in self.__osnames:
            cloud = self.get_random_cloud()
            c = OSSupport(n['name'],n['version'],cloud)
            self.OSSUPPORTS.append(c)
        return self.OSSUPPORTS
    def generate_machines(self):
        if self.MACHINES:
            return self.MACHINES
        if self.MACHINES == None:
            self.MACHINES = []
        for i in range(0,10):
            version = self.get_random_machine_version()
            osdetail = self.get_random_osdetail()
            name = osdetail['name'] + '_' + osdetail['version'] + '_' + version
            alreadyexists = False
            if self.MACHINES:
                for m in self.MACHINES:
                    if name == m.name:
                        alreadyexists = True
                        break
            if alreadyexists:
                continue
            ossupport = self.get_random_ossupport()
            released_date = datetime.datetime(random.randint(1990, 2015), random.randint(1, 12), random.randint(1, 28))
            status = self.get_random_status()
            c = Machine(name, version, status, released_date, ossupport)
            self.MACHINES.append(c)
        return self.MACHINES
    def generate_machinedetails(self):
        if self.MACHINEDETAILS:
            return self.MACHINEDETAILS
        if self.MACHINEDETAILS == None:
            self.MACHINEDETAILS = []
        if self.MACHINES == None or len(self.MACHINES) == 0:
            self.generate_machines()
        if self.MACHINEATTRIBUTES == None or len(self.MACHINEATTRIBUTES) == 0:
            self.generate_machineattributes()
        for m in self.MACHINES:
            for n in self.__machine_attributes:
                attributename = n.keys()[0]
                attributevalue = n[attributename]
                attribute = None
                for attr in self.MACHINEATTRIBUTES:
                    if attributename == attr.name:
                        attribute = attr
                        break
                c = MachineDetails(attributevalue, attribute, m)
                self.MACHINEDETAILS.append(c)
        return self.MACHINEDETAILS
    def generate_machinetestresults(self):
        if self.MACHINETESTRESULTS:
            return self.MACHINETESTRESULTS
        if self.MACHINETESTRESULTS == None:
            self.MACHINETESTRESULTS = []
        if self.MACHINES == None or len(self.MACHINES) == 0:
            self.generate_machines()
        if self.MACHINEATTRIBUTES == None or len(self.MACHINEATTRIBUTES) == 0:
            self.generate_machineattributes()
        if self.TESTS == None or len(self.TESTS) == 0:
            self.generate_tests()
        for m in self.MACHINES:
            for t in self.TESTS:
                status = self.get_random_status()
                c = MachineTestResults(t, status, m)
                self.MACHINETESTRESULTS.append(c)
        return self.MACHINETESTRESULTS
    def get_random_cloud(self):
        if self.CLOUDS:
            ln_length = len(self.CLOUDS)
        else:
            ln_length = len(self.generate_clouds())
        return self.CLOUDS[random.randint(0, ln_length - 1)]
    def get_random_ossupport(self):
        if self.OSSUPPORTS:
            ln_length = len(self.OSSUPPORTS)
        else:
            ln_length = len(self.generate_ossupports())
        return self.OSSUPPORTS[random.randint(0, ln_length - 1)]
    def get_random_machine_version(self):
        ln_length = len(self.__machine_versions)
        return self.__machine_versions[random.randint(0, ln_length - 1)]
    def get_random_osdetail(self):
        ln_length = len(self.__osnames)
        return self.__osnames[random.randint(0, ln_length - 1)]
    def get_random_status(self):
        ln_length = len(self.__status)
        return self.__status[random.randint(0, ln_length - 1)]

if __name__ == "__main__":
    c = CloudDataGenerator()
    print 'generate_machinedetails: ' + str(c.generate_machinedetails())
    print 'generate_machinetestresults: ' + str(c.generate_machinetestresults())
