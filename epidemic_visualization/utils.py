# -*- coding:utf-8 -*-
"""==============================
@author: 
@file: utils.py
@date: 2020-07-02
@time: 11:27:46
=============================="""
import time
import sqlite3


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


# 连接数据库
def get_conn():
    conn = sqlite3.connect("../epidemic_database.db")
    # 创建游标：
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    '''
    :param sql:
    :param args:
    :return:返回结果，((),())形式
    '''
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()  # 获取结果
    close_conn(conn, cursor)
    return res


def get_update_top():
    sql = "select fr_district,fr_newly_increased from each_nation_num " \
          "order by cast(fr_newly_increased as int) desc"
    res = query(sql)
    return res


def get_c1_data():
    sql = "select fr_sum_infect," \
          "fr_sum_die," \
          "fr_sum_cure," \
          "fr_mortality " \
          "from fr_situation_report "
    res = query(sql)
    return res[0]


def get_c1_china_data():
    sql = "select now_infect," \
          "no_symptom," \
          "now_suspected," \
          "overseas_input " \
          "from situation_report "
    res = query(sql)
    return res[0]


def get_c2_data():
    sql = "select district,now_infected from each_province_num " \
          "group by district"
    res = query(sql)
    return res


def get_china_total_now():
    sql = "select sum(total_now) from each_province_num "
    res = query(sql)
    return res


def get_world_c2_data():
    sql = "select fr_district,fr_total_now from each_nation_num " \
          "group by fr_district"
    res = query(sql)
    return res


def get_l1_data():
    sql = "select fr_district,fr_total_now from each_nation_num order by cast(fr_total_now as int) desc"
    res = query(sql)
    return res


def get_l2_data():
    sql = "select date,new_local,new_foreign from new_local_foreign_trend"
    res = query(sql)
    return res


def get_l2_china_data():
    sql = "select date,new_local from new_local_trend"
    sql1 = "select date,new_input from new_input_trend"
    res = query(sql)
    res1 = query(sql1)
    return res, res1


def get_r1_china_data():
    sql = "select district,newly_increased from each_province_num " \
          "order by cast(newly_increased as int) desc"
    res = query(sql)
    return res


def get_r2_china_data():
    sql = "select district,newly_increased,now_infected,total_now,cured,death from each_province_num"
    res = query(sql)
    return res


def get_R2_world_data():
    sql = "select fr_district,fr_newly_increased,fr_total_now,fr_cured,fr_death from each_nation_num"
    res = query(sql)
    return res


def get_home_news():   # 资讯
    sql = "select headline,link,pubtime from home_news"
    res = query(sql)
    return res


def get_abroad_news():
    sql = "select headline,link,pubtime from abroad_news"
    res = query(sql)
    return res


if __name__ == '__main__':
    # get_l1_data()
    #  get_r1_data()
    # get_r2_data()
    pass
