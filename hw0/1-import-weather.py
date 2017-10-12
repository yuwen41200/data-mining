#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mariadb
import xml.etree.ElementTree as ElementTree

if __name__ == '__main__':
    cnx = mariadb.connect(user='root', host='localhost', database='dm', charset='utf8')
    cursor = cnx.cursor()
    tree = ElementTree.parse('../dataset/weather.xml')
    root = tree.getroot()
    ns = {'cwb': 'urn:cwb:gov:tw:cwbcommon:0.1'}
    for loc in root.find('cwb:dataset', ns).findall('cwb:location', ns):
        sta = loc.find('cwb:locationName', ns).text
        for cat in loc.findall('cwb:weatherElement', ns):
            if cat.find('cwb:elementName', ns).text == '逐時觀測':
                for row in cat.findall('cwb:time', ns):
                    time = row.find('cwb:obsTime', ns).text + ':00'  # YYYY-MM-DD HH:MM:SS
                    if time.endswith('24:00:00'):  # 24:00 is not allowed in MariaDB datetime
                        time = time.replace('24:00:00', '23:59:59')  # change it to 23:59
                    p, t, h, v, d, r, s = None, None, None, None, None, None, None
                    for col in row.findall('cwb:weatherElement', ns):
                        if col.find('cwb:elementName', ns).text == '測站氣壓':
                            p = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '溫度':
                            t = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '相對濕度':
                            h = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '風速':
                            v = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '風向':
                            d = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '降水量':
                            r = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                            r = None if r == 'T' else r  # some record has invalid value T
                        elif col.find('cwb:elementName', ns).text == '日照時數':
                            s = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        else:
                            print('WTF?!', col.find('cwb:elementName', ns).text)
                    query = (
                        "INSERT INTO 逐時觀測 "
                        "(測站, 時間, 測站氣壓, 溫度, 相對濕度, 風速, 風向, 降水量, 日照時數) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (sta, time, p, t, h, v, d, r, s))
            elif cat.find('cwb:elementName', ns).text == '每日統計':
                for row in cat.findall('cwb:time', ns):
                    time = row.find('cwb:obsTime', ns).text + ' 00:00:00'  # YYYY-MM-DD HH:MM:SS
                    ht, lt, at = None, None, None
                    for col in row.findall('cwb:weatherElement', ns):
                        if col.find('cwb:elementName', ns).text == '當日最高溫度(°C)':
                            ht = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '當日最低溫度(°C)':
                            lt = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        elif col.find('cwb:elementName', ns).text == '當日平均溫度(°C)':
                            at = col.find('cwb:elementValue', ns).find('cwb:value', ns).text
                        else:
                            print('WTF?!', col.find('cwb:elementName', ns).text)
                    query = (
                        "INSERT INTO 每日統計 "
                        "(測站, 時間, 當日最高溫度, 當日最低溫度, 當日平均溫度) "
                        "VALUES (%s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (sta, time, ht, lt, at))
            else:
                print('WTF?!', cat.find('cwb:elementName', ns).text)
    cnx.commit()
    cursor.close()
    cnx.close()
