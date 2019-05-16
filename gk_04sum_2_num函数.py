def sum_2_num():
    """对两个数字的求和"""

    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    result = num1 + num2
    print("%d + %d = %d" %(num1,num2,result))





def sum_3_num(num1,num2,num3):


    result1 = num1 + num2 +num3

    print("%.2f + %.2f + %.2f = %.2f" % (num1,num2,num3,result1))

print(sum_3_num(30,80,115.5))
