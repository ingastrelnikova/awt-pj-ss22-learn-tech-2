
from xml.etree import ElementTree as ET
import db_helper as db

def import_course(): #possibly get the document as a parameter
    tree = ET.parse('data/course-description/FOKUS_AWT_CompetencyExtraction_WB_Brandenburg.xml')
    courses = tree.findall('.//COURSE')

    #print(len(courses))
    '''
    for course in courses:
        #print('Hi')
        name = course.find('CS_NAME') 
        id = course.find('CS_ID') 
        description = course.find('CS_DESC_LONG') 
        root = ET.Element("COURSE")
        root.append(name)
        root.append(id)
        root.append(description)
        tree_new = ET.ElementTree(root)
        db.add_to_db(name.text, id.text, description.text)
    '''
    name = courses[0].find('CS_NAME') 
    id = courses[0].find('CS_ID') 
    description = courses[0].find('CS_DESC_LONG') 
    
    #create a new XML file
    root = ET.Element("COURSE")
    root.append(name)
    root.append(id)
    root.append(description)
    tree_new = ET.ElementTree(root)
    db.add_to_db(name.text, id.text, description.text)

    string = ET.tostring(root, encoding='unicode')
    #print(name.text)

    #tree_new.write('course.xml')

    #return name.text, id.text, description.text

#name, id, description = import_course()
#db.add_to_db(name, id, description)



import_course()
    

