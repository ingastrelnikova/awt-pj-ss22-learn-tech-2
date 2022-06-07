from py2neo import Graph


uri = "neo4j+s://9559b7fa.databases.neo4j.io"
#user = "neo4j"
#password = "aO3E8ZZ5I_M082cqqGpskvuoVsGGzFv9YPnR1H9FfFs"

query = ("USING PERIODIC COMMIT "
        'LOAD CSV FROM "https://drive.google.com/uc?export=download&id=14dCwOno88T01HjsRo_E82vY3deB0AKja" AS line '
        "CREATE (:Course {name: line[0], id: line[1], description: line[2]})"
)


graph = Graph(uri, auth = ("neo4j","aO3E8ZZ5I_M082cqqGpskvuoVsGGzFv9YPnR1H9FfFs"))

graph.run(query)