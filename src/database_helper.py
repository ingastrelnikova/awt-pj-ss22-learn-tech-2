from neo4j import GraphDatabase
import pandas as pd

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()
        
    def create_skill(self, concept_uri, preferred_label, description):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(self._create_and_return_skill, 
                                               concept_uri, preferred_label, description)
            
    @staticmethod
    def _create_and_return_skill(tx, concept_uri, preferred_label, description):
        query = (
            "CREATE (skill:Skill {concept_uri: $concept_uri, \
            preferred_label: $preferred_label, description: $description})"
            "RETURN skill"
        )

        results = tx.run(query, concept_uri=concept_uri, 
                             preferred_label=preferred_label, 
                             description=description)
    
    def create_skills(self, csv_path):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_skills, csv_path)
            
    @staticmethod
    def _create_skills(tx, csv_path):
        assert "http" in csv_path, "Loading csv files from local is \
        not possible due to security reasons, please use online files." 
        query = (
            "LOAD CSV WITH HEADERS FROM $csv_path AS skill \
            CREATE (:Skill {concept_uri: skill.concept_uri, \
            preferred_label: skill.preferred_label, description: skill.description})"
        )
        results = tx.run(query, csv_path=csv_path)
        
    def create_course(self, course_name, course_id, course_description):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(self._create_and_return_course, 
                                               course_name, course_id, course_description)
            
    @staticmethod
    def _create_and_return_course(tx, course_name, course_id, course_description):
        
        query = (
            "CREATE (course:Course {course_id: $course_id, course_name: \
            $course_name, course_description: $course_description})"
            "RETURN course"
        )

        results = tx.run(query, course_id=course_id, 
                             course_name=course_name, 
                             course_description=course_description)
        
    def create_courses(self, csv_path):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_courses, csv_path)
            
    @staticmethod
    def _create_courses(tx, csv_path):
        assert "http" in csv_path, "Loading csv files from local is \
        not possible due to security reasons, please use online files." 
        query = (
            "LOAD CSV WITH HEADERS FROM $csv_path AS course \
            CREATE (:Course {course_id: course.course_id, \
            course_name: course.course_name, course_description: course.course_description})"
        )
        results = tx.run(query, csv_path=csv_path)
    
    def create_relation(self, course_id, concept_uri):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_relation, course_id, concept_uri)
    
    @staticmethod
    def _create_relation(tx, course_id, concept_uri):
        query = (
            "MATCH (course:Course), (skill:Skill) \
            WHERE course.course_id = $course_id AND skill.concept_uri = $concept_uri \
            CREATE (course)-[provide_skill:PROVIDE_SKILL]->(skill) \
            RETURN type(provide_skill)"
        )
        results = tx.run(query, course_id=course_id, concept_uri=concept_uri)
        
    def create_relations(self, csv_path):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_relations, csv_path)
    
    @staticmethod
    def _create_relations(tx, csv_path):
        query = (
            "LOAD CSV WITH HEADERS FROM $csv_path AS relation \
            MERGE (course:Course {course_id: relation.course_id}) \
            MERGE (skill:Skill {concept_uri: relation.concept_uri}) \
            MERGE (course)-[:PROVIDE_SKILL]->(skill)"
        )
        results = tx.run(query, csv_path=csv_path)
        
    def read_skills(self, csv_path):
        with self.driver.session() as session:
            result = session.write_transaction(self._read_skills, csv_path)
            print(result)
            res = []
            for i in result:
                d = {}
                d['preferred_label'] = i['preferred_label']
                d['description']=i['description']
                res.append(d)
            return res
    
    @staticmethod
    def _read_skills(tx, course_id):
        query = (
            "MATCH provided_skills = \
            (course:Course{course_id: $ course_id})-[provide_skill:PROVIDE_SKILL]->(skill) \
            RETURN skill" #provided_skills"
        )
        results = tx.run(query, course_id=course_id) 
        return [row.data()['skill'] for row in results]

    def get_related_courses(self, skill):
        with self.driver.session() as session:
            result = session.write_transaction(self._get_related_courses, skill)
            res = []
            for i in result:
                d = {}
                d['course_name'] = i['course_name']
                d['course_description'] = i['course_description']
                res.append(d)
            return res

    @staticmethod
    def _get_related_courses(tx, preferred_label):
        query = (
            "MATCH (s:Skill{preferred_label: $ preferred_label}) MATCH (s)-[]-(course) RETURN course"
        )
        results = tx.run(query, preferred_label=preferred_label)
        return [row.data()['course'] for row in results]
