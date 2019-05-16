name_list = ["zhangsan","lisi","wangwu"]
#1.取值和取索引
print(name_list[0])
print(name_list.index("lisi"))

#2.修改
name_list[0] = "李四"
print(name_list)

#3.添加数据
#append方法可以向列表末尾追加数据
name_list.append("王狗蛋")
print(name_list)

#insert方法可以在列表指定的索引位置增加数据
name_list.insert(3,"郁郁寡欢")
print(name_list)

#extend方法可以把另外一个列表中的完整数据追加到当前列表的末尾
temp_list = ["孙悟空","猪八戒","沙和尚"]
name_list.extend(temp_list)

print(name_list)
print(name_list.index("孙悟空"))
name_list.insert(2,"大雕烧")
print(name_list)

#删除
#1.remove方法可以从列表中删除指定的数据
name_list.remove("wangwu")
print(name_list)
#2.pop方法可以删除列表最后一个数据,也可以指定索引删除数据
#name_list.pop()
#print(name_list)
name_list.pop(0)
print(name_list)
#3.clear可以清空整个列表
#name_list.clear()
#print(name_list)

#4.del关键字本质上是用来将一个变量从内存中删除
del name_list[1]
print(name_list)