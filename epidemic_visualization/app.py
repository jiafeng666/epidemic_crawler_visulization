import datetime
from flask import Flask
from flask import render_template
from flask import jsonify
import utils
import judge_continent
from apscheduler.schedulers.blocking import BlockingScheduler


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route("/top", methods=['get', 'post'])
def get_update_top():
    data = utils.get_update_top()
    nation, updates = [], []
    for tub in data[0:10]:
        nation.append(tub[0])
        updates.append(int(tub[1]))
    return jsonify({"nation": nation, "updates": updates})


@app.route('/c1', methods=['get', 'post'])
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm": str(data[0]), "dead": str(data[1]), "heal": str(data[2]), "motrality": str(data[3])})


@app.route('/china_c1', methods=['get', 'post'])
def get_c1_china_data():
    data = utils.get_c1_china_data()
    return jsonify(
        {"confirm": str(data[0]), "symptom": str(data[1]), "suspected": str(data[2]), "overseas": str(data[3])})


@app.route("/c2", methods=['get', 'post'])
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


@app.route("/world", methods=['get', 'post'])
def get_world_c2_data():
    res = []
    for tup in utils.get_world_c2_data():
        res.append({'name': tup[0], 'value': int(tup[1])})
    china_num = utils.get_china_total_now()
    res.append({'name': '中国', 'value': china_num})
    return jsonify({'data': res})


@app.route("/l1", methods=['get', 'post'])
def get_l1_data():
    data = utils.get_l1_data()
    res = []
    for tub in data[0:10]:
        res.append({'name': tub[0], 'value': int(tub[1])})
    return jsonify({'data': res})


@app.route("/l2", methods=['get', 'post'])
def get_l2_data():
    data = utils.get_l2_data()
    day, local_add, foreign_add = [], [], []
    for a, b, c in data:
        day.append(a)
        local_add.append(b)
        foreign_add.append(c)
    return jsonify({"day": day[-20:], "local_add": local_add[-20:], "foreign_add": foreign_add[-20:]})


@app.route("/china_l2", methods=['get', 'post'])
def get_l2_china_data():
    local_data, input_data = utils.get_l2_china_data()
    day, local_add, input_add = [], [], []
    for a, b in local_data:
        day.append(a)
        local_add.append(b)
    for a, b in input_data:
        input_add.append(b)
    return jsonify({"day": day[-20:], "local_add": local_add[-20:], "input_add": input_add[-20:]})


@app.route("/china_r1", methods=['get', 'post'])
def get_r1_china_data():
    data = utils.get_r1_china_data()
    province, confirm = [], []
    for tub in data[0:10]:
        province.append(tub[0])
        confirm.append(int(tub[1]))
    return jsonify({"province": province, "confirm": confirm})


@app.route("/r2", methods=['get', 'post'])
def get_r2_china_data():
    datas = utils.get_r2_china_data()
    province, newly, now, total, cured, death = [], [], [], [], [], []
    for data in datas:
        province.append(data[0])
        newly.append(data[1])
        now.append(data[2])
        total.append(data[3])
        cured.append(data[4])
        death.append(data[5])
    return jsonify({"province": province, "newly": newly, "now": now, "total": total, "cured": cured, "death": death})


@app.route("/F2", methods=['get', 'post'])
def get_R2_world_data():
    datas = utils.get_R2_world_data()
    print(datas)
    province, newly, total, cured, death = [], [], [], [], []
    for data in datas:
        province.append(data[0])
        newly.append(data[1])
        total.append(data[2])
        cured.append(data[3])
        death.append(data[2])
    return jsonify({"province": province, "newly": newly, "total": total, "cured": cured, "death": death})


@app.route("/aa", methods=['get', 'post'])
def get_na_data():
    data = utils.get_l1_data()
    res = []
    for tub in data:
        res.append({'name': tub[0], 'value': int(tub[1])})
    data = []
    asia, europe, south_america, africa, oceania, north_america = judge_continent.count_rate(res)
    data.append({'name': '亚洲', 'value': asia})
    data.append({'name': '欧洲', 'value': europe})
    data.append({'name': '南美洲', 'value': south_america})
    data.append({'name': '非洲', 'value': africa})
    data.append({'name': '大洋洲', 'value': oceania})
    data.append({'name': '北美洲', 'value': north_america})
    return jsonify({"data": data})


@app.route("/home_data", methods=['get', 'post'])  # 资讯
def get_home_data():
    data = utils.get_home_news()
    headline, link, pubtime = [], [], []
    for a, b, c in data:
        headline.append(a)
        link.append(b)
        pubtime.append(c)
    return jsonify({"headline": headline, "link": link, "pubtime": pubtime})


@app.route("/abroad_data", methods=['get', 'post'])
def get_abroad_data():
    data = utils.get_abroad_news()
    headline, link, pubtime = [], [], []
    for a, b, c in data:
        headline.append(a)
        link.append(b)
        pubtime.append(c)
    return jsonify({"headline": headline, "link": link, "pubtime": pubtime})


if __name__ == '__main__':
    # app.run()
    scheduler = BlockingScheduler()
    scheduler.add_job(app.run(), 'cron', hour=12, minute=30, next_run_time=datetime.datetime.now())
    scheduler.start()
