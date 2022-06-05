from xml.etree import ElementTree as ET
import csv

def import_course(xml_data): #possibly get the document as a parameter
    tree = ET.ElementTree(ET.fromstring(xml_data))
    #tree = ET.parse('data/course-description/2022-05-10_FOKUS_AWT_CompetencyExtraction_WB_Brandenburg_re-encoded.xml')
    courses = tree.findall('.//COURSE')


    header = ['course_name', 'course_id', 'couse_description']
    data_list=[]
    
    for course in courses:
        name = course.find('CS_NAME').text
        id = course.find('CS_ID').text
        description = course.find('CS_DESC_LONG').text
        #root = ET.Element("COURSE")
        #root.append(name)
        #root.append(id)
        #root.append(description)
        #tree_new = ET.ElementTree(root)
        #db.add_to_db(name.text, id.text, description.text)
        data = [name, id, description]
        data_list.append(data)
    
    #name = courses[0].find('CS_NAME').text
    #id = courses[0].find('CS_ID').text
    description = courses[0].find('CS_DESC_LONG').text

    
    

    with open('all_courses.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(data_list)


    '''
    
    #create a new XML file
    root = ET.Element("COURSE")
    root.append(name)
    root.append(id)
    root.append(description)
    tree_new = ET.ElementTree(root)
    db.add_to_db(name.text, id.text, description.text)

    string = ET.tostring(root, encoding='unicode')
    #print(name.text)

    #tree_new.write('course.xml')'''

    #return name.text, id.text, description.text

#name, id, description = import_course()
#db.add_to_db(name, id, description)




    

