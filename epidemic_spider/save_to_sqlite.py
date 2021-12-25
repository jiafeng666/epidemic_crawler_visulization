import sqlite3


class ConnSqlite(object):
    def __init__(self):
        self.db = sqlite3.connect('../epidemic_database.db')   # 创建/连接数据库

    def create_static(self):
        try:
            sql1 = """create table situation_report(
                    update_time text not null,
                    now_infect varchar(20),
                    no_symptom varchar(20),
                    now_suspected varchar(20),
                    now_severe varchar(20),
                    sum_infect varchar(20),
                    overseas_input varchar(20),
                    sum_cure varchar(20),
                    sum_die varchar(20)) """
            self.db.execute(sql1)

            sql2 = """create table now_infect_city(
                    city text not null,
                    new_local varchar(20),
                    now_infect varchar(20)) """
            self.db.execute(sql2)

            sql3 = """create table each_province_num(
                    district text not null,
                    newly_increased varchar(20),
                    now_infected varchar(20),
                    total_now varchar(20),
                    cured varchar(20),
                    death varchar(20)) """
            self.db.execute(sql3)

            sql4 = """create table each_city_num(
                    district text not null,
                    newly_increased varchar(20),
                    now_infected varchar(20),
                    total_now varchar(20),
                    cured varchar(20),
                    death varchar(20)) """
            self.db.execute(sql4)

            sql5 = """create table fr_situation_report(
                    fr_update_time text not null,
                    fr_now_infect varchar(20),
                    fr_sum_cure varchar(20),
                    fr_sum_die varchar(20),
                    fr_sum_infect varchar(20),
                    fr_cure_rate varchar(20),
                    fr_mortality varchar(20)) """
            self.db.execute(sql5)

            sql6 = """create table each_nation_num(
                    fr_district text not null,
                    fr_newly_increased varchar(20),
                    fr_total_now varchar(20),
                    fr_cured varchar(20),
                    fr_death varchar(20)) """
            self.db.execute(sql6)

            sql7 = """create table home_news(
                                headline text not null ,
                                link varchar(20),
                                pubtime varchar(20)) """
            self.db.execute(sql7)

            sql8 = """create table abroad_news(
                                headline text not null ,
                                link varchar(20),
                                pubtime varchar(20)) """
            self.db.execute(sql8)

        except Exception as e:
            print(e)

    def create_dynamic(self):
        try:
            sql1 = """create table new_local_trend(
                    date text not null,
                    new_local varchar(20)) """
            self.db.execute(sql1)

            sql2 = """create table new_input_trend(
                    date text not null,
                    new_input varchar(20)) """
            self.db.execute(sql2)

            sql3 = """create table new_local_foreign_trend(
                    date text not null,
                    new_local varchar(20),
                    new_foreign varchar(20)) """
            self.db.execute(sql3)

            sql4 = """create table foreign_sum_now_trend(
                    date text not null,
                    sum_infect varchar(20),
                    now_infect varchar(20)) """
            self.db.execute(sql4)

            sql5 = """create table foreign_cure_die_trend(
                    date text not null,
                    cure varchar(20),
                    death varchar(20)) """
            self.db.execute(sql5)

        except Exception as e:
            print(e)

    def insert_static(self, data_dict):
        try:
            sql_1 = """INSERT INTO situation_report(update_time, now_infect, no_symptom, now_suspected, now_severe, sum_infect, overseas_input, sum_cure, sum_die)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            data_1 = (
                data_dict['更新时间'], data_dict['现有确诊'], data_dict['无症状'], data_dict['现有疑似'], data_dict['现有重症'],
                data_dict['累计确诊'], data_dict['境外输入'], data_dict['累计治愈'], data_dict['累计死亡'])
            self.db.execute(sql_1, data_1)

            now_infect_city = data_dict['现存确诊城市']
            for nic in now_infect_city:
                sql_2 = """INSERT INTO now_infect_city(city, new_local, now_infect)VALUES(?, ?, ?)"""
                data_2 = (nic['城市'], nic['新增本土'], nic['现有病例'])
                self.db.execute(sql_2, data_2)

            infect_pro_list = data_dict['各省份累计病例']
            for pro in infect_pro_list:
                sql_3 = """INSERT INTO each_province_num(district, newly_increased, now_infected, total_now, cured, death)VALUES(?, ?, ?, ?, ?, ?) """
                data_3 = (pro['地区'], pro['新增'], pro['现有'], pro['累计'], pro['治愈'], pro['死亡'])
                self.db.execute(sql_3, data_3)

            infect_city_list = data_dict['各城市累计病例']
            for cit in infect_city_list:
                sql_4 = """INSERT INTO each_city_num(district, newly_increased, now_infected, total_now, cured, death)VALUES(?, ?, ?, ?, ?, ?)"""
                data_4 = (cit['地区'], cit['新增'], cit['现有'], cit['累计'], cit['治愈'], cit['死亡'])
                self.db.execute(sql_4, data_4)

            sql_5 = """INSERT INTO fr_situation_report(fr_update_time, fr_now_infect, fr_sum_cure, fr_sum_die, fr_sum_infect, fr_cure_rate, fr_mortality)VALUES(?, ?, ?, ?, ?, ?, ?)"""
            data_5 = (
                data_dict['国外疫情数据更新时间'], data_dict['国外现有确诊'], data_dict['国外累计治愈'], data_dict['国外累计死亡'],
                data_dict['国外累计确诊'], data_dict['国外治愈率'], data_dict['国外死亡率'])
            self.db.execute(sql_5, data_5)

            infect_nation_list = data_dict['各国累计病例']
            for nat in infect_nation_list:
                sql_6 = """INSERT INTO each_nation_num(fr_district, fr_newly_increased, fr_total_now, fr_cured, fr_death)VALUES(?, ?, ?, ?, ?)"""
                data_6 = (nat['地区'], nat['新增'], nat['累计'], nat['治愈'], nat['死亡'])
                self.db.execute(sql_6, data_6)

            news_list_cn = data_dict['国内资讯']
            for news in news_list_cn:
                sql_7 = """INSERT INTO home_news(headline, link, pubtime)VALUES(?, ?, ?)"""
                data_7 = (news['标题'], news['链接'], news['时间'])
                self.db.execute(sql_7, data_7)

            news_list_fr = data_dict['国外资讯']
            for news in news_list_fr:
                sql_8 = """INSERT INTO abroad_news(headline, link, pubtime)VALUES(?, ?, ?)"""
                data_8 = (news['标题'], news['链接'], news['时间'])
                self.db.execute(sql_8, data_8)

        except Exception as e:
            print(e)

    def insert_dynamic(self, data_dict):
        try:
            new_local_list = data_dict['新增本土趋势']
            for loc in new_local_list:
                sql_1 = """INSERT INTO new_local_trend(date, new_local)VALUES(?, ?)"""
                data_1 = (loc['日期'], loc['新增本土'])
                self.db.execute(sql_1, data_1)

            new_input_list = data_dict['境外输入新增趋势']
            for inp in new_input_list:
                sql_2 = """INSERT INTO new_input_trend(date, new_input)VALUES(?, ?)"""
                data_2 = (inp['日期'], inp['新增境外输入'])
                self.db.execute(sql_2, data_2)

            new_lofo_list = data_dict['国内/国外新增确诊 趋势']
            for lofo in new_lofo_list:
                sql_3 = """INSERT INTO new_local_foreign_trend(date, new_local, new_foreign)VALUES(?, ?, ?)"""
                data_3 = (lofo['日期'], lofo['国内'], lofo['国外'])
                self.db.execute(sql_3, data_3)

            fr_suno_list = data_dict['国外累计确诊/现有确诊 趋势']
            for suno in fr_suno_list:
                sql_4 = """INSERT INTO foreign_sum_now_trend(date, sum_infect, now_infect)VALUES(?, ?, ?)"""
                data_4 = (suno['日期'], suno['累计确诊'], suno['现有确诊'])
                self.db.execute(sql_4, data_4)

            fr_cude_list = data_dict['国外累计治愈/死亡 趋势']
            for cude in fr_cude_list:
                sql_5 = """INSERT INTO foreign_cure_die_trend(date, cure, death)VALUES(?, ?, ?)"""
                data_5 = (cude['日期'], cude['治愈'], cude['死亡'])
                self.db.execute(sql_5, data_5)

        except Exception as e:
            print(e)

    def __del__(self):
        self.db.commit()  # 提交操作
        print("数据已存到数据库！")
        self.db.close()  # 关闭数据库连接
