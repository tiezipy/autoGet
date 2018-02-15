import requests
from bs4 import BeautifulSoup


#制作lushu'an的数据
def makeLu(html_doc):
	soup=BeautifulSoup(html_doc,'html.parser')
	Lu_list=soup.find(id="######").parent
	data=[]

	for i in Lu_list:
		data.append(i.string)
		
	LU_str="啊啊啊:\n资产净值：%s \n已用按金：%s \n可用按金：%s  \n按金比例：%s " % (data[-8],data[-6],data[-4],data[-2])
    #写到一个文件中
	f = open('lushuan.txt','w',encoding='utf-8')
	f.write(LU_str)


#登录
def login(baseurl,account,pwd):
	login_data={'account':account,'pwd':pwd}
	#使用session登录
	session=requests.session()
	baseurl += '/Manager/'
	content=session.post(baseurl,data=login_data)
	s=session.get('#######', verify=False)
    
	return s.text

if __name__ =="__main__":
    url = '#######'
    file=login(url,'######','######')
    makeLu(file)
    