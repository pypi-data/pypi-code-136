# -*- coding:utf-8 -*-
# 1~n级为标签，不具备权限值。只有所有子权限都被勾选后，当前标签勾选，否则不勾选。标签允许有任意多个上级和下级。
# 倒数第二级为API级别权限，称为接口权限。key为handler的名称url_name.拦截位置处于系统顶层入口处（只针对permission_class=api的权限），不侵入业务（可做到完全解耦）。当子类（如有）任意权限被勾选时，当前权限勾选。否则不勾选
# 倒数第一级为逻辑权限，是最小粒度的权限类型。属于API级的子类权限且不能再派生出子类权限。缺点是需要侵入业务内，即耦合较强。
# API权限辅助钩子，位于API数据体内的hook_func所制定的函数。用来拓展或者增强API接口的权限拦截，实现更高的定制化配置（如当请求参数里包含什么值时，禁止访问或修正该值）。
# 它不同于逻辑权限之处在于，钩子适合只做简单的条件判断；逻辑权限可在代码任意位置、任意逻辑、任意即时数据的值进行更复杂的进行判断。包括条件依赖判断、数据依赖判断、关系依赖判断。甚至在for循环内进行实时判断。
# key:method必须全局唯一，且一单设置永不得修改（除非用脚本全量修改且更新代码内的handler.url_name)，如有需要请通过删除该条struct,在用新的key定义新的struct
"""
要求：
1、api接口仅支持get、post、put、方法，且分别对应查、增、改、删
2、api权限一对一，一个key只对应一个url请求。
3、api权限一对多，一个key对应若干个url请求，如
    1）url采用动态路由设置时（/(thumb|comment)/detail代表2个url详情）,key=thumb_thumb,method=get可以实现权限："允许查看点赞|评论数据"权限，
    2）url采用动态路由设置时（/(thumb|comment)代表2个url详情），key=thumb_thumb,method=get,post,put,可以实现权限："允许增删查改点赞|评论数据"权限，
    3）使用逻辑权限

权限表结构设置:
{
    "name": "允许查看和新增",             # 权限名称
    "key": "control2-xxx-api",          # 路由名称,取url_name的值
    "method": "get,post,可空",           # 该权限支持的方法,多个用逗号隔开, 仅针对permission_class=api时有效
    "parent_id": 0,                      # 父级的id值，parent和parent_id二选一
    # "parent": 0,                        # 父级的key或key:method值的组合，为空时代表顶级
    "permission_class": "",                        # 类别，tag标签；api接口权限；logic逻辑权限
    "hook_func": "",                    # 钩子，可空
    "state": 1,                         # 1启用0禁用，默认1
    "desc": "",                         # 详细说明
    "url": "",                          # 权限对应的url，可空
    "content_type": 1 or 0              # 1 业务端使用，0系统管理端
}
角色表：
groups：{
    "name": "角色名称",
    #                       # 父级id,暂不支持
    # "group_class": "技术部",            # 分类，可以按标签|部门|组织等自定义划分
    "state": 1,                           # 1可以 0 禁用 默认1
    "content_type": 1 or 0,             # 1 业务端使用，0系统管理端
    "permissions": {
        "control2-xxx-api:get": 1,
        "control2-xxx-api2:get,post,put,delete": 1,
        "monitoring-tasks-api:post": 1
    }
}
商户角色：分配给商户的角色
company_groups: {
    "group_id": "group.id",
    "company_id": "",
}

例：permissions: []
标签1：{"name": "控制台", "key": "control1", "parent": "无父级，留空", "permission_class": "tag", "state": "1启用0停用，默认1", "desc": "详细说明，可空"}
    标签2: {"name": "左侧区域", "key": "control2", "parent": "control1;父级的id值,不填时有程序自动识别", "permission_class": "tag"}
        API权限1: {"name": "查看详情", "key": "control2-xxx-api", "method": "get", "parent": "control2;父级的id值", "permission_class": "api", "hook_func": "func_for_definition"}
            逻辑权限1: {"name": "男性能查看游戏数据", "key": "control2-xxx-api-for-boy", "method": "get", "parent": "control2-xxx-api;父级的id值", "permission_class": "logic"}
            逻辑权限2: {"name": "女性能查看购物数据", "key": "control2-xxx-api-for-girls", "method": "get", "parent": "control2-xxx-api;父级的id值", "permission_class": "logic"}
            逻辑权限3: {"name": "查看点赞|评论数据", "key": "control2-thumb-comment", "method": "get", "parent": "control2-xxx-api;父级的id值", "permission_class": "logic"}
            逻辑权限4: {"name": "增删查改点赞|评论数据", "key": "control2-thumb-comment", "method": "get,post,put,", "parent": "control2-xxx-api;父级的id值", "permission_class": "logic"}
        API权限2: {"name": "添加数据", "key": "control2-xxx-api", "method": "post", "parent": "control2;父级的id值", "permission_class": "api", "hook_func": "func_for_definition，默认空"}
        API权限3: {"name": "删除数据", "key": "control2-xxx-api", "method": "", "parent": "control2;父级的id值", "permission_class": "api", "hook_func": "func_for_definition"}
    标签3: {"name": "右侧区域", "key": "control3", "parent": "control1;父级的id值", "permission_class": "tag"}
    ...
    API权限4: {"name": "查看", "key": "url_name", "parent": "control1;父级的id值", "permission_class": "tag"}
    API权限5: {"name": "查看", "key": "url_name", "parent": "control1;父级的id值", "permission_class": "tag"}
        逻辑权限a
        逻辑权限b
    ...
    逻辑权限i
    逻辑权限j
    ...
标签4
标签5
...
API权限6
API权限7
...
逻辑权限x
逻辑权限y

角色权限结构:
group_permission1：{
    "control2-xxx-api:get": 1代表有权限，0或不存在该key，代表无权限,
    "control2-xxx-api-for-girls:get": 0
    "control2-xxx-api:get,post": 1, # 组合权限，允许新增和查看。不能按方法分拆为多条，否则无法映射回原始权限条目
    "control2-xxx-api:get,post": 1, # 组合权限，允许新增和查看。不能按方法分拆为多条，否则无法映射回原始权限条目
}
group_permission2：{
    "control2-xxx-api:get": 1代表有权限，0或不存在该key，代表无权限,
    "control2-xxx-api-for-girls:get": 0
}

配置步骤：
1、编写脚本将数据生成类型下面的permission结构，
2、用导入脚本将permission结构转为单条db数据，key+method组合唯一，写入db或redis
3、在管理界面调用，读出permission数据渲染
4、按角色分别勾选权限后保存，将被勾选的权限key保存到角色内
5、修改权限：导出数据并组装为permission结构，进行修改；重复第2步。或者直接在线上修改，然后导出备份
"""

