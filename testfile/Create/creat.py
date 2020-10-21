import os
import time
import datetime
def Creat_Folder(name):
	os.makedirs(name)	
New_Folder = input('请写出你需要创建的文件夹名（或者输入q退出）：')
while New_Folder=='q':
	break
else:
	Creat_Folder(New_Folder)
	print('文件夹已经创建成功'+New_Folder)

end_time=datetime.datetime.now()
end_times=end_time.strftime('%Y-%m-%d %H:%M:%S')
satrt_time=end_time-datetime.timedelta(days=8)
satrt_times=satrt_time.strftime('%Y-%m-%d %H:%M:%S')

def Creat_file(name):
	file=open(name,'w')
	with open(name,'a') as file_object:
		file_object.write('#'+str(end_times))
New_filename = input('请写出你需要创建文件的名字（输入q退出）：')
while New_filename=='q':
	break
else:
	Creat_file(New_filename)
	print('文件创建成功'+New_filename)
