from multiprocessing import Process, Lock
import json, time, random


# 查票
def search(i):
    with open('data', 'r', encoding='utf8') as f:
        dic = json.load(f)
    print('用户%s查询余票：%s' % (i, dic.get('ticket_num')))


def buy(i, lock):
    search(i)		# 先查票
	# 再买票
    lock.acquire()  # 抢锁
    time.sleep(random.randint(1, 3))
    with open('data', 'r', encoding='utf8') as f:
        dic = json.load(f)
    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        with open('data', 'w', encoding='utf8') as f:
            json.dump(dic, f)
        print('用户%s买票成功' % i)
    else:
        print('用户%s买票失败' % i)
    lock.release()  # 释放锁



if __name__ == '__main__':
    lock = Lock()
    for i in range(1, 11):
        p = Process(target=buy, args=[i, lock])
        p.start()