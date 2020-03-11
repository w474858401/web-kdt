import time,os,subprocess
from common.search import Findelement
from PIL import ImageFont,Image,ImageDraw
from pymouse import PyMouse
'''类中每次操作返回值caseture来确定操作成功执行'''
class zhoutiger:

	def __init__(self):
		self.find = Findelement()
		devices = subprocess.check_output('adb devices').decode()
		cc = devices.strip().split('\r\n')
		for i in range(1, len(cc)):
			self.udid = cc[i].split('\t')[0]#默认得到第一个手机设备的编号

# aap点击
	def click(self,how,waht):
		x,y=self.find.appelement(how,waht)
		os.system(f'adb -s {self.udid} shell input tap {x} {y}')
		return 'caseTrue'

# app元素检查用于断言
	def check(self,how,waht):
		try:
			x,y=self.find.appelement(how,waht)
			return 'caseTrue'
		except:
			return 'caseFalse'

# 退出打开的应用
	def close(self,how):
		os.system(f'adb shell am force-stop {how}')
		return 'caseTrue'
# 输入内容
	def input(self,how ,what,values):
		self.click(how,what)
		os.system(f'adb -s {self.udid} shell input tap {values}')
		return 'caseTrue'

	def screen(self):  # app截图
		now = time.strftime('%Y-%m-%d%H_%M_%S')
		png = now + '.png'
		os.system("adb shell screencap -p /sdcard/screen.png")
		os.system("adb pull /sdcard/screen.png ../screenshoot/%s" % png)
		source_path = '../screenshoot/%s' % png
		return source_path
# png图片地址 worderror写入文字
	def addword(self,png,worderror):
		# 设置字体
		font = ImageFont.truetype('D:\\lol\\华文细黑.ttf', 40)
		# 打开底版图片
		imageFile = png
		im1 = Image.open(imageFile)
		# 在图片上添加文字 1
		draw = ImageDraw.Draw(im1)    #^(0,255,0)为字体的颜色
		draw.text((0, 0), worderror, (0, 255, 0), font=font)
		draw = ImageDraw.Draw(im1)
		# 保存
		im1.save("{}".format(png))
	@staticmethod
	def start(self):
		PyMouse().click(91, 880)
		PyMouse().click(91, 880)


	def newweb(self):
		pass
if __name__=='__main__':
	zhoutiger().start()
	pass