from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
import os
import logging
from locust import HttpLocust, TaskSet, task

def index(l):
    l.client.get("/")

def stats(l):
    l.client.get("/stats/requests")

class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    tasks = [index, stats]
    # 列出需要测试的任务形式二 
    @task
    def page404(self):
        self.client.get("/does_not_exist")
    
class WebsiteUser(HttpLocust):
    #host = "http://127.0.0.1:8089"
    host = 'https://www.baidu.com'
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks


def show_time(f):
    def inner():
        start = time.time
        f()
        end = time.time()
        print('jieshu')
    return inner
#装饰器写法
@show_time    #类似：foo = show_time(foo)
def foo():
    print('ttttt')



if __name__ == '__main__':
	os.system("locust -f filetest.py --web-host='127.0.0.1'")