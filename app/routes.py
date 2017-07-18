from flask import jsonify
from flask import render_template

from middleware import candidate_by_id
from middleware import candidate
from middleware import add_candidate
from middleware import candidate_update_name
from middleware import random_candidates
from middleware import delete_candidate
from middleware import random_projects
from middleware import add_project

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


def init_api_routes(app):
    if app:
        # app.add_url_rule('/api/candidate/<string:id>', 'candidate_by_id', candidate_by_id, methods=['GET'])
        # app.add_url_rule('/api/candidate', 'candidate', candidate, methods=['GET'])
        # app.add_url_rule('/api/candidate', 'add_candidate', add_candidate, methods=['POST'])
        # app.add_url_rule('/api/candidate/<string:id>/name/<string:new_name>', 'candidate_update_name',
        #                  candidate_update_name, methods=['PUT'])
        # app.add_url_rule('/api/candidate/random', 'get_one_random_candidate', random_candidates,
        #                  methods=['GET'], defaults={'nr_of_items': 1})
        # app.add_url_rule('/api/candidate/random/<int:nr_of_items>', 'get_random_candidates', random_candidates,
        #                  methods=['GET'])
        # app.add_url_rule('/api/candidate/delete/<string:id>', 'delete_candidate', delete_candidate, methods=['DELETE'])
        # app.add_url_rule('/api/project/random/<int:nr_of_items>', 'get_random_projects', random_projects,
        #                  methods=['GET'])
        # app.add_url_rule('/api/project', 'add_project', add_project, methods=['POST'])
        app.add_url_rule('/api/cloud', 'cloud', cloud, methods=['GET'])
        app.add_url_rule('/api/cloud/<string:id>', 'cloud_by_id', cloud_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/cloud/<string:id>/ossupport', 'ossupports_by_cloudid',
                        ossupports_by_cloudid, methods=['GET'])
        app.add_url_rule('/api/cloud/<string:id>/machine', 'machines_by_cloudid',
                        machines_by_cloudid, methods=['GET'])
        app.add_url_rule('/api/cloud','add_cloud',add_cloud,methods=['POST'])

        app.add_url_rule('/api/ossupport', 'ossupport', ossupport, methods=['GET'])
        app.add_url_rule('/api/ossupport/<string:id>', 'ossupport_by_id', ossupport_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/ossupport','add_ossupport',add_ossupport,methods=['POST'])

        app.add_url_rule('/api/test', 'test', test, methods=['GET'])
        app.add_url_rule('/api/test/<string:id>', 'test_by_id', test_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/test','add_test',add_test,methods=['POST'])

        app.add_url_rule('/api/machine', 'machine', machine, methods=['GET'])
        app.add_url_rule('/api/machine/<string:id>', 'machine_by_id', machine_by_id,
                          methods=['GET'])
        app.add_url_rule('/api/machine/<string:id>/machinetestresult',
                        'machinetestresults_by_machineid', machinetestresults_by_machineid,
                        methods=['GET'])
        app.add_url_rule('/api/machine/<string:id>/machinedetail',
                        'machinedetails_by_machineid', machinedetails_by_machineid,
                        methods=['GET'])
        app.add_url_rule('/api/machine','add_machine',add_machine,methods=['POST'])

        app.add_url_rule('/api/machineattribute', 'machineattribute', machineattribute,
                        methods=['GET'])
        app.add_url_rule('/api/machineattribute/<string:id>', 'machineattribute_by_id',
                        machineattribute_by_id,methods=['GET'])
        app.add_url_rule('/api/machineattribute','add_machineattribute',
                        add_machineattribute,methods=['POST'])

        app.add_url_rule('/api/machinedetail', 'machinedetail', machinedetail,
                        methods=['GET'])
        app.add_url_rule('/api/machinedetail/<string:id>', 'machinedetail_by_id',
                        machinedetail_by_id,methods=['GET'])
        app.add_url_rule('/api/machinedetail','add_machinedetail',
                        add_machinedetail,methods=['POST'])

        app.add_url_rule('/api/machinetestresult', 'machinetestresult', machinetestresult,
                        methods=['GET'])
        app.add_url_rule('/api/machinetestresult/<string:id>', 'machinetestresult_by_id',
                        machinetestresult_by_id,methods=['GET'])
        app.add_url_rule('/api/machinetestresult','add_machinetestresult',
                        add_machinetestresult,methods=['POST'])
        app.add_url_rule('/api/machinetestresult/<string:id>/status/<string:new_status>',
                        'machinetestresult_update_status', machinetestresult_update_status,
                        methods=['PUT'])
        app.add_url_rule('/api/machinetestresult/delete/<string:id>',
                        'delete_machinetestresult', delete_machinetestresult, methods=['DELETE'])

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
