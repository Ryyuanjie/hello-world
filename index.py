# coding=utf-8
import httplib
import threading


def jb51():
    url = "http://www.baidu.com"
    conn = httplib.HTTPConnection("www.baidu.com")
    conn.request(method="GET", url=url)
    response = conn.getresponse()
    res = response.status
    print res


threads = []
for i in range(10):
    t = threading.Thread(target=jb51, args=())
    # 把创建的线程加入线程组
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in threads:
        i.start()
        # keep thread
    for i in threads:
        i.join()
