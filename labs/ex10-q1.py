# Write a Python programme that asks for 2 people's names from the command line, then returns a movie's title, 
# release date, and the first 20 characters of the tagline of any movies they are both related to.

from neo4j import GraphDatabase

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    # note here that we don't define the database to connect to, it just uses whatever is currently active on the browser
    driver = GraphDatabase.driver(uri,auth=("neo4j", "password"), max_connection_lifetime=1000)

def get_associations(tx, p1, p2):
    # you can replace query parameters with placeholders to be populated by variables passed to the function
    query = "MATCH(tom:Person{name:$person1})-->(m:Movie)<--(ron:Person{name:$person2}) RETURN m.released, m.tagline, m.title"
    results = tx.run(query, person1=p1, person2=p2)
    # store the results in an array, see https://neo4j.com/docs/api/python-driver/current/api.html#managed-transactions-transaction-functions
    associations = []
    for result in results:
        associations.append(
            {"title":result["m.title"],
             "released":result["m.released"],
             # restricted number of characters returned
             "tagline":result["m.tagline"][0:19]})
    return associations

def main():
    connect()
    p1 = input("enter first person: ")
    p2 = input("enter second person: ")
    with driver.session() as session:
        values = session.read_transaction(get_associations, p1, p2)
        for i in values:
            print(i["title"], "---", i["released"], "---", i["tagline"])


if __name__ == "__main__":
    main()
