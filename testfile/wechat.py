
'''
import time
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date

a=timestamp_to_date(1573142400)
print(a)
'''
# coding=utf-8
import requests
from locust import HttpLocust,TaskSet,task
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class MyBlogs(TaskSet):
    # 访问我的博客首页
    @task(1)
    def get_blog(self):
        # 定义请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        req = self.client.get("/imyalost",  headers=header, verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")

class websitUser(HttpLocust):
    task_set = MyBlogs
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f wechat.py --host=https://tx-demo.ikandy.cn:4001/login")
