import os,time
import cv2 as cv
from lxml import  etree
from time import sleep

class Findelement:
	def __init__(self):
		# self.path='D:\\lol'
		pass
# web元素找定位，设置默认等待时间为3秒
	def find_element(self,driver,how,what,timeout=3):
		find=getattr(driver,'find_element_by_{}'.format(how))
		try:
			for i in range(timeout):
				element=find(what)
				return element
		except:
			sleep(1)
		return None


#app的xml文件的元素定位查元素
	def appelements(self,how,what):
		os.system('adb shell uiautomator dump')
		os.system('adb pull /storage/emulated/legacy/window_dump.xml D:\\lol')#获得xml文件
		tree = etree.parse("D:\\lol\\window_dump.xml")
		if how!='appxpath':
			node_list=tree.xpath("//node[@{}='{}']".format(how,what))
		elif how=='appxpath':
			try:
				node_list=tree.xpath(what)
			except Exception:
				node_list=''
		if len(node_list)>0:
			bounds=node_list[0].get('bounds')
			bounds = bounds.replace('][', ',')
			bounds = eval(bounds)
			x = int((bounds[0] + bounds[2]) / 2)
			y = int((bounds[1] + bounds[3]) / 2)
			return [x,y]
		else:
			return [-1,-1]

#类似隐时等待时间设置，找到xml中的元素
	def appelement(self,how,what):
		list=[]
		for i in range(4):
			list=self.appelements(how,what)
			if list==[-1,-1]:
				sleep(1)
			else:
				return list

	# 通过图片对比找出app坐标定位
	def find_image(self,image,like=0.8):
		testtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		os.system('adb shell /system/bin/screencap -p /sdcard/{}.png'.format(testtime))
		os.system('adb pull /sdcard/{}.png D:\\lol'.format(testtime))
		source=cv.imread('D:\\lol'.format(testtime))
		try:
			tem=cv.imread(image)
			result=cv.matchTemplate(source,tem,cv.TM_CCOEFF_NORMED)
			pos=cv.minMaxLoc(result)[3]
			x=int(pos[0])+int(tem.sharpe[1]/2)
			y=int(pos[1])+int(tem.sharpe[0]/2)
			similarity=cv.minMaxLoc(result)[1]
			if similarity>like:
				return (x,y)
			else:
				return (-1,-1)
		except:
			return (-1,-1)


if __name__=='__main__':
	pass


