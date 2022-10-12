import xcall

"""
测试集
"""

# 指定端口号
xcall.phone_port = 12138
# 是否debug模式
xcall.debug = False
# 是否使用局域网连接
xcall.use_lan = False
# 如果使用局域网连接，需要提供手机ip
xcall.phone_ip = "10.93.134.25"


def test():
    # 调用静态方法
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testInt", 1, 10))

    # 调用嵌套类的构造器
    print(xcall.call_constructor_str("com.dragon.read.xcall.demo.Test$ProgressData"))

    # 获取静态属性
    print(xcall.call_read_field_str("com.dragon.read.xcall.demo.Test.floatField"))

    # 修改静态属性值，显式指定类型为int
    print(xcall.call_write_field("com.dragon.read.xcall.demo.Test.shortField", 1, field_type='short'))

    # 调用静态方法，显式指定参数为char
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testChar(char,char)", 'a', 'b'))

    # 调用无参静态方法
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testVoid"))

    # 异步调用方法
    print(xcall.call_method_str("java.lang.Thread.currentThread", mainThread=False))

    # 输出转换为json
    print(xcall.call_read_field_json("com.dragon.read.xcall.demo.Test.book"))

    # 参数为null
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testObj(com.dragon.read.xcall.demo.Test$Book)", None))

    # 参数为数组，元组和列表均可识别
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testArray", ((1, 2), (2, 3)), [[2, 3], [3, 4]]))

    # 参数为model
    print(xcall.call_method_json(
        "com.dragon.read.xcall.demo.Test.testModel(com.dragon.read.xcall.demo.Test$ProgressData)",
        {'id': "hello", "pageIndex": 100}))

    # 使用objId连续调用
    book = xcall.call_read_field("com.dragon.read.xcall.demo.Test.book")
    progressData = xcall.call_read_field(book + ".progressData")
    pageIndex = xcall.call_read_field_str(progressData + ".pageIndex")
    print(pageIndex)

    # 大量数据传输
    print(xcall.call_method_str("com.dragon.read.xcall.demo.Test.testBigData"))

    # 手动构造请求json调用
    print(xcall.call({
        "target": "java.lang.String.valueOf",
        "params": [
            13.14
        ],
        "types": [
            "double"
        ],
        "converter": 0
    }))
