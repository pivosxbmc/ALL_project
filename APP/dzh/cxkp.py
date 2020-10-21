import sys
sys.path.append('E:/Teacher/Imooc/AppiumPython')
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def get_driver():
	capabilities = {
	 	"platformName": "Android",
	 	"automationName":"UiAutomator2",
	 	#"deviceName": "6a3b720d",
	 	"deviceName": "6a3b720d",
	 	"platformVersion":"8.0.0",
	 	"appPackage":"com.txt.gxrb",
	 	#"app": "E:\\PythonAppium\\AutoTestAppium\\apps\\mukewang.apk",
	 	"appWaitActivity":"com.txt.rbb.ui.login.SplashActivity",
	 	'androidDeviceReadyTimeout':'20',
	 	'unicondeKeyboard':True,
	 	'resetKeyboard':True
	 	#"noReset":"true"
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
#get_driver()
import os
def print_directory_contents(sPath):                                      
   for sChild in os.listdir(sPath):         
       sChildPath = os.path.join(sPath,sChild)
       if os.path.isdir(sChildPath):
           print_directory_contents(sChildPath)
       else:
           print(sChildPath)

print_directory_contents('D:\jx\APP')

