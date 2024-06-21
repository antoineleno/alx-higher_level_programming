#!/usr/bin/python3
"""
1-filter_states
"""
import MySQLdb
import sys


def list_all_states(username, db_password, db_name):
    """list_all_states function

    Args:
        username (string): The username of the database
        db_password (String): Database password
        db_name (String): Database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         password=db_password,
                         db=db_name)

    cursor = db.cursor()
    MY_query = ("SELECT * FROM states WHERE "
                "name COLLATE utf8mb4_bin LIKE 'N%' ORDER BY states.id ASC")
    cursor.execute(MY_query)
    result = cursor.fetchall()
    for row in result:
        print(row)
        cursor.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    else:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
