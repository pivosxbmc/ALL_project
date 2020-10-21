#from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()
#device.installPackage('F:\\MyDownloads\\rbassessB-v1.0.0-1912301355-release.apk')
device.startActivity(component='com.txt.rbe/com.txt.rbb.rbe.ui.login.SplashActivity')

#录制
