# DESCity
一个自动生成拟合曲线的小项目

支持对多个 年 / 值 两列的excel表单进行自动读取，
使用DoubleExponentialSmoothing模型，自动生成图表： 
   年份必须连续
   首行不读取，暂时不支持识别excel表达式，所以需要转存成值
   默认damped_trend=True，可以在des.py中调整模型参数

des模块
  des函数：
    实现二次指数平滑的函数，可以改写成别的模型
  plot_results
    画图函数
output_result.py
    批量处理注册的表单，生成图表和拟合数据写入./result目录中
RegistSheet
    在这里要注册的表单，写入的是已经存储的表单的路径，建议表单存储路径为./repos
readexcel.py
    导入表单数据（需要先配置RegistSheet）

处理流程
  1 、表单数据调整到符合要求，放入./repos目录中
  2 、RegistSheet中写入想要处理的表单的路径
  3 、执行readexcel.py将表导入
  4 、执行output_result.py出图和数据

做的很简短，不过很多地方改起来很容易
只是大一数学建模的软件，
也许有人用的上？


