import pymysql,time
class Report:
	def __init__(self):
		pass
	# 求得mysql现有的行数
	def line(self):
		con=pymysql.connect('localhost', 'root','123456','woniucbt')
		cursor=con.cursor()
		sql='select count(id) from report'
		cursor.execute(sql)
		num=cursor.fetchone()[0]
		con.commit()
		cursor.close()
		return num

# mysql里面填充每次的测试结果
	def write_report(self,id,version,module,testtype,caseid,
			casetitle,result,screenshot,testtime,error=''):
		con=pymysql.connect('localhost', 'root','123456','woniucbt')
		cursor=con.cursor()
		screenshot=self.caonima(screenshot)
		sql='''insert into report(id,version,modle,testtype,caseid,
			casetitle,result,testtime,error,screenshot)
			values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');'''%\
			(id,version,module,testtype,caseid,casetitle,result,testtime,error,screenshot)
		# print(sql)
		cursor.execute(sql)
		con.commit()
		cursor.close()

# 对写入图片的MySQL的\\转义符的改变
	@staticmethod
	def caonima(c):
		a = ''
		for i in c:
			if i == '\\':
				a = a + '\\'+'\\'
			else:
				a = a + i
		return a
# 删除report表中所以数据，方便每次的测试
	def reset_table(self):
		con=pymysql.connect('localhost', 'root','123456','woniucbt')
		cursor=con.cursor()
		cursor.execute('truncate table report')
		con.commit()
		con.close()





if __name__=='__main__':
# #INSERT INTO `report` (`id`, `version`, `modle`) VALUES ('1', '2', '2')
# # 	# Report().write_report('9','2','2','2','2','2','2','2','2',)
	c=Report()
	c.write_report(29,'WoniuSales-20180508-V1.4','商品入库','GUI','tc_put_ingoods_2','商品入库失败用例','测试用例中途错误','C:\\Users\\Administrator\\PycharmProjects\\keywordTest\\screenshoot\\20191218_235438.png','2019-12-18 23:54:44','无效操作')