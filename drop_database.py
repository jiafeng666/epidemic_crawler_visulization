import os
from apscheduler.schedulers.blocking import BlockingScheduler


def remove():
    path = 'epidemic_database.db'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)  # 删除文件，可使用以下两种方法。
        # os.unlink(path)
    else:
        print(f'no such file: {path}')  # 则返回文件不存在


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(remove, 'cron', hour=18)
    scheduler.start()