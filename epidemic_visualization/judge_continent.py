import re
import requests
from lxml import etree
import utils
from continents import CONTINENTS

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
}


def judge(resp):
    asia, europe, south_america, africa, oceania, north_america = [], [], [], [], [], []
    for res in resp:
        url = f"https://www.sogou.com/web?query={res['name']}是哪个洲的"
        response = requests.get(url, headers=headers)
        try:
            page = etree.HTML(response.text)
            continent = page.xpath("//h4/text()")[0].strip()
        except:
            try:
                continent = re.findall("[亚欧非北美大洋南美]洲", response.text)[0]
            except Exception as e:
                print(e)
                continue
        print(res['name'], continent)
        if continent == '亚洲':
            asia.append(res['name'])
        elif continent == '欧洲':
            europe.append(res['name'])
        elif continent == '南美洲':
            south_america.append(res['name'])
        elif continent == '非洲':
            africa.append(res['name'])
        elif continent == '大洋洲':
            oceania.append(res['name'])
        elif continent == '北美洲':
            north_america.append(res['name'])

    continents = {
        '亚洲': asia, '欧洲': europe, '南美洲': south_america,
        '非洲': africa, '大洋洲': oceania, '北美洲': north_america
    }

    with open('./continents.py', 'w', encoding='gbk') as file:
        file.write(str(continents))


def count_rate(resp):
    value_as = value_eu = value_sa = value_af = value_oc = value_na = 0
    for res in resp:
        if res['name'] in CONTINENTS['亚洲']:
            value_as += res['value']
        elif res['name'] in CONTINENTS['欧洲']:
            value_eu += res['value']
        elif res['name'] in CONTINENTS['南美洲']:
            value_sa += res['value']
        elif res['name'] in CONTINENTS['非洲']:
            value_af += res['value']
        elif res['name'] in CONTINENTS['大洋洲']:
            value_oc += res['value']
        elif res['name'] in CONTINENTS['北美洲']:
            value_na += res['value']
    value_all = value_as + value_eu + value_sa + value_af + value_oc + value_na
    asia = value_as / value_all  # 亚洲
    europe = value_eu / value_all  # 欧洲
    south_america = value_sa / value_all  # 南美洲
    africa = value_af / value_all  # 非洲
    oceania = value_oc / value_all  # 大洋洲
    north_america = value_na / value_all  # 北美洲
    # print(asia, europe, south_america, africa, oceania, north_america)
    return asia, europe, south_america, africa, oceania, north_america


def get_l1_data():
    data = utils.get_l1_data()
    res = []
    for tub in data:
        res.append({'name': tub[0], 'value': int(tub[1])})
    return res


if __name__ == '__main__':
    res = get_l1_data()
    # judge(res)
    count_rate(res)
