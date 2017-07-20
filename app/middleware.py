from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

db_engine = 'postgresql://postgres:tester@localhost:5432/flask-second'

DATA_PROVIDER = DataProviderService(db_engine)

def initialize_database():
    DATA_PROVIDER.init_database()

# Cloud functions
def cloud(serialize = True):
    clouds = DATA_PROVIDER.get_cloud(serialize=serialize)
    if serialize:
        if clouds == None:
            return jsonify({"clouds": clouds, "total": 0})
        else:
            return jsonify({"clouds": clouds, "total": len(clouds)})
    else:
        return clouds

def cloud_by_id(id):
    current_cloud = DATA_PROVIDER.get_cloud(id=id, serialize=True)
    if current_cloud:
        return jsonify({"cloud": current_cloud})
    else:
        #
        # In case we did not find the cloud by id
        # we send HTTP 404 - Not Found error to the cloud
        #
        abort(404)
def cloud_by_name(name):
    current_cloud = DATA_PROVIDER.get_cloud(name=name, serialize=True)
    if current_cloud:
        return jsonify({"cloud": current_cloud})
    else:
        abort(404)
def add_cloud():
    name = request.form["name"]
    new_cloud_id = DATA_PROVIDER.add_cloud(name=name)
    return jsonify({
        "id": new_cloud_id,
        "url": url_for("cloud_by_id", id=new_cloud_id)
    })
def ossupports_by_cloudid(id):
    ossupports = DATA_PROVIDER.get_ossupport(cloud_id=id,serialize=True)
    if ossupports:
        if len(ossupports) == 0:
            return jsonify({"ossupports": ossupports, "total": 0})
        else:
            return jsonify({"ossupports": ossupports,
                    "total": len(ossupports)})
    else:
        abort(404)
def machines_by_cloudid(id):
    machines = DATA_PROVIDER.get_machine(cloud_id=id,serialize=True)
    if machines:
        if len(machines) == 0:
            return jsonify({"machines": machines, "total": 0})
        else:
            return jsonify({"machines":  machines,
                    "total": len(machines)})
    else:
        abort(404)
# ossupport functions
def ossupport(serialize = True):
    ossupports = DATA_PROVIDER.get_ossupport(serialize=serialize)
    if serialize:
        if ossupports == None:
            return jsonify({"ossupports": ossupports, "total": 0})
        else:
            return jsonify({"ossupports": ossupports, "total": len(ossupports)})
    else:
        return ossupports

def ossupport_by_id(id):
    current_ossupport = DATA_PROVIDER.get_ossupport(id=id, serialize=True)
    if current_ossupport:
        return jsonify({"ossupport": current_ossupport})
    else:
        abort(404)
def ossupport_by_name(name):
    current_ossupport = DATA_PROVIDER.get_ossupport(name=name, serialize=True)
    if current_cloud:
        return jsonify({"ossupport": current_ossupport })
    else:
        abort(404)
def add_ossupport():
    name = request.form["name"]
    version = request.form["version"]
    cloud_id = request.form["cloud_id"]

    new_ossupport_id = DATA_PROVIDER.add_ossupport(name,version,cloud_id)
    return jsonify({
        "id": new_ossupport_id,
        "url": url_for("ossupport_by_id", id=new_ossupport_id)
    })
# test functions
def test(serialize = True):
    tests = DATA_PROVIDER.get_test(serialize=serialize)
    if serialize:
        if tests == None:
            return jsonify({"tests": tests, "total": 0})
        else:
            return jsonify({"tests": tests, "total": len(tests)})
    else:
        return tests

def test_by_id(id):
    current_test = DATA_PROVIDER.get_test(id=id,serialize=True)
    if current_test:
        return jsonify({"test": current_test})
    else:
        abort(404)
def test_by_name(name):
    current_test = DATA_PROVIDER.get_test(name=name,serialize=True)
    if current_test:
        return jsonify({"test": current_test})
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
    machines = DATA_PROVIDER.get_machine(serialize=serialize)
    if serialize:
        if machines == None:
            return jsonify({"machines": machines, "total": 0})
        else:
            return jsonify({"machines": machines, "total": len(machines)})
    else:
        return machines

