"""
@Project:pymysql
@File:Model.py
@Author:函封封
@Date:9:23
"""

from pathlib import Path
import pymysql

# mysql操作
class Model():
    def __init__(self,database=None,user=None,password=None,host="localhost",port=3306,charset="utf8"):
        try:
            if not all([database, user, password, host, port, charset]):
                # BASE_DIR = Path(__file__).resolve().parent
                print("连接数据库失败！")
                print("ToDo 读取配置文件")
                self.pymysql_con = None
            else:

                self.pymysql_con = pymysql.connect(database=database, user=user, password=str(password), host=host,port=port, charset=charset)
            self.mysql = self.pymysql_con.cursor() # 创建游标对象
            self.table_name = None  # 表名
            self.field = ["id",]  # 表字段
        except Exception as e:
            print("连接数据库失败！")
            print("错误信息：",e)
        else:
            print("连接数据库成功！")

    # 获取数据库内所有的表
    def show_tables(self):
        try:
            sql = f"""show tables;"""
            self.mysql.execute(sql)
        except Exception as e:
            print("查询表失败！")
            print("错误信息：", e)
        else:
            data = self.mysql.fetchall()
            table_list = []
            for i in data:   # 元组转换为列表
                table_list.append(i[0])
            return table_list # 返回当前数据库内所有的表



    # 连接表 接收一个字符串类型的表名
    def link_table(self, table_name=None, field=None):
        try:
            self.table_name = table_name  # 将表名赋值给实例属性
            field_str = ""
            for i in field:
                field_str += i + ","  # 将所有的字段与字段类型以 “ , ” 拼接
                field_name = i.split()[0]  # 获取所有的字段名，不含字段类型
                self.field.append(field_name)  # 获取该表的所有的字段名

            table_list = self.show_tables()  # 获取数据库里所有的表
            for i in table_list:
                if self.table_name == i:  # 判断该表是否已存在
                    print(f"——连接 {self.table_name} 成功！——")
                    return True # 该表已存在！直接返回

            field_str = field_str.rstrip(",")  # 删除字符串最后的“,”
            sql = f"""
                 create table {self.table_name}(
                    id int primary key auto_increment,
                    {field_str}
                  );
             """
            self.mysql.execute(sql)

        except Exception as e:
            print("***连接失败***")
            print("错误信息：", e)
            return False
        else:
            print(f"——创建并连接 {self.table_name} 成功！——")
            return True

    # 查询数据
    def all(self):
        try:
            sql = f"""select * from {self.table_name};""" # 根据表名直接查询
            self.mysql.execute(sql)
        except Exception as e:
            print("查询失败！")
            print("错误信息：", e)
        else:
            data = self.mysql.fetchall()
            data_list = []
            for i in data:  # 进行数据转换
                data_dict = {}
                for k,j in enumerate(self.field):# 每行数据 组成字典类型
                    data_dict[j] = i[k]
                data_list.append(data_dict)

            return data_list # 最终返回查询集

    # 添加数据     接收所有的命名参数 即根据字段名传入对应数据
    def create(self,**kwargs):
        try:
            create_data = ""
            for i in self.field:
                if i == "id": # id 字段跳过
                    continue
                try:
                    if not kwargs[i]: # 传入的改字段值为空
                        print("错误信息：",i,"字段为空")
                        return False
                except Exception: # 异常时缺少字段
                    print("字段不全！")
                    return False
                if isinstance(kwargs[i], str): # 判断类型 为字符串 需加引号
                    create_data += f"'{kwargs[i]}',"
                else:
                    create_data += f"{kwargs[i]},"
            field_str = create_data.rstrip(",") # 删除字符最后的“,”
            # id 字段为null ，默认自增
            sql = f"""
                insert into {self.table_name} values 
                (null ,{field_str});
            """
            self.mysql.execute(sql)
        except Exception as e:
            self.pymysql_con.rollback()
            print("添加失败！")
            print("错误信息：", e)
            return False
        else:
            self.pymysql_con.commit()
            print("添加成功！")
            return True

    # 修改数据    接收所有的命名参数 即根据字段名传入对应数据
    def update(self,**kwargs):
        try:
            update_str = ""
            for i in self.field:
                try:
                    if not kwargs[i]:  # 传入字段值参数为空 警告  字段值为空则不做修改
                        print("警告：", i, "传入该字段值为空，则该字段不做修改！")
                        continue
                except Exception:  # 缺少字段，该字段也不做修改
                    print("提示：", i, "该字段没有传入参数，则该字段不做修改！")
                    continue
                if isinstance(kwargs[i],str):
                    update_str += f"{i}='{kwargs[i]}',"
                else:
                    update_str += f"{i}={kwargs[i]},"

            field_str = update_str.rstrip(",")  # 删除字符最后的“,”
            # 根据传入id 进行修改数据 若没有传入id 则报错 修改失败
            sql = f"""
                    update {self.table_name} set {field_str} where id = {kwargs["id"]};
                """
            self.mysql.execute(sql)
        except Exception as e:
            self.pymysql_con.rollback()
            print("修改失败！")
            print("错误信息：", e)
            return False
        else:
            self.pymysql_con.commit()
            print("修改成功！")
            return True

    # 删除数据的方法   接收所有的命名参数 即根据字段名传入对应数据
    def delete(self,**kwargs):
        try:
            delete_str = ""
            for i in self.field:
                try:
                    if not kwargs[i]:  # 字段值为空 返回删除失败！
                        print("错误信息：", i, "该字段值为空！")
                        return False
                except Exception:  # 该字段没有传入跳过
                    continue
                if isinstance(kwargs[i],str):
                    delete_str += f"{i}='{kwargs[i]}' and "
                else:
                    delete_str += f"{i}={kwargs[i]} and"
            field_str = delete_str.rstrip(" and ")  # 删除字符最后的“,”

            # 先查询满足条件的数据个数
            sql = f"""
                        select * from {self.table_name} where {field_str};
                """
            self.mysql.execute(sql)
            data = self.mysql.fetchall()
            if not data:  # 没有查询到则返回删除失败
                print("没有可删除的数据！")
                print("删除失败！")
                return False

            # 删除数据
            sql = f"""
                    delete from {self.table_name} where {field_str};
                """
            self.mysql.execute(sql)
        except Exception as e:
            self.pymysql_con.rollback()
            print("删除失败！")
            print("错误信息：", e)
            return False
        else:
            self.pymysql_con.commit()
            print("删除成功！")
            return True

    # 过滤查询数据
    def filter(self, **kwargs):
        try:
            filter_str = ""
            for i in self.field:
                try:
                    if not kwargs[i]: # 传入字段值参数为空 警告
                        print("警告：", i, "传入该字段值为空！")
                        continue
                except Exception:
                    continue

                if isinstance(kwargs[i], str):
                    filter_str += f"{i}='{kwargs[i]}'and"
                else:
                    filter_str += f"{i}={kwargs[i]} and"

            field_str = filter_str.rstrip(" and ")  # 删除字符最后的“,”

            sql = f"""
                select * from {self.table_name} where {field_str};
            """
            self.mysql.execute(sql)
        except Exception as e:
            print("查询失败！")
            print("错误信息：", e)
        else:
            data = self.mysql.fetchall()
            data_list = []
            for i in data:
                data_dict = {}
                for k,j in enumerate(self.field):
                    data_dict[j] = i[k]
                data_list.append(data_dict)
            # 返回查询集
            return data_list

    # 过滤获取数据  返回第一个数据
    def get(self,**kwargs):
        try:
            get_str = ""
            for i in self.field:
                try:
                    if not kwargs[i]:
                        print("错误信息：",i,"字段为空")
                        return False
                except Exception:
                    continue

                if isinstance(kwargs[i],str):
                    get_str += f"{i}='{kwargs[i]}' and"
                else:
                    get_str += f"{i}={kwargs[i]} and"

            field_str = get_str.rstrip(" and ")  # 删除字符最后的“,”

            sql = f"""
                select * from {self.table_name} where {field_str};
            """
            self.mysql.execute(sql)
        except Exception as e:
            print("查询失败！")
            print("错误信息：", e)
        else:
            data = self.mysql.fetchall()
            data_list = []
            for i in data:
                data_dict = {}
                for k,j in enumerate(self.field):
                    data_dict[j] = i[k]
                data_list.append(data_dict)

            if data_list: # 只返回查询到的第一行数据
                return data_list[0] # dict 字典类型
            return {}