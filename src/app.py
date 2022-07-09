from flask import Flask, request,jsonify, make_response
from flask_restx import Api, Resource, fields
import course_import as ci
import database_helper
from neo4j import GraphDatabase


app = Flask(__name__)
#app.config["DEBUG"] = True

api = Api(app, version='1.0', title='Competency extranction from courses',
    description='A service for finding courses by the competencies they cover as well as find what competencies are covered by a particular course.',
)

ns = api.namespace('Filtering options', 
                   description='Available filtering options for the user.')

uri = "neo4j+s://fbb398e7.databases.neo4j.io"
password = "3bO4Zwc9eYOyZBQ_CHE49lqd7NKeLSySJAq4flxUtAA"
user = "neo4j"  

app1 = database_helper.App(uri, user, password)


'''@api.route('/skills/<skill>')
@api.doc(params={'skill': 'Skill name'})
class Skill(Resource):

    def get(self,skill):
        result = app1.get_related_courses(skill)
        app1.close()
        
        if result !=[]:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found'}, 200)'''


'''@api.route('/skills')
@api.doc()
class Skills(Resource):
    def post(self):
        app1.create_skills("https://raw.githubusercontent.com/ingastrelnikova/awt-pj-ss22-learn-tech-2/main/data/all_skills.csv")
        app1.close()
        return make_response({"msg":'Skills imported successfully'},200)'''

@ns.route('/course/<course_id>')
@ns.doc(params={'course_id': 'Course id'})
class Skills(Resource):

    def get(self,course_id):
        result = app1.find_skills(course_id)
        app1.close()
        
        if len(result[0])>0:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found'}, 200)


@ns.route('/courses/<path:uri>')
@ns.doc(params={'uri': 'Competency URI'})
class Courses(Resource):

    '''def post(self,link):
        app1.create_courses(link)

        return make_response({"msg":'Courses imported'},200)

        #app1.create_relation'''
    
    def get(self,uri):
        result = app1.find_courses(uri)
        app1.close()
        
        if len(result[0])>0:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found'}, 200)


@ns.route('/courses_label/<label>')
@ns.doc(params={'label': 'Competency label'})
class Courses_by_label(Resource):

    
    def get(self,label):
        result = app1.find_courses_by_label(label)
        app1.close()
        
        if len(result[0])>0:
            return make_response(jsonify(result), 200)
        else:
            return make_response({"msg":'Nothing found for the entered competency'}, 200)

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
        