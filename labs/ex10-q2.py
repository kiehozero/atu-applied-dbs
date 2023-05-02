# Write a Python programme that allows a user to enter a movie's title, release year and tagline to the database.
# If a movie with that title already exists, the user should be informed, otherwise state that the movie has been successfully added.

from neo4j import GraphDatabase
from neo4j import exceptions

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    # note here that we don't define the database to connect to, it just uses whatever is currently active on the browser
    driver = GraphDatabase.driver(uri,auth=("neo4j", "password"), max_connection_lifetime=1000)

def add_movie(tx, title, released, tagline):
    query = 'CREATE(:Movie{title:$x, released:$y, tagline:$z})'
    tx.run(query, x=title, y=released, z=tagline)

def main():
    connect()
    title = input('Enter movie name: ')
    released = input('Enter release year: ')
    tagline = input('Enter the tagline: ')
    with driver.session() as session:
        try:
            # the result of add_student is returned to this variable, because the run() function passes back to read_transaction
            session.write_transaction(add_movie, title, released, tagline)
            print(title, " added to database.")
        except exceptions.ConstraintError as e:
            print("\nError: ", e.message)

if __name__ == "__main__":
    main()
