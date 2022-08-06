from xml.etree import ElementTree as ET
import csv
from os import path

def import_course():
    tree = ET.parse('../data/2022-05-10_FOKUS_AWT_CompetencyExtraction_WB_Brandenburg_re-encoded.xml')
    courses = tree.findall('.//COURSE')

    # Column names for the CSV file
    header = ['course_name', 'course_id', 'couse_description']
    data_list=[]
    
    for course in courses:
        name = course.find('CS_NAME').text
        id = course.find('CS_ID').text
        description = course.find('CS_DESC_LONG').text
        data = [name, id, description]
        data_list.append(data)

    
    file_path = path.relpath("../data/all_courses.csv")
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(data_list)

if __name__ == "__main__":
    import_course()




    

