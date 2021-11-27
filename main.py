import create_excel
import create_word
#打印欢迎信息
print("欢迎使用")
#打印作者信息
print("作者：NoDream")
#打印版本信息
print("版本：0.0.3")
#打印更新时间
print("更新时间：2021-11-27")
#打印更新内容
print("更新内容：更改excel库为xlsxwriter")
#打印更新内容
print("更新内容：让excel文件能装下更多东西了")
#打印更新内容
print("更新内容：更新为xlsx文件")
print("")
choose = input("请选择导出类型：1.Excel 2.Word: ")
print("重新运行需要删除或移除Oj.xlsx文件")
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