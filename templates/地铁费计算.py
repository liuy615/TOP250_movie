# -*- coding: utf-8 -*
# @Time    : 2023/1/3 15:55
# @Author  : liuy
# @File    : 地铁费计算.py
"""
项目目的：此脚本主要是根据工作日计算出每月所需要的地铁费
基本属性：
    1.周一至周五单次地铁费：8，周6单次地铁费：7
    2.每日往返2次
    3.累积地铁费未达到200，地铁费9折，达到200之后地铁费6折
    4.每月月初自动清零
项目思路：
    1.根据输入的年月得到当月的第一天，依次判断此后是否为工作日
    2.做一个循环，累积计算地铁费
    3.做一个判断，当未达到200，按9折计算，达到200，按6折计算。
优化思路
    1. 此项目未考虑节假日对时间的影响，这个问题值得优化
    2. 此项目未考虑实际生活中的随机性，比如地铁临时打八折，或者某一天不坐地铁，这种随机性很难预测
"""


import datetime


def main():
    print("这是程序的入口")


def Metro_fee(year, month):
    money = 0
    day = datetime.date(year, month, 1)
    # last_day = str(day - datetime.timedelta(days=1))[-2:]  # 获取上个月一共多少天
    last_day = day - datetime.timedelta(days=1)
    for i in range(int(last_day.day)):
        day_num = day.isoweekday()
        if money < 200:
            if day_num < 6:
                money = money + (8*2)*0.9
            elif day_num == 6:
                money = money + (7*2)*0.9
            else:
                money = money
        else:
            if day_num < 6:
                money = money + (8*2)*0.6
            elif day_num == 6:
                money = money + (7*2)*0.6
            else:
                money = money
        day = day + datetime.timedelta(days=1)

    return round(money, 2)


print(Metro_fee(2023, 1))
if __name__ == '__main__':
    print("程序结束！")