def machine_by_id(id):
    current_machine = DATA_PROVIDER.get_machine(id=id,serialize=True)
    if current_machine:
        return jsonify({"machine": current_machine})
    else:
        abort(404)
def machine_by_name(name):
    current_machine = DATA_PROVIDER.get_machine(name=name,serialize=True)
    if current_machine:
        return jsonify({"machine": current_machine})
    else:
        abort(404)
def add_machine():
    name = request.form["name"]
    version = request.form["version"]
    status = request.form["status"]
    released_date = request.form["released_date"]
    ossupport_id = request.form["ossupport_id"]

    new_machine_id = DATA_PROVIDER.add_machine(name, version, status,
                                                released_date,ossupport_id)

    return jsonify({
        "id": new_machine_id,
        "url": url_for("machine_by_id", id=new_machine_id)
    })
def machinetestresults_by_machineid(id):
    machineresults = DATA_PROVIDER.get_machinetestresult(machine_id=id)
    if machineresults:
        if len(machineresults) == 0:
            return jsonify({"machineresults": machineresults, "total": 0})
        else:
            return jsonify({"machineresults": [c.serialize() for c in machineresults],
                    "total": len(machineresults)})
    else:
        abort(404)
def machinedetails_by_machineid(id):
    machinedetails = DATA_PROVIDER.get_machinedetail(machine_id=id)
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
    machineattributes = DATA_PROVIDER.get_machineattribute(serialize=serialize)
    if serialize:
        if machineattributes == None:
            return jsonify({"machineattributes": machineattributes, "total": 0})
        else:
            return jsonify({"machineattributes": machineattributes,
                            "total": len(machineattributes)})
    else:
        return machineattributes

def machineattribute_by_id(id):
    current_machineattribute = DATA_PROVIDER.get_machineattribute(id=id,serialize=True)
    if current_machineattribute:
        return jsonify({"machineattribute": current_machineattribute})
    else:
        abort(404)
def machineattribute_by_name(name):
    current_machineattribute = DATA_PROVIDER.get_machineattribute(name=name,serialize=True)
    if current_machineattribute:
        return jsonify({"machineattribute": current_machineattribute})
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
    machinedetails = DATA_PROVIDER.get_machinedetail(serialize=serialize)
    if serialize:
        if machinedetails == None:
            return jsonify({"machinedetails": machinedetails, "total": 0})
        else:
            return jsonify({"machinedetails": machinedetails,
                            "total": len(machinedetails)})
    else:
        return machinedetails

def machinedetail_by_id(id):
    current_machinedetails = DATA_PROVIDER.get_machine_detail(id,serialize=True)
    if current_machinedetails:
        return jsonify({"machinedetails": current_machinedetails})
    else:
        abort(404)

def add_machinedetail():
    machine_id = request.form["machine_id"]
    attribute_id = request.form["attribute_id"]
    value = request.form["value"]
    new_machinedetail_id = DATA_PROVIDER.add_machinedetail(value, attribute_id, machine_id)

    return jsonify({
        "id": new_machinedetail_id,
        "url": url_for("machinedetail_by_id", id=new_machinedetail_id)
    })

#MachineTest functions
def machinetestresult(serialize = True):
    machinetestresults = DATA_PROVIDER.get_machinetestresult(serialize=serialize)
    if serialize:
        if machinetestresults == None:
            return jsonify({"machinetestresults": machinetestresults, "total": 0})
        else:
            return jsonify({"machinetestresults": machinetestresults,
                            "total": len(machinetestresults)})
    else:
        return machinedetails

def machinetestresult_by_id(id):
    current_machinetestresult = DATA_PROVIDER.get_machinetestresult(id,serialize=True)
    if current_machinetestresult:
        return jsonify({"current_machinetestresult": current_machinetestresult})
    else:
        abort(404)

def add_machinetestresult():
    test_id = request.form["test_id"]
    machine_id = request.form["machine_id"]
    status = request.form["status"]
    new_machinetestresult_id = DATA_PROVIDER.add_machinetestresult(status,machine_id,test_id)

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
def build_message(key, message):
    return {key:message}
