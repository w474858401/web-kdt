import os
import time
import pymysql


class Htmlreport:

	def gener_html(self,version):
		conn=pymysql.connect('localhost', 'root','123456','woniucbt')
		cursor=conn.cursor()
		sql="select * from report where version='%s'"%version
		cursor.execute(sql)
		results=cursor.fetchall()
		tempate_path=os.path.abspath('..')+'\\report\\template.html'
		tempate=open(tempate_path,'r',encoding='UTF-8')
		content=tempate.read()
		version=results[0][1]
		content=content.replace('$test-version',version)
		sql_base="select count(*) from report where version="
		sql_pass=sql_base+"'%s' and result='测试用例通过'"%version
		cursor.execute(sql_pass)
		pass_count=cursor.fetchone()[0]
		content=content.replace("$test-pass-count",str(pass_count))
		sql_fail=sql_base+"'%s' and result='测试用例没有通过'"%version
		cursor.execute(sql_fail)
		fail_count=cursor.fetchone()[0]
		content=content.replace("$fail-count",str(fail_count))
		sql_error=sql_base+"'%s' and result='错误'"%version
		cursor.execute(sql_error)
		error_count=cursor.fetchone()[0]
		content=content.replace("$error-count",str(error_count))
		sql_last="select testtime from report where version='%s' order by id desc limit 0,1" % version
		cursor.execute(sql_last)
		last_time=cursor.fetchone()[0]
		content=content.replace("$last-time",str(last_time))
		content=content.replace("$test-date",str(last_time))
		test_result=''
		for record in results:
			test_result+="<tr height='40'>"
			test_result+="<td width=7%'>"+str(record[0])+"</td>"
			test_result+="<td width='9%'>"+record[2]+"</a></td>"
			test_result+="<td width='9%'>"+record[3]+"</td>"
			test_result+="<td width='7%'>"+record[4]+"</td>"
			test_result+="<td width='20%'>"+record[5]+"</td>"
			if record[6]=='测试用例通过':
				test_result+="<td width=7% bgcolor='lightgreen'>"+record[6]+"</td>"
			elif record[6]=='测试用例没有通过':
				test_result+="<td width=7% bgcolor='red'>"+record[6]+"</td>"
			elif record[6]=='测试用例中途错误':
				test_result+="<td width=7% bgcolor='yellow'>"+record[6]+"</td>"
			test_result+="<td width=16%>"+str(record[7])+"</td>"
			test_result+="<td width=15%>"+record[8]+"</td>"
			if record[9]=='':
				test_result+="<td width=10%>"+record[9]+"</td>"
			else:
				test_result+="<td width='10%'><a href='{}'>查看截图</a></td>".format(record[9])
			test_result+="</tr>\r\n"
		content=content.replace("$test-result",test_result)
		nowtime=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
		report_path = os.path.abspath('..') + '\\report\\'+nowtime+'cbt.html'
		report= open(report_path,'w', encoding='UTF-8')
		report.write(content)
		report.close()
		cursor.close()
		conn.close()


if __name__=='__main__':
	de=Htmlreport()
