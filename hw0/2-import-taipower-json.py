#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import mysql.connector as mariadb
import json


def parse_time(str_time):
    t1 = str_time.split('(')
    t2 = t1[0].split('.')
    y, m, d = t2[0], t2[1], t2[2]
    t2 = t1[1].split(')')
    t3 = t2[1].split(':')
    h, i, s = t3[0], t3[1], 0
    dt = datetime.datetime(int(y)+1911, int(m), int(d), int(h), int(i), int(s))
    return dt


if __name__ == '__main__':
    cnx = mariadb.connect(user='root', host='localhost', database='dm', charset='utf8')
    cursor = cnx.cursor()
    with open('../dataset/power.json') as fp:
        rows = json.load(fp)
    for row in rows:
        # print(json.dumps(row, indent=4))
        ut = parse_time(row['reserveData']['updateTime'])
        # use the "updateTime" in "reserveData" because it is detailed and uses local timezone
        ns = row['regionData']['northSupply']
        nu = row['regionData']['northUsage']
        cs = row['regionData']['centerSupply']
        cu = row['regionData']['centerUsage']
        ss = row['regionData']['southSupply']
        su = row['regionData']['southUsage']
        es = row['regionData']['eastSupply']
        eu = row['regionData']['eastUsage']
        query = (
            "INSERT INTO Power "
            "(updateTime, northSupply, northUsage, centerSupply, centerUsage,"
            " southSupply, southUsage, eastSupply, eastUsage) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(query, (ut, ns, nu, cs, cu, ss, su, es, eu))
    cnx.commit()
    cursor.close()
    cnx.close()
