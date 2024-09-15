#Bài 5: Viết chương trình in ra bảng cửu chương từ 2 đến 9.
# number = int(input("Bang cuu chuong: "))

# if number< 2 or number >9:
#     print(" Error")
# else:
#     for i in range (2,10):
#         print(f"{number} x {i} = {number*i}")
list_1 =[2,3,4,5,6,7,8,9]
list_2 =[1,2,3,4,5,6,7,8,9,10]
for i in list_1:
    for j in list_2:
        print(f"{i} x {j} = {i*j}")
        