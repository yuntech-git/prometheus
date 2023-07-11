import os
 def read_my_cnf():
    # 定义my.cnf文件的路径，根据实际情况进行修改
    my_cnf_path = "../mysql/my.cnf"
     try:
        # 尝试打开my.cnf文件
        with open(my_cnf_path, "r") as file:
            # 读取文件内容
            content = file.read()
            # 打印文件内容
            print(content)
    except FileNotFoundError:
        # 如果文件不存在或路径不正确，打印错误信息
        print("my.cnf文件不存在或路径不正确")
 if __name__ == "__main__":
    # 调用read_my_cnf函数
    read_my_cnf()