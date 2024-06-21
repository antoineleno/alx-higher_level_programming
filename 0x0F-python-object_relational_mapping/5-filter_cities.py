#!/usr/bin/python3
"""
4-city by states modeule
"""
import MySQLdb
import sys


def list_all_states(username, db_password, db_name, statename):
    """list_all_states function

    Args:
        username (string): The username of the database
        db_password (String): Database password
        db_name (String): Database name
        state_name(String): Name of the state to pass as arugment
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         password=db_password,
                         db=db_name)

    cursor = db.cursor()
    my_query = (f'select name from cities where state_id in (select id from states where name="{statename}")')
    cursor.execute(my_query)
    result = cursor.fetchall()
    rows = cursor.fetchall()

    city_names = [row[0] for row in result]
    print(", ".join(city_names))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>  <statename>".format(sys.argv[0]))
        sys.exit(1)
    else:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
