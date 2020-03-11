from selenium import webdriver
from selenium.webdriver.support.select import Select

class Mydriver:
	driver=None

	def __init__(self):
		pass
	# 单例流浪器默认是火狐
	@classmethod #浏览器单例
	def get_driver(cls,brower='Firefox'):
		if cls.driver==None:
			driver=getattr(webdriver,'{}'.format(brower))
			cls.driver=driver()
			cls.driver.maximize_window()
			cls.driver.implicitly_wait(4)
		return cls.driver

	@classmethod
	def get_app_driver(cls):
		pass
# 调用鼠标双击操作
	@staticmethod
	def double_click(driver,element):
		webdriver.ActionChains(driver).double_click(element).perform()

#下拉框的选择
	@staticmethod
	def selectt(element,positioin):
		Select(element).select_by_index(positioin)


if __name__=='__main__':
	pass