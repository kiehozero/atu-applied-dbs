# Write a Python programme that reads a student SID and name from the command line. A new student node should then be created with those values in demo10DB

from neo4j import GraphDatabase
from neo4j import exceptions

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    # note here that we don't define the database to connect to, it just uses whatever is currently active on the browser
    driver = GraphDatabase.driver(uri,auth=("neo4j", "password"), max_connection_lifetime=1000)

def add_student(tx, sid, name):
    query = 'CREATE(:Student{sid:$x, name:$y})'
    tx.run(query, x=sid, y=name)

def main():
    connect()
    sid = input('Enter student ID: ')
    name = input('Enter student name: ')
    with driver.session() as session:
        try:
            # the result of add_student is returned to this variable, because the run() function passes back to read_transaction
            session.write_transaction(add_student, sid, name)
            print("\nStudent: ", sid, ", ", name, " added to database.")
        except exceptions.ConstraintError as e:
            print("\nError: ", e.message)

if __name__ == "__main__":
    main()
