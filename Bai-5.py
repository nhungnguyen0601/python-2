#Bài 5: Viết chương trình in ra bảng cửu chương từ 2 đến 9.
number = int(input("Bang cuu chuong: "))

if number< 2 or number >9:
    print(" Error")
else:
    for i in range (1,11):
        print(f"{number} x {i} = {number*i}")
        # print("{} x {}={}".format(number, i, number*i))

#list =[[1,2], [2,3]]

# list_1 =[2,3,4,5,6,7,8,9]
# list_2 =[1,2,3,4,5,6,7,8,9,10]
# for i in list_1:
#     for j in list_2:
#         print(f"{i} x {j} = {i*j}")
        