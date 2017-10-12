#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mariadb
import os

if __name__ == '__main__':
    cnx = mariadb.connect(user='root', host='localhost', database='dm', charset='utf8')
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM Power WHERE DATE(updateTime) = '2017-09-02'")
    # records on 2017/9/2 are inconsistent, remove those in JSON file
    cnx.commit()
    parent = os.path.join('..', 'dataset')
    files = os.listdir(parent)
    for file in files:
        if file.endswith('.csv'):
            with open(os.path.join(parent, file)) as fp:
                rows = fp.readlines()
            rows = [r.strip() for r in rows]
            date = file.split('.csv')[0]
            for row in rows:
                cols = row.split(',')
                time = str(date) + ' ' + cols[0] + ':00'  # YYYY-MM-DD HH:MM:SS
                query = (
                    "INSERT INTO Power "
                    "(updateTime, northSupply, northUsage, centerSupply, centerUsage,"
                    " southSupply, southUsage, eastSupply, eastUsage) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )
                data = (time, cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8])
                cursor.execute(query, data)
            print(file, 'imported')
    cnx.commit()
    cursor.close()
    cnx.close()
