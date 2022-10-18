import datetime
from ayaka import AyakaApp

app = AyakaApp("时区助手")
app.help = """时区助手
- tz_add <name> <timezone> 添加一条时区转换，例如
    tz_add 北京 8
    tz_add 伦敦 0
    tz_add 洛杉矶 -8
- tz <name> 返回name对应时区的时间，例如 
    tz 北京
- tz <number> 返回对应时区的时间，例如 
    tz 8
- tz_list 查看所有的时区转换
"""


@app.on_command("tz_add")
async def tz_add():
    if len(app.args) < 2:
        await app.send(app.help)
        return

    name = str(app.args[0])
    try:
        timezone = int(str(app.args[1]))
    except:
        await app.send("timezone 参数格式错误，请输入纯数字，东八区为8，西八区为-8")
        return

    timezone = (timezone+8) % 24 - 8

    st = app.group_storage("data", default={})
    data: dict = st.load()
    data[name] = timezone
    st.save(data)

    await app.send("添加成功："+get_info(name, timezone))


def get_info(name, timezone):
    if timezone == 0:
        timezone = "零时区"
    elif timezone > 0:
        timezone = f"东{timezone}区"
    else:
        timezone = f"西{-timezone}区"
    return f"[{name}] {timezone}"


@app.on_command("tz_list")
async def tz_list():
    data: dict = app.group_storage("data", default={}).load()
    items = []
    for name, timezone in data.items():
        items.append(get_info(name, timezone))
    if items:
        await app.send("\n".join(items))
    else:
        await app.send("目前没有设置任何时区转换")


@app.on_command("tz")
async def tz():
    if len(app.args) < 1:
        await app.send(app.help)
        return

    data: dict = app.group_storage("data", default={}).load()
    name = str(app.args[0])
    if name in data:
        timezone = data[name]
    else:
        try:
            timezone = int(name)
        except:
            await app.send("不存在可用的时区转换")
            await app.send(app.help)
            return

    td = datetime.timedelta(hours=timezone)
    tz = datetime.timezone(td)
    time = datetime.datetime.now(tz=tz)
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    await app.send(t)
