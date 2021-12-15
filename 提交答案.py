import requests as req
import get_answer as da
import re
da.login('tyh','030706')
答案 = da.get_answer_text(1322)
答案 = re.sub(r'[^\x00-\x7F]+',' ', 答案)

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
# 获得题目提交的
print(答案)
# 获得题目的csrf
def getCsrf(page):
  url = 'https://oj.czos.cn/p/'+page
  html = req.get(url).text
  csrf = html

# 提交的数据
data = {
  '_csrf': 'xpFdRBdhGsEi6wvcAlfmO5Dy7r4uX8t_XaotCUo7HhSWy241XTtCo26fWLg6CK8P85qHzkcbniwT_kxqfm4sIw==',
'Solution[language]': '0',
'Solution[source]': 答案
}
