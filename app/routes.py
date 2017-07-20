from flask import jsonify
from flask import render_template

from middleware import cloud
from middleware import add_cloud
from middleware import cloud_by_id
from middleware import ossupports_by_cloudid
from middleware import machines_by_cloudid
from middleware import ossupport
from middleware import add_ossupport
from middleware import ossupport_by_id
from middleware import test
from middleware import add_test
from middleware import test_by_id
from middleware import machine
from middleware import add_machine
from middleware import machine_by_id
from middleware import machinetestresults_by_machineid
from middleware import machinedetails_by_machineid
from middleware import machineattribute
from middleware import add_machineattribute
from middleware import machineattribute_by_id
from middleware import machinedetail
from middleware import add_machinedetail
from middleware import machinedetail_by_id
from middleware import machinetestresult
from middleware import add_machinetestresult
from middleware import machinetestresult_by_id
from middleware import machinetestresult_update_status
from middleware import delete_machinetestresult

from middleware import initialize_database as init_db
from middleware import build_message


def init_api_routes(app):
    if app:
        app.add_url_rule('/api/clouds', 'cloud', cloud, methods=['GET'])
        app.add_url_rule('/api/clouds/<string:id>', 'cloud_by_id', cloud_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/clouds/<string:id>/ossupports', 'ossupports_by_cloudid',
                        ossupports_by_cloudid, methods=['GET'])
        app.add_url_rule('/api/clouds/<string:id>/machines', 'machines_by_cloudid',
                        machines_by_cloudid, methods=['GET'])
        app.add_url_rule('/api/clouds','add_cloud',add_cloud,methods=['POST'])

        app.add_url_rule('/api/ossupports', 'ossupport', ossupport, methods=['GET'])
        app.add_url_rule('/api/ossupports/<string:id>', 'ossupport_by_id', ossupport_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/ossupports','add_ossupport',add_ossupport,methods=['POST'])

        app.add_url_rule('/api/tests', 'test', test, methods=['GET'])
        app.add_url_rule('/api/tests/<string:id>', 'test_by_id', test_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/tests','add_test',add_test,methods=['POST'])

        app.add_url_rule('/api/machines', 'machine', machine, methods=['GET'])
        app.add_url_rule('/api/machines/<string:id>', 'machine_by_id', machine_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/machines/<string:id>/machinetestresults',
                        'machinetestresults_by_machineid', machinetestresults_by_machineid,
                        methods=['GET'])
        app.add_url_rule('/api/machines/<string:id>/machinedetails',
                        'machinedetails_by_machineid', machinedetails_by_machineid,
                        methods=['GET'])
        app.add_url_rule('/api/machines','add_machine',add_machine,methods=['POST'])

        app.add_url_rule('/api/machineattributes', 'machineattribute', machineattribute,
                        methods=['GET'])
        app.add_url_rule('/api/machineattributes/<string:id>', 'machineattribute_by_id',
                        machineattribute_by_id,methods=['GET'])
        app.add_url_rule('/api/machineattributes','add_machineattribute',
                        add_machineattribute,methods=['POST'])

        app.add_url_rule('/api/machinedetails', 'machinedetail', machinedetail,
                        methods=['GET'])
        app.add_url_rule('/api/machinedetails/<string:id>', 'machinedetail_by_id',
                        machinedetail_by_id,methods=['GET'])
        app.add_url_rule('/api/machinedetails','add_machinedetail',
                        add_machinedetail,methods=['POST'])

        app.add_url_rule('/api/machinetestresults', 'machinetestresult', machinetestresult,
                        methods=['GET'])
        app.add_url_rule('/api/machinetestresults/<string:id>', 'machinetestresult_by_id',
                        machinetestresult_by_id,methods=['GET'])
        app.add_url_rule('/api/machinetestresults','add_machinetestresult',
                        add_machinetestresult,methods=['POST'])
        app.add_url_rule('/api/machinetestresults/<string:id>/status/<string:new_status>',
                        'machinetestresult_update_status', machinetestresult_update_status,
                        methods=['PUT'])
        app.add_url_rule('/api/machinetestresults/delete/<string:id>',
                        'delete_machinetestresult', delete_machinetestresult, methods=['DELETE'])

        app.add_url_rule('/api/initdb', 'initdb', initialize_database)
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'],
                        defaults={'app': app})

def page_about():
    return render_template('about.html', selected_menu_item="about")


def page_project():
    return render_template('project.html', selected_menu_item="project")


def page_experience():
    return render_template('experience.html', selected_menu_item="experience")


def page_candidate():
    current_candidates = candidate(serialize=False)
    return render_template('candidate.html', selected_menu_item="candidate", candidates=current_candidates)


def page_index():
    return render_template('index.html', selected_menu_item="index")


def init_website_routes(app):
    if app:
        app.add_url_rule('/about', 'page_about', page_about, methods=['GET'])
        app.add_url_rule('/project', 'page_project', page_project, methods=['GET'])
        app.add_url_rule('/candidate', 'page_candidate', page_candidate, methods=['GET'])
        app.add_url_rule('/experience', 'page_experience', page_experience, methods=['GET'])
        app.add_url_rule('/', 'page_index', page_index, methods=['GET'])


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})

def initialize_database():
    message_key = "Initialize Database"
    try:
        init_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))
