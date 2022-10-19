import os


def show_4_item(menu_id):

    new_menu_list = [f"菜单{i}" for i in range(1, 8 + 1)]
    menu_id = menu_id % 8
    if menu_id == 0:  # 如果是8的整倍数
        menu_id = 8

    new_menu_list[menu_id - 1] += "<-"

    if menu_id > 4:  # 如果菜单项大于4，一定在第2页
        l = new_menu_list[4:]  # 第二页
    else:
        l = new_menu_list[:4]  # 第一页
    os.system("cls")  # windows 清空控制台

    print("\n".join(l), flush=True)


menu_id = 81

while True:
    show_4_item(menu_id)
    cmd = input("请输入指令（w向上，s向下，其他退出）:")
    if cmd.lower() == "w":
        menu_id -= 1

    elif cmd.lower() == "s":
        menu_id += 1
    else:
        print("bey~")
        break
