from flask import Flask, request,jsonify, make_response
from flask_restx import Api, Resource, fields
import course_import as ci
import database_helper
from neo4j import GraphDatabase


app = Flask(__name__)
#app.config["DEBUG"] = True

api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

uri = "neo4j+s://3f32e422.databases.neo4j.io"
user = "neo4j"  
password = "Xm3_uLclyVQspJgpSoMKmYONcOIFPZx7WKVrTbiU_ms"
app1 = database_helper.App(uri, user, password)


@api.route('/skills/<skill>')
@api.doc(params={'skill': 'Skill name'})
class Skill(Resource):

    def get(self,skill):
        result = app1.get_related_courses(skill)
        app1.close()
        
        if result !=[]:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found'}, 200)


@api.route('/skills')
@api.doc()
class Skills(Resource):
    def post(self):
        app1.create_skills("https://raw.githubusercontent.com/ingastrelnikova/awt-pj-ss22-learn-tech-2/main/data/all_skills.csv")
        app1.close()
        return make_response({"msg":'Skills imported successfully'},200)

@api.route('/course/<course_id>')
@api.doc(params={'course_id': 'Course id'})
class Skill(Resource):

    def get(self,course_id):
        result = app1.read_skills(course_id)
        app1.close()
        
        if result !=[]:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found'}, 200)


@api.route('/courses/<path:link>')
@api.doc(params={'link': 'Link to courses'})
class Courses(Resource):

    def post(self,link):
        app1.create_courses(link)

        return make_response({"msg":'Courses imported'},200)

        #app1.create_relation

'''
    #@app.route('/course', methods=["POST"])
    def q():
        xml_data = request.get_data().decode('utf-8')
        print(xml_data)
        ci.import_course(xml_data)

        return ''
        

    @app.route('/competency_by_course', methods=["GET"])
    def get_competencies_covered():
        course_id = request.get_data() 

        return ''



    @app.route('/find_courses', methods=["GET"])
    def find_courses_by_competency():
        competency = request.get_data() 

        return ''

'''
if __name__ == "__main__":
    app.run(debug=True)
        
'''




from flask import Flask

from werkzeug.utils import cached_property



app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

@api.route('/my-resource/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)


if __name__ == '__main__':
    app.run(debug=True)'''