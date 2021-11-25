import requests as req
#引入requests模块
import re #引入正则表达式
from lxml import etree

def get_page_html(index_page):
  '''
    获得题目的html文本
    成功获取返回html文本
    失败返回Not this page
  '''
  url = f'https://oj.czos.cn/p/{index_page}'
  #依次请求请求题目
  html = req.get(url)
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
def get_page_title(index_page):
  '''
    获得题目的标题
  '''
  regular_expression = re.compile(r'  <h3><b>.*? - 【.*】(.*)</b></h3>')
  try:
    title = regular_expression.findall(get_page_html(index_page))[0]
    return title
  except:
    return str(index_page) + ' 标题未获取到'
def get_page_difficulty(index_page):
  '''
    获得题目的难度
  '''
  regular_expression = re.compile(r' <h3><b>.*? - 【(.*)】.*</b></h3>')
  try:
    difficulty = regular_expression.findall(get_page_html(index_page))[0]
    return difficulty
  except:
    return str(index_page) + ' 难度未获取到'
def get_page_describe(index_page):
  '''
    获得题目的描述
  '''
  all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[0].xpath('string(.)')
  all_list = [i for i in all_list if i != ' ']
  all_list = ''.join(all_list)
  try:
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目描述未获取到'
def get_page_input_text(index_page):
  '''
    获得题目的输入 描述
  '''
  all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[1]
  all_list = all_list.xpath('string(.)')
  all_list = [i for i in all_list if i != ' ']
  all_list = ''.join(all_list)
  #去除数组的空元素
  try:
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目输入描述未获取到'
def get_page_output_text(index_page):
  '''
    获得题目的输出 描述
  '''
  try:
    all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[2]
    all_list = all_list.xpath('string(.)')
    all_list = [i for i in all_list if i != ' ']
    all_list = ''.join(all_list)
    #去除数组的空元素
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目输出描述未获取到'
def get_page_Sample_input_text(index_page):
  '''
    获得题目的样例输入 
  '''
  try:
    all_list = get_page_html_lxml(index_page).xpath('//div[@class="sample-test"]/div[@class="input"]/pre//text()')[0]
    # all_list = ''.join(all_list)
    #去除数组的空元素
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目样例输入未获取到或无样例'
def get_page_Sample_output_text(index_page):
  '''
    获得题目的样例输出
  '''
  try:
    all_list = get_page_html_lxml(index_page).xpath('//div[@class="sample-test"]/div[@class="output"]/pre//text()')[0]
    # all_list = ''.join(all_list)
    #去除数组的空元素
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目样例输出未获取到或无样例'
def get_page_Tips(index_page):
  '''
    获得题目的提示
  '''
  try:
    title_list = get_page_html_lxml(index_page).xpath('//div[@class="content-header"]')[4]
    title_list = title_list.xpath('string(.)')
    title_list = [i for i in title_list if i != ' ']
    title_list = ''.join(title_list)
    if (title_list == '提示'):
      all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[3]
      all_list = all_list.xpath('string(.)')
      all_list = [i for i in all_list if i != ' ']
      #去除数组的空元素
      all_list = ''.join(all_list)
      describe = all_list
      return describe
    else:
      return '该题没提示，自己想'
  except:
    return str(index_page) + ' 题目输出描述未获取到'
def get_page_source(index_page):
  '''
    获得题目的来源
  '''
  try:
    title_list = get_page_html_lxml(index_page).xpath('//div[@class="content-header"]')[4]
    title_list = title_list.xpath('string(.)')
    title_list = [i for i in title_list if i != ' ']
    title_list = ''.join(title_list)
    if (title_list == '提示'):
      all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[4]
    else:
      all_list = get_page_html_lxml(index_page).xpath('//div[@class="markdown"]')[3]
    all_list = all_list.xpath('string(.)')
    all_list = [i for i in all_list if i != ' ']
    #去除数组的空元素
    all_list = ''.join(all_list)
    describe = all_list
    return describe
  except:
    return str(index_page) + ' 题目输出描述未获取到'
def main():
  for i in range(1000,2253):
    # #循环所有题目
    if(get_page_html(i) == 'Not this page'): continue
    print(get_page_source(i),'\n')
if __name__ == '__main__':
    main()