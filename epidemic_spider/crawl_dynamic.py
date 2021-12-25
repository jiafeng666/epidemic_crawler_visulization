import time
import datetime
from lxml import etree
from selenium.webdriver.common.action_chains import ActionChains
from apscheduler.schedulers.blocking import BlockingScheduler
from driver import get_driver
from save_to_sqlite import ConnSqlite


class CrawlDataDynamic(object):
    def __init__(self):
        self.data = {}

    def get_data(self):
        url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"
        driver = get_driver()
        driver.get(url)
        time.sleep(2)
        self.data["新增本土趋势"] = [data for data in self.gen("dain", driver)]
        self.data["境外输入新增趋势"] = [data for data in self.gen("daou", driver)]
        self.data["国内/国外新增确诊 趋势"] = [data for data in self.gen("daio", driver)]
        self.data["国外累计确诊/现有确诊 趋势"] = [data for data in self.gen("dasn", driver)]
        self.data["国外累计治愈/死亡 趋势"] = [data for data in self.gen("dacd", driver)]
        # print(self.data)
        # with open("./data.txt", 'w') as f:    # 保存到txt文件
        #     f.write(str(self.data))
        driver.quit()
        self.save_data()

    def save_data(self):
        # print(self.data)
        coon = ConnSqlite()   # 连接数据库
        coon.create_dynamic()
        coon.insert_dynamic(self.data)

    @staticmethod
    def gen(kw, driver):
        """
        数据生成器，省时又省力
        @param kw: 传入爬取数据部分对应关键词
        @param driver:驱动
        """
        if kw == "dain":      # 新增本土趋势
            element = driver.find_element_by_xpath("//span[contains(text(), '新增本土: ')]/../../div[1]")
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)

            date_list = []
            for i in range(50):
                html = etree.HTML(driver.page_source)
                date = html.xpath("//span[contains(text(), '新增本土: ')]/../span[1]/text()")[0]
                if date in date_list:     # 去重
                    ActionChains(driver).move_by_offset(1.2, 0).perform()
                    continue
                    # html = etree.HTML(driver.page_source)   # 看移动后效果
                    # date = html.xpath("//span[contains(text(), '新增本土: ')]/../span[1]/text()")[0]
                else:
                    date_list.append(date)
                increase = html.xpath("//span[contains(text(), '新增本土: ')]/text()")[0].replace("新增本土: ", "")
                ActionChains(driver).move_by_offset(8, 0).perform()
                print({"日期": date, "新增本土": increase})
                yield {"日期": date, "新增本土": increase}

        if kw == 'daou':   # 境外输入新增趋势
            driver.find_element_by_xpath("//span[contains(text(), '新增趋势')]/../span[text()='境外输入']").click()
            time.sleep(1)
            element = driver.find_element_by_xpath("//div[@id='ptab-0']/div[4]/div[1]//span[contains(text(), '新增境外输入: ')]/../../div[1]")
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)

            date_list = []
            for i in range(50):
                html = etree.HTML(driver.page_source)
                date = html.xpath("//div[@id='ptab-0']/div[4]/div[1]//span[contains(text(), '新增境外输入: ')]/../span[1]/text()")[0]
                if date in date_list:  # 去重
                    ActionChains(driver).move_by_offset(1.2, 0).perform()
                    continue
                else:
                    date_list.append(date)
                increase = html.xpath("//div[@id='ptab-0']/div[4]/div[1]//span[contains(text(), '新增境外输入: ')]/text()")[0].replace("新增境外输入: ", "")
                ActionChains(driver).move_by_offset(8, 0).perform()
                print({"日期": date, "新增境外输入": increase})
                yield {"日期": date, "新增境外输入": increase}

        if kw == 'daio':   # 国内/国外新增确诊 趋势
            element = driver.find_element_by_xpath("//span[contains(text(), '国内: ')]/../../div[1]")
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)

            date_list = []
            for i in range(50):
                html = etree.HTML(driver.page_source)
                date = html.xpath("//span[contains(text(), '国内: ')]/../span[1]/text()")[0]
                if date in date_list:  # 去重
                    ActionChains(driver).move_by_offset(1.2, 0).perform()
                    continue
                else:
                    date_list.append(date)
                increase_in = html.xpath("//span[contains(text(), '国内: ')]/text()")[0].replace("国内: ", "")
                increase_fr = html.xpath("//span[contains(text(), '国外: ')]/text()")[0].replace("国外: ", "")
                ActionChains(driver).move_by_offset(8, 0).perform()
                print({"日期": date, "国内": increase_in, "国外": increase_fr})
                yield {"日期": date, "国内": increase_in, "国外": increase_fr}

        if kw == 'dasn':   # 国外累计确诊/现有确诊 趋势
            driver.find_element_by_xpath("//span[contains(text(), '国外累计确诊/')]").click()
            time.sleep(1)
            element = driver.find_element_by_xpath("//span[contains(text(), '累计确诊: ')]/../../div[1]")
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)

            date_list = []
            for i in range(50):
                html = etree.HTML(driver.page_source)
                date = html.xpath("//span[contains(text(), '累计确诊: ')]/../span[1]/text()")[0]
                if date in date_list:  # 去重
                    ActionChains(driver).move_by_offset(1.2, 0).perform()
                    continue
                else:
                    date_list.append(date)
                sum_infect = html.xpath("//span[contains(text(), '累计确诊: ')]/text()")[0].replace("累计确诊: ", "")
                now_infect = html.xpath("//span[contains(text(), '现有确诊: ')]/text()")[0].replace("现有确诊: ", "")
                ActionChains(driver).move_by_offset(8, 0).perform()
                print({"日期": date, "累计确诊": sum_infect, "现有确诊": now_infect})
                yield {"日期": date, "累计确诊": sum_infect, "现有确诊": now_infect}

        if kw == 'dacd':   # 国外累计治愈/死亡 趋势
            driver.find_element_by_xpath("//span[contains(text(), '治愈/死亡')]").click()
            time.sleep(1)
            element = driver.find_element_by_xpath("//span[contains(text(), '治愈: ')]/../../div[1]")
            ActionChains(driver).move_to_element(element).perform()
            time.sleep(2)

            date_list = []
            for i in range(50):
                html = etree.HTML(driver.page_source)
                date = html.xpath("//span[contains(text(), '治愈: ')]/../span[1]/text()")[0]
                if date in date_list:  # 去重
                    ActionChains(driver).move_by_offset(1.2, 0).perform()
                    continue
                else:
                    date_list.append(date)
                cure = html.xpath("//span[contains(text(), '治愈: ')]/text()")[0].replace("治愈: ", "")
                death = html.xpath("//span[contains(text(), '死亡: ')]/text()")[0].replace("死亡: ", "")
                ActionChains(driver).move_by_offset(8, 0).perform()
                print({"日期": date, "治愈": cure, "死亡": death})
                yield {"日期": date, "治愈": cure, "死亡": death}


if __name__ == '__main__':
    crawl = CrawlDataDynamic()
    scheduler = BlockingScheduler()
    scheduler.add_job(crawl.get_data, 'cron', hour=12, minute=15, next_run_time=datetime.datetime.now())
    scheduler.start()

