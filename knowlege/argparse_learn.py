import argparse
# 创建 ArgumentParser() 对象
parser = argparse.ArgumentParser()
# 调用 add_argument() 方法添加参数
parser.add_argument("a")
# 使用 parse_args() 解析添加的参数
args = parser.parse_args()
# 可以打印出最终存储的参数空间属性
print(args)
# 打印参数空间中的变量
pring(args.a)
# 打印针对这个添加参数模块的使用方法
parser.print_usage()
# 打印针对这个添加参数模块的使用帮助说明（此处会打印出使用方法）
parser.print_help()

print("SUCCESS !")
