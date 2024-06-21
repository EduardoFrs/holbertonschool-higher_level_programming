#!/usr/bin/python3

""" script that list all cities of the state in arg"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name = '{}' \
                ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
