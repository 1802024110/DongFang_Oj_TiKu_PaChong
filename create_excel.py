import xlwt
import get_page_html
import get_answer
work_book = xlwt.Workbook()
"__init__(self, encoding='ascii', style_compression=0):"
# 默认编码 ASCII
work_sheet = work_book.add_sheet('题目')
def write_excel(row, col, value):
  for i in range(len(value)):
    work_sheet.write(row, col+i, value[i])
write_excel(0, 0, ['题号', '难度','题目', '题目描述', '输入','输出','样例输入' ,'样例输出','提示','来源','解析'])

def main():
  for item in range(1000,1005):
    # #循环所有题目
    try:
      work_sheet.write(item-999,0,item)
      #写入题号
      # #获取题目的描述
      describe = get_page_html.get_page_describe(item)
      work_sheet.write(item-999,3,describe)
      # #获取题目的输入
      input_data = get_page_html.get_page_input_text(item)
      work_sheet.write(item-999,4,input_data)
      # # #获取题目的输出
      output_data = get_page_html.get_page_output_text(item)
      work_sheet.write(item-999,5,output_data)
      # # #获取题目的提示
      tips = get_page_html.get_page_Tips(item)
      work_sheet.write(item-999,8,tips)
      # # #获取题目的来源
      source = get_page_html.get_page_source(item)
      work_sheet.write(item-999,9,source)
      # # #获取题目的解析
      analysis = get_answer.get_answer_text(item)
      work_sheet.write(item-999,9,analysis)
      # #获取题目的难度
      difficulty = get_page_html.get_difficulty(item)
      work_sheet.write(item-999,10,difficulty)
      # #获取题目的样例输入
      input_sample = get_page_html.get_page_Sample_input_text(item)
      work_sheet.write(item-999,6,input_sample)
      # #获取题目的样例输出
      output_sample = get_page_html.get_page_Sample_output_text(item)
      work_sheet.write(item-999,7,output_sample)
    except:
      print('题目'+str(item)+'获取失败')
  work_book.save('2.xls')
if __name__ == '__main__':
    main()
    