# 业务端权限
service_permissions = [
    {"name": "控制台", "key": "control1", "permission_class": "tag",
     "children": [
        {"name": "左侧区域", "key": "control2", "permission_class": "tag", "parent": "父级的id值,不填时有程序自动识别",
         "children": [
            {"name": "查看详情", "key": "user_detail", "method": "get", "permission_class": "api", "hook_func": "func_for_definition，默认空",
             "children": [
                # 暂不支持逻辑权限
                # {"name": "男性能查看游戏数据", "key": "ontrol2-xxx-api", "permission_class": "logic"},
                # {"name": "女性能查看购物数据", "key": "ontrol2-xxx-api", "permission_class": "logic"}
             ]}
         ]},
        {"name": "右侧区域", "key": "control2", "parent": "control1", "permission_class": "tag", "children": []}
    ]},
    {"name": "监测任务", "key": "monitoring-tasks", "permission_class": "tag", "children": [
        {"name": "查看", "key": "monitoring-tasks-api", "method": "get", "permission_class": "api", "hook_func": ""},
        {"name": "新增", "key": "monitoring-tasks-api", "method": "post", "permission_class": "api"},
        {"name": "编辑", "key": "monitoring-tasks-api", "method": "put", "permission_class": "api"},
        {"name": "删除", "key": "monitoring-tasks-api", "method": "delete", "permission_class": "api"},
        {"name": "停用/启用", "key": "monitoring-tasks-state", "method": "get", "permission_class": "api"},
    ]},
    {"name": "风险监测", "key": "monitoring-risk", "permission_class": "tag", "children": [
        {"name": "敏感内容", "key": "monitoring-risk-stc", "permission_class": "tag", "children": [
            {"name": "查看", "key": "monitoring-risk-stc", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "新增", "key": "monitoring-risk-stc", "method": "post", "permission_class": "api"},
            {"name": "编辑", "key": "monitoring-risk-stc", "method": "put", "permission_class": "api"},
            {"name": "删除", "key": "monitoring-risk-stc", "method": "delete", "permission_class": "api"},
            {"name": "导出", "key": "monitoring-risk-stc-export", "method": "get", "permission_class": "api"},
            {"name": "导入", "key": "monitoring-tasks-stc-import", "method": "post", "permission_class": "api"},
        ]},
        {"name": "网页篡改", "key": "monitoring-risk-wtd", "permission_class": "tag", "children": [
            {"name": "查看", "key": "monitoring-risk-wtd", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "新增", "key": "monitoring-risk-wtd", "method": "post", "permission_class": "api"},
            {"name": "编辑", "key": "monitoring-risk-wtd", "method": "put", "permission_class": "api"},
            {"name": "删除", "key": "monitoring-risk-wtd", "method": "delete", "permission_class": "api"},
            {"name": "导出", "key": "monitoring-risk-wtd-export", "method": "get", "permission_class": "api"},
            {"name": "导入", "key": "monitoring-tasks-wtd-import", "method": "post", "permission_class": "api"},
        ]},
        {"name": "挂马检测", "key": "monitoring-risk-trj", "permission_class": "tag", "children": [
            {"name": "查看", "key": "monitoring-risk-trj", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "新增", "key": "monitoring-risk-trj", "method": "post", "permission_class": "api"},
            {"name": "编辑", "key": "monitoring-risk-trj", "method": "put", "permission_class": "api"},
            {"name": "删除", "key": "monitoring-risk-trj", "method": "delete", "permission_class": "api"},
            {"name": "导出", "key": "monitoring-risk-trj-export", "method": "get", "permission_class": "api"},
            {"name": "导入", "key": "monitoring-tasks-trj-import", "method": "post", "permission_class": "api"},
        ]},
        {"name": "暗链检测", "key": "monitoring-risk-bhs", "method": "get", "permission_class": "tag", "children": [
            {"name": "查看", "key": "monitoring-risk-bhs", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "新增", "key": "monitoring-risk-bhs", "method": "post", "permission_class": "api"},
            {"name": "编辑", "key": "monitoring-risk-bhs", "method": "put", "permission_class": "api"},
            {"name": "删除", "key": "monitoring-risk-bhs", "method": "delete", "permission_class": "api"},
            {"name": "导出", "key": "monitoring-risk-bhs-export", "method": "get", "permission_class": "api"},
            {"name": "导入", "key": "monitoring-tasks-bhs-import", "method": "post", "permission_class": "api"},
        ]}
    ]},
    {"name": "报告管理", "key": "report-manage", "permission_class": "tag", "children": [
        {"name": "查看", "key": "report-manage", "method": "get", "permission_class": "api", "hook_func": ""},
        {"name": "新增", "key": "report-manage", "method": "post", "permission_class": "api"},
        {"name": "编辑", "key": "report-manage", "method": "put", "permission_class": "api"},
        {"name": "删除", "key": "report-manage", "method": "delete", "permission_class": "api"},
        {"name": "导出", "key": "report-manage-export", "method": "get", "permission_class": "api"},
        {"name": "导入", "key": "report-manage-import", "method": "post", "permission_class": "api"},
    ]},
    {"name": "资源配置", "key": "resource-manage", "permission_class": "tag", "children": []},
    {"name": "资产配置", "key": "asset-manage", "permission_class": "tag", "children": []},
]

# 系统管理端权限
system_permissions = []

# 业务端角色
service_groups = [
        {"name": "网站管理员", "desc": "主账号"},
        {"name": "网站运营人员", "desc": "安全管理员"},
        {"name": "普通用户", "desc": "数据分析师、运营人员等"},
        {"name": "体验用户", "desc": ""},
]
# 系统管理端角色
system_groups = [
        {"name": "系统管理员", "desc": ""},
        {"name": "管理员", "desc": ""},
        {"name": "研发人员", "desc": ""},
        {"name": "测试人员", "desc": ""},
]

if __name__ == '__main__':
    pass