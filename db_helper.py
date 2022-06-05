import logging

from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_course(self):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._create_course)
            for record in result:
                print("Created")
                      #.format(p1=record['p1'], p2=record['p2']))

    
    @staticmethod
    def _create_course(tx):
        # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
        # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
        #query = (
        #    "CREATE (n:Course {CS_NAME: $name, CS_ID: $id ,CS_DESC_LONG: $description })"
        
        #)

        query = (
            "LOAD CSV FROM 'file:///c.csv' AS line"
            "CREATE (:Course {name: line[0], id: line[1], description: line[2]})"
        )
        #result = tx.run(query, name=name, id = id, description = description)
        result = tx.run(query)
        try:
            return [{"c": record["c"]["name"]}
                    for record in result]
        # Capture any errors along with the query and data for traceability
        except Neo4jError as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
    






def add_to_db():
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://9559b7fa.databases.neo4j.io"
    user = "neo4j"
    password = "aO3E8ZZ5I_M082cqqGpskvuoVsGGzFv9YPnR1H9FfFs"

    app = App(uri, user, password)
    #app.create_friendship("Alice", "David")
    #app.find_person("Alice")
    #app.create_course(cs_name, cs_id, cs_desc)
    app.create_course()

    app.close()



add_to_db()