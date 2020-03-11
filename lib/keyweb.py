from common.mydriver import Mydriver
from common.search import Findelement
import time,os
from PIL import ImageFont,Image,ImageDraw

class Robot:
	def __init__(self):
		self.driver=Mydriver().get_driver()
		self.find=Findelement()
# 上网点击网址
	def open(self,url):
		self.driver.get(url)
# 点击
	def click(self,how,what):
		self.find.find_element(self.driver,how,what).click()
		return 'caseTrue'
# 发送
	def send(self,how,what,values):
		self.find.find_element(self.driver, how, what).send_keys(values)
		return 'caseTrue'


#清空重新书写内容发送
	def send1(self,how,what,values):
		self.clear(how,what)
		self.send(how,what,values)
		return 'caseTrue'

# 选择
	def select(self,how,what,values):
		element=self.find.find_element(self.driver,how,what)
		Mydriver.selectt(element,values)
		return 'caseTrue'

# 双击
	def double_click(self,how,what):
		element=self.find.find_element(self.driver, how, what)
		Mydriver.double_click(self.driver, element)
		return 'caseTrue'

# 查找元素断言,元素纯在给值caseture
	def check_exsit(self,how,what):
		self.find.find_element(self.driver, how, what)
		return 'caseTrue'

#关浏览器
	def closedriver(self):
		self.driver.close()
#清屏
	def clear(self,how,what):
		self.find.find_element(self.driver, how, what).clear()

#刷新页面
	def newweb(self):
		self.driver.refresh()
		try:
			self.click('link_text', '注销')
		except:
			pass

#文本内容断言
	def check_text(self,how,what,values):
		connent=self.find.find_element(self.driver, how, what).text
		# print(connent)
		if values in connent:
			return 'caseTrue'
		else:
			return 'caseFalse'
#截图
	def screen(self):
		image_name=time.strftime('%Y%m%d_%H%M%S')
		tempate=os.path.abspath('..')+'\\screenshoot\\'
		filename=tempate+image_name+'.png'
		self.driver.get_screenshot_as_file(filename)
		name='../screenshoot/'+image_name+'.png'
		return name

#弹窗捕捉
	def alert(self,choice=1):
		if choice!=1:
			self.driver.switch_to.alert.dismiss()
		else:
			self.driver.switch_to.alert.accept()
		return 'caseTrue'

# png图片地址 worderror写入文字
	def addword(self,png,worderror):
		# 设置字体，如果没有，也可以不设置
		font = ImageFont.truetype('D:\\lol\\华文细黑.ttf', 40)
		color = "#000000"
		# 打开底版图片
		imageFile = png
		im1 = Image.open(imageFile)
		# 在图片上添加文字 1
		draw = ImageDraw.Draw(im1)
		draw.text((0, 0), worderror, (0, 0, 0), font=font)
		draw = ImageDraw.Draw(im1)
		# 保存
		im1.save("{}".format(png))

if __name__=='__main__':
	dd=Robot()
	dd.open('https://www.baidu.com/')
	dc=dd.screen()
	print(dc)


