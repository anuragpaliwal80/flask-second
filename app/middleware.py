from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

DATA_PROVIDER = DataProviderService(0)

# Cloud functions
def cloud(serialize = True):
    clouds = DATA_PROVIDER.get_clouds()
    if serialize:
        if clouds == None:
            return jsonify({"clouds": clouds, "total": 0})
        else:
            return jsonify({"clouds": [c.serialize() for c in clouds],
                    "total": len(clouds)})
    else:
        return clouds

def cloud_by_id(id):
    current_cloud = DATA_PROVIDER.get_cloud(id)
    if current_cloud:
        return jsonify({"cloud": current_cloud.serialize()})
    else:
        #
        # In case we did not find the cloud by id
        # we send HTTP 404 - Not Found error to the cloud
        #
        abort(404)
def cloud_by_name(name):
    current_cloud = DATA_PROVIDER.get_cloud_by_name(name)
    if current_cloud:
        return jsonify({"cloud": current_cloud.serialize()})
    else:
        abort(404)
def add_cloud():
    name = request.form["name"]
    new_cloud_id = DATA_PROVIDER.add_cloud(name)
    return jsonify({
        "id": new_cloud_id,
        "url": url_for("cloud_by_id", id=new_cloud_id)
    })
def ossupports_by_cloudid(id):
    ossupports = DATA_PROVIDER.ossupports_by_cloudid(id)
    if ossupports:
        if len(ossupports) == 0:
            return jsonify({"ossupports": ossupports, "total": 0})
        else:
            return jsonify({"ossupports": [c.serialize() for c in ossupports],
                    "total": len(ossupports)})
    else:
        abort(404)
def machines_by_cloudid(id):
    machines = DATA_PROVIDER.machines_by_cloudid(id)
    if machines:
        if len(machines) == 0:
            return jsonify({"machines": machines, "total": 0})
        else:
            return jsonify({"machines": [c.serialize() for c in machines],
                    "total": len(machines)})
    else:
        abort(404)
# ossupport functions
def ossupport(serialize = True):
    ossupports = DATA_PROVIDER.get_ossupports()
    if serialize:
        if ossupports == None:
            return jsonify({"ossupports": ossupports, "total": 0})
        else:
            return jsonify({"ossupports": [c.serialize() for c in ossupports],
                    "total": len(ossupports)})
    else:
        return ossupports

def ossupport_by_id(id):
    current_ossupport = DATA_PROVIDER.get_ossupport(id)
    if current_cloud:
        return jsonify({"ossupport": current_ossupport.serialize()})
    else:
        abort(404)
def ossupport_by_name(name):
    current_ossupport = DATA_PROVIDER.get_ossupport_by_name(name)
    if current_cloud:
        return jsonify({"ossupport": current_ossupport.serialize()})
    else:
        abort(404)
def add_ossupport():
    name = request.form["name"]
    version = request.form["version"]
    cloud_name = request.form["cloud_name"]
    c = DATA_PROVIDER.get_cloud_by_name(cloud_name)

    new_ossupport_id = DATA_PROVIDER.add_ossupport(name,version,c)
    return jsonify({
        "id": new_ossupport_id,
        "url": url_for("ossupport_by_id", id=new_ossupport_id)
    })
# test functions
def test(serialize = True):
    tests = DATA_PROVIDER.get_tests()
    if serialize:
        if tests == None:
            return jsonify({"tests": tests, "total": 0})
        else:
            return jsonify({"tests": [t.serialize() for t in tests],
                    "total": len(tests)})
    else:
        return tests

def test_by_id(id):
    current_test = DATA_PROVIDER.get_test(id)
    if current_test:
        return jsonify({"test": current_test.serialize()})
    else:
        abort(404)
def test_by_name(name):
    current_test = DATA_PROVIDER.get_test_by_name(name)
    if current_test:
        return jsonify({"test": current_test.serialize()})
    else:
        abort(404)
def add_test():
    name = request.form["name"]
    new_test_id = DATA_PROVIDER.add_test(name)
    return jsonify({
        "id": new_test_id,
        "url": url_for("test_by_id", id=new_test_id)
    })
#Machine functions
def machine(serialize = True):
    machines = DATA_PROVIDER.get_machines()
    if serialize:
        if machines == None:
            return jsonify({"machines": machines, "total": 0})
        else:
            return jsonify({"machines": [m.serialize() for m in machines],
                            "total": len(machines)})
    else:
        return machines

def machine_by_id(id):
    current_machine = DATA_PROVIDER.get_machine(id)
    if current_machine:
        return jsonify({"machine": current_machine.serialize()})
    else:
        abort(404)
def machine_by_name(name):
    current_machine = DATA_PROVIDER.get_machine_by_name(name)
    if current_machine:
        return jsonify({"machine": current_machine.serialize()})
    else:
        abort(404)
def add_machine():
    name = request.form["name"]
    version = request.form["version"]
    status = request.form["status"]
    released_date = request.form["released_date"]
    new_machine_id = DATA_PROVIDER.add_machine(name, version, status, released_date)

    return jsonify({
        "id": new_machine_id,
        "url": url_for("machine_by_id", id=new_machine_id)
    })
def machinetestresults_by_machineid(id):
    machineresults = DATA_PROVIDER.machinetestresults_by_machineid(id)
    if machineresults:
        if len(machineresults) == 0:
            return jsonify({"machineresults": machineresults, "total": 0})
        else:
            return jsonify({"machineresults": [c.serialize() for c in machineresults],
                    "total": len(machineresults)})
    else:
        abort(404)
