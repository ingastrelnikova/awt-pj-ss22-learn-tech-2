from flask import Flask, request
import course_import as ci


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def function():
    return 'This is my first API call!'

@app.route('/course', methods=["POST"])
def import_course_descriptions():
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


if __name__ == "__main__":
    app.run()