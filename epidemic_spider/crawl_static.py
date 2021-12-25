import time
import datetime
from lxml import etree
from driver import get_driver
from save_to_sqlite import ConnSqlite
from apscheduler.schedulers.blocking import BlockingScheduler


class CrawlDataStatic(object):
    def __init__(self):
        self.data = {}

    def get_detail(self):
        url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"
        try:
            driver = get_driver()
            driver.get(url)
            time.sleep(4)
            folds = driver.find_elements_by_xpath("//span[contains(text(), '展开全部')]")  # 点击展开全部
            for fold in folds[:3]:
                fold.click()
            time.sleep(4)
            tags = driver.find_elements_by_xpath("//div[@id='nationTable']//tbody/tr/td[1]")
            for tag in tags:
                driver.execute_script("arguments[0].click();", tag)
            time.sleep(4)
            html = driver.page_source
            page = etree.HTML(html)

            """————————国内疫情————————"""
            update_time_cn = page.xpath("//div[contains(text(), '国内疫情')]/../div[2]/span/text()")[0]
            _time = update_time_cn.replace("数据更新至 ", '')
            self.data['更新时间'] = _time
            elements = page.xpath("//div[@id='ptab-0']//div[contains(@class, '2ZJJBJ')]/text()")  # 疫情速报
            self.epidemic_report(elements)

            extract_cities = page.xpath("//div[contains(@class, '2IAAkE')]/div[2]/a")  # 现有确诊城市
            city_list = []
            for city in extract_cities:
                city_dict = {
                    '城市': city.xpath("./div/div[1]/div/span[1]//text()")[0],
                    '新增本土': city.xpath("./div/div[2]//text()")[0],
                    '现有病例': city.xpath("./div/div[3]//text()")[0]
                }
                city_list.append(city_dict)
            self.data['现存确诊城市'] = city_list

            districts = page.xpath("//tbody/tr[contains(@class, '3m6Ybq')]")  # 各省份累计病例
            province_list = []
            for dis in districts:
                province_dict = {
                    '地区': dis.xpath("./td[1]//text()")[0],
                    '新增': dis.xpath("./td[2]/text()")[0],
                    '现有': dis.xpath("./td[3]/text()")[0],
                    '累计': dis.xpath("./td[4]/text()")[0],
                    '治愈': dis.xpath("./td[5]/text()")[0],
                    '死亡': dis.xpath("./td[6]/text()")[0]
                }
                province_list.append(province_dict)
            self.data["各省份累计病例"] = province_list

            cities = page.xpath("//div[@id='nationTable']//td[@colspan='6']//tbody/tr")  # 各城市累计病例
            each_list = []
            for cit in cities:
                each_dict = {
                    '地区': cit.xpath("./td[1]//text()")[0],
                    '新增': cit.xpath("./td[2]/text()")[0],
                    '现有': cit.xpath("./td[3]/text()")[0],
                    '累计': cit.xpath("./td[4]/text()")[0],
                    '治愈': cit.xpath("./td[5]/text()")[0],
                    '死亡': cit.xpath("./td[6]/text()")[0]
                }
                each_list.append(each_dict)
            self.data["各城市累计病例"] = each_list

            news_cn = page.xpath("//div[contains(@class, '2SKAfr')]/div")  # 国内资讯
            news_list = []
            for news in news_cn[:10]:
                news_dict = {
                    '标题': news.xpath("./div[2]//text()")[0],
                    '链接': news.xpath("./@href")[0],
                    '时间': ''.join(news.xpath("./div[1]//text()"))
                }
                news_list.append(news_dict)
            self.data['国内资讯'] = news_list

            """————————国外疫情————————"""
            update_time_fr = page.xpath("//div[@id='ptab-4']//span[contains(text(), '数据更新至')]//text()")[0]
            time_fr = update_time_fr.replace('数据更新至', '')
            self.data['国外疫情数据更新时间'] = time_fr
            elements_fr = page.xpath("//div[contains(@class, '2fhqEt')]/text()")
            self.fr_epidemic_report(elements_fr)

            nations = page.xpath("//div[@id='foreignTable']//tr[@data-type='btn']")  # 各国累计病例
            nation_list = []
            for nat in nations:
                nation_dict = {
                    '地区': nat.xpath("./td[1]//text()")[0],
                    '新增': nat.xpath("./td[2]/text()")[0],
                    '累计': nat.xpath("./td[3]/text()")[0],
                    '治愈': nat.xpath("./td[4]/text()")[0],
                    '死亡': nat.xpath("./td[5]/text()")[0]
                }
                nation_list.append(nation_dict)
            self.data['各国累计病例'] = nation_list

            driver.find_element_by_xpath("//div[contains(text(), '国外资讯')]").click()  # 国外资讯
            html = driver.page_source
            page = etree.HTML(html)
            news_fr = page.xpath("//div[contains(@class, '2SKAfr')]/div")
            news_list_fr = []
            for news in news_fr[:10]:
                news_dict = {
                    '标题': news.xpath("./div[2]//text()")[0],
                    '链接': news.xpath("./@href")[0],
                    '时间': ''.join(news.xpath("./div[1]//text()"))
                }
                news_list_fr.append(news_dict)
            self.data['国外资讯'] = news_list_fr

            driver.quit()
            self.save_data()
        except Exception as e:
            print(e)

    def epidemic_report(self, num_list):
        value_list = ['现有确诊', '无症状', '现有疑似', '现有重症', '累计确诊', '境外输入', '累计治愈', '累计死亡']
        index = 0
        for i in value_list:
            self.data[i] = num_list[index]
            index += 1

    def fr_epidemic_report(self, no_list):
        fr_value_list = ['国外现有确诊', '国外累计治愈', '国外累计死亡', '国外累计确诊', '国外治愈率', '国外死亡率']
        index = 0
        for val in fr_value_list:
            self.data[val] = no_list[index]
            index += 1

    def save_data(self):
        # print(dict_data)
        database = ConnSqlite()  # 创建数据库
        database.create_static()    # 创建表格
        database.insert_static(self.data)   # 插入数据


if __name__ == '__main__':
    crawl = CrawlDataStatic()
    scheduler = BlockingScheduler()
    scheduler.add_job(crawl.get_detail, 'cron', hour=12, next_run_time=datetime.datetime.now())
    scheduler.start()

