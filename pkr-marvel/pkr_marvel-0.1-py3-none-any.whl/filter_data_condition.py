def filter_data():
    print("Enter no of characters you want to look for based on character starting letter")
    n= int(input())
    lst=[]
    print("Enter the characters one by one")
    for i in range(0, n):
        ele = str(input())
        lst.append(ele)
    return lst