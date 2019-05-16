def print_line(char,times):
    """打印分割线

    :param char: 分割线使用的字符
    :param times: 分割线重复的次数
    """
    print(char * times)




def print_lines(char,times):

    line = 1
    while line <= 5:

        print_line(char,times)
        line += 1

print_lines("+",30)
