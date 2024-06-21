#!/usr/bin/python3
"""
2-My filter states modeule
"""
import MySQLdb
import sys


def list_all_states(username, db_password, db_name, state_searched):
    """list_all_states function

    Args:
        username (string): The username of the database
        db_password (String): Database password
        db_name (String): Database name
        state_searched(String): State to search
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         password=db_password,
                         db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_searched)
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
        cursor.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <user> <pwd> <db> <state>".format(sys.argv[0]))
        sys.exit(1)
    else:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
