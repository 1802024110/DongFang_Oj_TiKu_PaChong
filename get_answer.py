import requests as req
#引入requests模块
import re #引入正则表达式
from lxml import etree
session = req.session()
#实例化session，保持登录状态

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
  print(html)
  if html == 200:
    return True
  else:
    return False
  #发送登录请求
def get_page_html(index_page):
  '''
    获得题目的html文本
    成功获取返回html文本
    失败返回Not this page
  '''
  url = f'https://oj.czos.cn/p/{index_page}'
  #依次请求请求题目
  html = session.get(url)
  html.encoding = 'utf-8'
  if ( html.status_code == 404) : return 'Not this page'
  html.encoding = 'utf-8'
  html = html.text
  # #将html中所有换行删除
  html = html.replace('\n','')
  # #将html中所有<br>删除
  html = html.replace('\r','\n')
  return html
def get_page_html_lxml(index_page):
  '''
    获得网页的html的lxml格式文本
  '''
  html = get_page_html(index_page)
  #将html文本转换为lxml格式
  html = etree.HTML(html)
  return html
def get_answer_url(index_page):
  '''
    获得题目的url
  '''
  html = get_page_html(index_page)
  #获取题目的url
  try:
    url = re.findall('<a class="btn btn-default" href="(.*?)"><span class="glyphicon glyphicon-comment"></span> 题解</a>',html)[0]
  except:
    print('你还没做,没有题解')
    return False
  url = url.replace('amp;','')
  #获取题目的url
  return 'https://oj.czos.cn'+url
def get_answer_list(index_page):
  html = session.get(get_answer_url(index_page)).text
  return html
def get_answer_list_url(index_page):
  html = get_answer_list(index_page)
  #获取题解的url
  try:
    url_islt = re.findall('<a class="thread-title" href="(.*?)">.{0,}',html)[0]
    #去除元素中的空格
    url_islt = 'https://oj.czos.cn'+url_islt.replace('amp;','')
    return url_islt
  except:
    print('没有题解')
    return False
def get_answer_text(index_page):
  '''
    获取真正题解
  '''
  html = session.get(get_answer_list_url(index_page)).text
  #lxml匹配class="thread-content"
  html = etree.HTML(html)
  try:
    text = html.xpath('//div[@class="markdown"]')
    #获取题解的文本
    text = etree.tostring(text[0],encoding='utf-8').decode('utf-8')
    text = text.replace('</p>','\n')
    #将lxml格式转换为html文本
    text = re.sub('<.*?>','',text)
    #去除html标签
    text = text.replace('&lt;','<')
    text = text.replace('&gt;','>')
    return text
  except:
    print('没有题解')
    return False
def main():
  login('tyh','030706')
  for i in range(1000,1190):
    if (get_page_html(i) == 'Not this page' or get_answer_url(i) == False): continue
    print('第',i,'题')
    print(get_answer_text(i))
if __name__ == '__main__':
  main()
    