#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mariadb
import xml.etree.ElementTree as ElementTree

if __name__ == '__main__':
    cnx = mariadb.connect(user='root', database='dm')
    cursor = cnx.cursor()
    tree = ElementTree.parse('../dataset/weather.xml')
    root = tree.getroot()
    for loc in root.find('dataset').findall('location'):
        sta = loc.find('locationName').text
        for cat in loc.findall('weatherElement'):
            if cat.find('elementName').text == '逐時觀測':
                for row in cat.findall('time'):
                    time = row.find('obsTime').text + ':00'  # YYYY-MM-DD HH:MM:SS
                    p, t, h, v, d, r, s = None, None, None, None, None, None, None
                    for col in row.findall('weatherElement'):
                        if col.find('elementName').text == '測站氣壓':
                            p = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '溫度':
                            t = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '相對濕度':
                            h = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '風速':
                            v = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '風向':
                            d = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '降水量':
                            r = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '日照時數':
                            s = col.find('elementValue').find('value').text
                        else:
                            print('WTF?!', col.find('elementName').text)
                    query = (
                        "INSERT INTO 逐時觀測 "
                        "(測站, 時間, 測站氣壓, 溫度, 相對濕度, 風速, 風向, 降水量, 日照時數) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (sta, time, p, t, h, v, d, r, s))
            elif cat.find('elementName').text == '每日統計':
                for row in cat.findall('time'):
                    time = row.find('obsTime').text + ' 00:00:00'  # YYYY-MM-DD HH:MM:SS
                    ht, lt, at = None, None, None
                    for col in row.findall('weatherElement'):
                        if col.find('elementName').text == '當日最高溫度(°C)':
                            ht = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '當日最低溫度(°C)':
                            lt = col.find('elementValue').find('value').text
                        elif col.find('elementName').text == '當日平均溫度(°C)':
                            at = col.find('elementValue').find('value').text
                        else:
                            print('WTF?!', col.find('elementName').text)
                    query = (
                        "INSERT INTO 每日統計 "
                        "(測站, 時間, 當日最高溫度, 當日最低溫度, 當日平均溫度) "
                        "VALUES (%s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (sta, time, ht, lt, at))
            else:
                print('WTF?!', cat.find('elementName').text)
    cnx.commit()
    cursor.close()
    cnx.close()
