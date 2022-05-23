from flask import Flask, request
import xmltodict
from xml.etree import ElementTree as ET
import db_helper as db


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def function():
    return 'This is my first API call!'

@app.route('/course', methods=["POST"])
def import_course_descriptions():
    xml_data = request.get_data().decode('utf-8')
    
    #name, id, description = import_course(xml_data)
    #db.add_to_db(name, id, description)
    return ''
    
'''

def import_course(xml): #possibly get the document as a parameter
    #tree = ET.parse(xml)#'data/course-description/FOKUS_AWT_CompetencyExtraction_WB_Brandenburg.xml')
    tree = ET.fromstring(xml)
    courses = tree.findall('.//COURSE')

    #for course in courses: 
    name = courses[0].find('CS_NAME') 
    id = courses[0].find('CS_ID') 
    description = courses[0].find('CS_DESC_LONG') 
    
    #create a new XML file
    root = ET.Element("COURSE")
    root.append(name)
    root.append(id)
    root.append(description)
    tree_new = ET.ElementTree(root)

    string = ET.tostring(root, encoding='unicode')
    #print(name.text)

    #tree_new.write('course.xml')

    return name.text, id.text, description.text

#= import_course()


'''
if __name__ == "__main__":
    app.run()