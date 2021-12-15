import requests as req
import get_answer as da
from lxml import etree
import time
import re
# 自己账号session
session = req.session()
def login(username,password):
  '''
    输入用户名密码登录
    成功True
    失败False
  '''
  url = 'https://oj.czos.cn/site/login'
  #登录页面

  #登录信息
  html_before_login = session.get('https://oj.czos.cn/site/signup').text
  #获取登录前的页面,拿到csrf
  csrf = re.findall('<input type="hidden" name="_csrf" value="(.*?)">',html_before_login)[0]

  data = {
    '_csrf': csrf,
  'LoginForm[username]': username,
  'LoginForm[password]': password,
  'LoginForm[rememberMe]': '0',
  'login-button': ''
  }
  html = session.post(url,data=data).status_code
  if html == 200:
    return True
  else:
    return False
  #发送登录请求
# 获得题目的csrf
def getCsrf(page):
  url = 'https://oj.czos.cn/p/'+str(page)
  html = session.get(url).text
  #html转为lxml格式
  html = etree.HTML(html)
  #获得csrf
  csrf = html.xpath('//input[@name="_csrf"]/@value')[0]
  return csrf
# 提交答案
def submitAnswer(page,answer,csrf):
  data = {
  '_csrf': csrf,
  'Solution[language]': '1',
  'Solution[source]': answer
  }
  headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Host': 'oj.czos.cn',
  'Origin': 'https://oj.czos.cn',
  'Referer': 'https://oj.czos.cn/p/'+str(page),
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
  }
  session.post('https://oj.czos.cn/p/'+str(page),headers=headers,data=data)
  print(csrf,'\n',page,'\n',answer)
if __name__ == '__main__':
  """ 
    入口在这里
    报什么错误就报什么错误，安装对应的包
    pythonVersion: 3.7
    佛祖保佑，永无BUG
    有一部分没有解析，可能是解析的问题，没有解析的问题，可以自己去查找
  """
  da.login('tyh','030706')
  # 对方账号
  login('1802024110','2002zengyuan')
  # 我方账号
  for item in range(1000,2315):
    # 起始题号
    try:
      submitAnswer(item,da.get_answer_text(item),getCsrf(item))
      time.sleep(10)
      # 减速保命
    except:
      print('这题'+item+'出错了')
      continue