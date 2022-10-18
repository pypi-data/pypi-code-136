
    
import pathlib, importlib
import time

test_path = pathlib.Path(__file__).parent
# print(test_path)

print("开始一键测试: %s" % test_path)
time.sleep(1)

for path in test_path.rglob('*.py'):
    filename = path.name
    module = path.stem
    if module in [test_path.name, "__init__"]:
        continue
    # print(filename, module)
    import_object = importlib.import_module(module)
    if not hasattr(import_object, "batch_groups"):
        print("正在执行脚本: %s" % filename)
        raise Exception("文件[%s]，未找到测试簇方法:batch_groups()" % filename)

    # 执行测试簇
    print("正在执行脚本: %s" % filename)
    try:
        getattr(import_object, 'batch_groups')()
    except Exception as e:
        print(str(e))
        print("测试退出")
        exit()
    else:
        print("测试完成")
    