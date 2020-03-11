from lib.keyapp import zhoutiger
from lib.keyweb import Robot
import time
from report.woniusalesreport import Report
from run.htmlreport import Htmlreport

class Dotest:
	def __init__(self):
		pass

# 一次性读取所以文件内容，生成三维列表。
	def datamark(self,file):
		f=open(file,'r',encoding='UTF-8')
		lines=f.readlines()
		listmid=[]
		listmax=[]
		listtitle=[]
		for line in lines:
			li=self.__killaiir(line)
			listmin=[]
			if  li[:3]=='tc_' or li[:3]=='tb_':
				listtitle.append(li.split(':')[0])
				listmid=[]
				listmax.append(listmid)
			elif li[0]=='s':
				chair=li.index(':')
				word=li[chair+1:].split(',')
				for i in word:
					if i=='\n':
						listmin.append('')
						pass
					else:
						c=i.split()[0]
						listmin.append(c)
				listmid.append(listmin)
		print(listmax,listtitle)
		return listmax,listtitle

# 调度运行
	def walk(self,file):
		bigbox=[]
		listmax,listtitel=self.datamark(file)
		for i in range(len(listtitel)):
			listmid=listmax[i]
			title=listtitel[i].split('\n')[0]
			cat=''
			if 'tc_' in title:
				monkey = Robot()
			elif 'tb_' in title:
				monkey = zhoutiger()
				Robot().closedriver()
			else:
				break
			for listmin in listmid:
				keyword = listmin[0]
				nothing = listmin[1:]
				result=''
				try:
					step= getattr(monkey, keyword)
					result = step(*nothing)  # 每个用例最后一步是check，
					print(result)
					print(monkey)
				except Exception as hello_bug:
					result = 'caseFalse'
					word = str(hello_bug)
					cat = monkey.screen()
					monkey.addword(cat, word)
					break
			rest=self.equl(cat,result,title)
			content = title + '$' + rest + '&' + cat#结束后把断言结果，标题，截图合在一起
			bigbox.append(content)
			time.sleep(1)
			monkey.newweb()

# 断言
	def equl(self,cat,result,title):
		rest='测试用例通过'
		if cat!='':
			rest='测试用例中途错误'
		else:
			if 'False'in result and '失败'in title:
				rest = '测试用例通过'
			elif 'False'in result and '成功'in title:
				rest = '测试用例没有通过'
			elif 'True'in result and '失败'in title:
				rest='测试用例没有通过'
			elif 'True' in result and '成功'in title:
				rest='测试用例通过'
				# print(333333333)
			else:
				rest = '测试用例没有通过'
				# print(44444)

		return rest

# 数据转换mysql的数据
	def mather(self,cattail):
		math=Report()
		data=[]
		datas=[]
		id=Report().line()
		for i in range(len(cattail)):
			id+=1
			num=cattail[i].index('#')
			num1=cattail[i].index('$')
			num2=cattail[i].index('&')
			version='WoniuSales-20180508-V1.4'
			module=cattail[i][num+1:num+5]
			testtype='GUI'
			caseid=cattail[i][:num]
			casetitle=cattail[i][num+1:num1]
			result=cattail[i][num1+1:num2]
			if cattail[i][num2+1:]!='0':
				screenshot=cattail[i][num2+1:]
			else:
				screenshot=''
			if '没有' in result:
				error = '断言失败'
			elif '错误'in result:
				error='无效操作'
			else:
				error=''
			id=int(id)
			testtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			data=[id,version,module,testtype,caseid,casetitle,result,screenshot,testtime,error]
			datas.append(data)
		return datas

# 去空行防止测试用例出现空行
	def __killaiir(self,line):
		li = ''
		for i in range(len(line)):
			if line[i] == ' ':
				pass
			else:
				li = li + line[i]
		return li

if __name__=='__main__':
	c=Dotest()
	datas=c.walk('..\\datayum\\aa.txt')
	de=Htmlreport()
	de.gener_html('WoniuSales-20180508-V1.4')

