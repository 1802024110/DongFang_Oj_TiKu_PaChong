import create_excel
import create_word

choose = input("请选择导出类型：1.Excel 2.Word: ")
if choose == "1":
  start = input("请输入起始题号：")
  end = input("请输入结束题号：")
  username = input("请输入用户名：")
  password = input("请输入密码：")
  create_excel.create(int(start),int(end),str(username),str(password))
  '''
    生成Excel表格
    参数说明：
    1. 开始的题号
    2. 结束的题号
    3. 用户名(可选)，用于获得题解
    4. 密码(可选)，用于获得题解
  '''
elif choose == "2":
  start = input("请输入起始题号：")
  end = input("请输入结束题号：")
  username = input("请输入用户名：")
  password = input("请输入密码：")
  create_word.create(int(start),int(end),str(username),str(password))
  '''
    生成Word表格
    参数说明：
    1. 开始的题号
    2. 结束的题号
    3. 用户名(可选)，用于获得题解
    4. 密码(可选)，用于获得题解
  '''