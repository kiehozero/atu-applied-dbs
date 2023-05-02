# Write a Python programme that reads a module name from the command line and prints out the name of each student studing that module in database demo10DB

from neo4j import GraphDatabase

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    # note here that we don't define the database to connect to, it just uses whatever is currently active on the browser
    driver = GraphDatabase.driver(uri,auth=("neo4j", "#"), max_connection_lifetime=1000)

# tx is a pre-built object inside the neo4j driver for handling transactions: https://neo4j.com/docs/api/python-driver/current/api.html#neo4j.ManagedTransaction
def get_students_by_module(tx, user_module):
    # the $module creates a placeholder to be filled by another variable that is passed to a function with the query, in this cases the tx.run()
    query = 'MATCH(m:Module{name:$module})<-[:STUDIES]-(s) RETURN s.name'
    names = []
    results = tx.run(query, module=user_module)
    for i in results:
        names.append(i['s.name'])
    return names

def main():
    connect()
    user_module = input('Enter module: ')
    with driver.session() as session:
        # the result of get_students_by_module is returned to this variable, because the run() function passes back to read_transaction
        values = session.read_transaction(get_students_by_module, user_module)
        if len(values) == 0:
            print('No students studying module')
        else:
            print('Students studying module')
            print('------')
            for j in values:
                print(j)

if __name__ == "__main__":
    main()