def machinedetails_by_machineid(id):
    machinedetails = DATA_PROVIDER.machinedetails_by_machineid(id)
    if machinedetails:
        if len(machinedetails) == 0:
            return jsonify({"machinedetails": machinedetails, "total": 0})
        else:
            return jsonify({"machinedetails": [c.serialize() for c in machinedetails],
                    "total": len(machinedetails)})
    else:
        abort(404)
#MachineAttribute functions
def machineattribute(serialize = True):
    machineattributes = DATA_PROVIDER.get_machineattributes()
    if serialize:
        if machineattributes == None:
            return jsonify({"machineattributes": machineattributes, "total": 0})
        else:
            return jsonify({"machineattributes": [m.serialize() for m in machineattributes],
                            "total": len(machineattributes)})
    else:
        return machineattributes

def machineattribute_by_id(id):
    current_machineattribute = DATA_PROVIDER.get_machineattribute(id)
    if current_machineattribute:
        return jsonify({"machineattribute": current_machineattribute.serialize()})
    else:
        abort(404)
def machineattribute_by_name(name):
    current_machineattribute = DATA_PROVIDER.get_machineattribute_by_name(name)
    if current_machineattribute:
        return jsonify({"machineattribute": current_machineattribute.serialize()})
    else:
        abort(404)
def add_machineattribute():
    name = request.form["name"]
    new_machineattribute_id = DATA_PROVIDER.add_machineattribute(name)

    return jsonify({
        "id": new_machineattribute_id,
        "url": url_for("machineattribute_by_id", id=new_machineattribute_id)
    })

#MachineDetails functions
def machinedetail(serialize = True):
    machinedetails = DATA_PROVIDER.get_machinedetails()
    if serialize:
        if machinedetails == None:
            return jsonify({"machinedetails": machinedetails, "total": 0})
        else:
            return jsonify({"machinedetails": [m.serialize() for m in machinedetails],
                            "total": len(machinedetails)})
    else:
        return machinedetails

def machinedetail_by_id(id):
    current_machinedetails = DATA_PROVIDER.get_machine_detail(id)
    if current_machinedetails:
        return jsonify({"machinedetails": current_machinedetails.serialize()})
    else:
        abort(404)

def add_machinedetail():
    machine = request.form["machine_name"]
    attribute = request.form["attribute_name"]
    value = request.form["value"]
    m = DATA_PROVIDER.get_machine_by_name(machine)
    a = DATA_PROVIDER.get_machine_attribute_by_name(attribute)
    new_machinedetail_id = DATA_PROVIDER.add_machinedetail(value, a, m)

    return jsonify({
        "id": new_machinedetail_id,
        "url": url_for("machinedetail_by_id", id=new_machinedetail_id)
    })

#MachineTest functions
def machinetestresult(serialize = True):
    machinetestresults = DATA_PROVIDER.get_machinetestresults()
    if serialize:
        if machinetestresults == None:
            return jsonify({"machinetestresults": machinetestresults, "total": 0})
        else:
            return jsonify({"machinetestresults": [m.serialize() for m in machinetestresults],
                            "total": len(machinetestresults)})
    else:
        return machinedetails

def machinetestresult_by_id(id):
    current_machinetestresult = DATA_PROVIDER.get_machinetestresult(id)
    if current_machinetestresult:
        return jsonify({"current_machinetestresult": current_machinetestresult.serialize()})
    else:
        abort(404)

def add_machinetestresult():
    test_name = request.form["test_name"]
    machine_name = request.form["machine_name"]
    status = request.form["status"]
    t = DATA_PROVIDER.get_test_by_name(test_name)
    m = DATA_PROVIDER.get_machine_by_name(machine_name)
    new_machinetestresult_id = DATA_PROVIDER.add_machinetestresult(t,status,m)

    return jsonify({
        "id": new_machinetestresult_id,
        "url": url_for("machinetestresult_by_id", id=new_machinetestresult_id)
    })
def machinetestresult_update_status(id, new_status):
    nr_of_updated_items = DATA_PROVIDER.machinetestresult_update_status(id, new_status)
    if nr_of_updated_items == 0:
        abort(404)
    else:
        return jsonify({"total_updated": nr_of_updated_items})
def delete_machinetestresult(id):
    if DATA_PROVIDER.delete_machinetestresult(id):
        return make_response('', 200)
    else:
        return abort(404)
# Other functions
def candidate(serialize = True):
    candidates = DATA_PROVIDER.get_candidates()
    if serialize:
        return jsonify({"candidates": candidates, "total": len(candidates)})
    else:
        return candidates


def candidate_by_id(id):
    current_candidate = DATA_PROVIDER.get_candidate(id)
    if current_candidate:
        return jsonify({"candidate": current_candidate})
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_candidate(id):
    if DATA_PROVIDER.delete_candidate(id):
        return make_response('', 200)
    else:
        return abort(404)


def candidate_update_name(id, new_name):
    nr_of_updated_items = DATA_PROVIDER.update_name(id, new_name)
    if nr_of_updated_items == 0:
        abort(404)
    else:
        return jsonify({"total_updated": nr_of_updated_items})


def random_candidates(nr_of_items):
    candidates = DATA_PROVIDER.get_random_candidates(nr_of_items)
    return jsonify({"candidates": candidates, "total": len(candidates)})


def random_projects(nr_of_items):
    projects = DATA_PROVIDER.get_random_projects(nr_of_items)
    return jsonify({"projects": projects, "total": len(projects)})


def add_project():
    project_name = request.form["name"]
    project_description = request.form["description"]

    new_project_id = DATA_PROVIDER.add_project(project_name, project_description)

    return jsonify({
        "id": new_project_id
    })


def add_candidate():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]

    new_candidate_id = DATA_PROVIDER.add_candidate(first_name, last_name)

    return jsonify({
        "id": new_candidate_id,
        "url": url_for("candidate_by_id", id=new_candidate_id)
    })
