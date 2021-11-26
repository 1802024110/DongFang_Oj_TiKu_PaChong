import xlwt
import get_page_html
work_book = xlwt.Workbook()
"__init__(self, encoding='ascii', style_compression=0):"
# 默认编码 ASCII
work_sheet = work_book.add_sheet('题目')
def write_excel(row, col, value):
  for i in range(len(value)):
    work_sheet.write(row, col+i, value[i])
write_excel(0, 0, ['题号', '难度','题目', '题目描述', '输入','样例输入' ,'样例输出','提示','来源','解析'])

def main():
  for item in range(1000,1005):
    # #循环所有题目
    try:
      # #获取题目的描述
      describe = get_page_html.get_page_describe(item)
      print(item-999,0,describe)
      write_excel(item-999,0,"describe")
      # # #获取题目的输入
      # input_data = get_answer.get_input(item)
      # # #获取题目的输出
      # output_data = get_answer.get_output(item)
      # # #获取题目的提示
      # hint = get_answer.get_hint(item)
      # # #获取题目的来源
      # source = get_answer.get_source(item)
      # # #获取题目的解析
      # analysis = get_answer.get_analysis(item)
      # # #获取题目的难度
      # difficulty = get_answer.get_difficulty(item)
      # # #获取题目的样例输入
      # input_sample = get_answer.get_input_sample(item)
      # # #获取题目的样例输出
      # output_sample = get_answer.get_output_sample(item)
    except:
      print('题目'+str(item)+'获取失败')
  work_book.save('2.xls')
if __name__ == '__main__':
    main()
    