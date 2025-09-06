#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state using the database hbtn_0e_4_usa. Safe from SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a single SQL query with parameter substitution (safe)
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    # Fetch and print results
    cities = cursor.fetchall()

    # Extract just the city names into a list
    city_names = [city[0] for city in cities]

    # Print them as a single line, comma-separated
    print(", ".join(city_names))

    # Clean up
    cursor.close()
    db.close()
