
a = 'a'
while True:
    a = input("请输入(q or Q exist.)：")
    #print(type(a))
    if (a != 'q' and a != 'Q'):
        print("十进制: ", int(a))
        print("二进制: ",bin(int(a)))
    else:
        break


    





