#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mariadb

if __name__ == '__main__':
    cnx = mariadb.connect(user='root', host='localhost', database='dm', charset='utf8')
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Power")
    for (updateTime, northSupply, northUsage, centerSupply, centerUsage, southSupply, southUsage, eastSupply, eastUsage) in cursor:
        pass
        # TODO
    cursor.close()
    cnx.close()
