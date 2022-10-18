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
    # "assign": 0,                        # 是否默认分配给商户 1是0否
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
4、按角色分别勾选权限后保存，将被勾选的权限key保存到角色内permissions字段，json——dict
5、修改权限：导出数据并组装为permission结构，进行修改；重复第2步。或者直接在线上修改，然后导出备份
6、用户登录
7、拉取权限数据，返回权限的所有条目和用户角色所拥有的权限以及权限版本号
8、接下来的每一次请求，都会带上权限版本号，后端根据版本号进行权限拦截判断
9、系统判断当前版本是否是最新的，如果不是，在header里设置标签，前端判断标签存在时，执行第7步操作
"""

# 业务端权限
service_permissions = [

    {"name": "控制台", "key": "dashboard", "permission_class": "tag", "children": [
        {"name": "总数统计", "key": "dashboard-url-count-api", "method": "get", "permission_class": "api", "hook_func": ""},
        {"name": "查看风险问题统计", "key": "dashboard-risk-statistics-api", "method": "get", "permission_class": "api"},
        {"name": "风险问题趋势", "key": "dashboard-risk-trend-api", "method": "get", "permission_class": "api"},
        {"name": "风险问题占比", "key": "dashboard-risk-proportion-api", "method": "get", "permission_class": "api"},
        {"name": "风险问题分级分布", "key": "dashboard-risk-level-api", "method": "get", "permission_class": "api"},
        {"name": "今日风险问题列表", "key": "dashboard-risk-list-api", "method": "get", "permission_class": "api"},
        {"name": "待办处理", "key": "dashboard-pending-list-api", "method": "get", "permission_class": "api"},
    ]},
    {"name": "监测任务", "key": "tasks", "permission_class": "tag", "children": [
        {"name": "查看任务列表", "key": "tasks-list-api", "method": "get", "permission_class": "api", "hook_func": ""},
        {"name": "查看任务详情", "key": "tasks-api", "method": "get", "permission_class": "api"},
        {"name": "新增任务", "key": "tasks-api", "method": "post", "permission_class": "api"},
        {"name": "修改任务", "key": "tasks-api", "method": "put", "permission_class": "api"},
        {"name": "删除任务", "key": "tasks-api", "method": "delete", "permission_class": "api"},
        {"name": "任务停用/启用", "key": "tasks-enable-api", "method": "put", "permission_class": "api"},
        {"name": "任务重新获取基准页", "key": "tasks-reload-url-api", "method": "put", "permission_class": "api"},
        {"name": "查看任务执行次数汇总", "key": "tasks-runtimes-api", "method": "get", "permission_class": "api"},
        {"name": "查看任务状态", "key": "tasks-status-api", "method": "get", "permission_class": "api"},
        {"name": "查看任务优先级", "key": "tasks-priority-api", "method": "get", "permission_class": "api"},
        {"name": "查看任务类型", "key": "tasks-type-api", "method": "get", "permission_class": "api"},
    ]},
    {"name": "风险监测", "key": "monitoring-risk", "permission_class": "tag", "children": [
        {"name": "敏感内容", "key": "monitoring-risk-stc", "permission_class": "tag", "children": [
            {"name": "查看敏感内容列表", "key": "monitoring-risk-stc-list", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "查看敏感内容详情", "key": "monitoring-risk-stc", "method": "get", "permission_class": "api"},
            {"name": "查看敏感内容快照", "key": "monitoring-risk-stc-snapshot", "method": "get", "permission_class": "api"},
            {"name": "查看敏感内容汇总数据", "key": "monitoring-risk-stc-summary", "method": "get", "permission_class": "api"},
            {"name": "查看敏感内容风险类别占比", "key": "monitoring-risk-stc-proportion", "method": "get",
             "permission_class": "api"},
            {"name": "查看敏感内容风险统计", "key": "monitoring-risk-stc-statistics", "method": "get", "permission_class": "api"},
            {"name": "处理敏感内容问题", "key": "monitoring-risk-stc-status", "method": "put", "permission_class": "api"},
            {"name": "敏感内容问题导出", "key": "monitoring-risk-stc-export", "method": "get", "permission_class": "api"},

        ]},
        {"name": "网页篡改", "key": "monitoring-risk-wtd", "permission_class": "tag", "children": [
            {"name": "查看网页篡改列表", "key": "monitoring-risk-wtd-list", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "查看网页篡改详情", "key": "monitoring-risk-wtd", "method": "get", "permission_class": "api"},
            {"name": "查看网页篡改快照", "key": "monitoring-risk-wtd-snapshot", "method": "get", "permission_class": "api"},
            {"name": "查看网页篡改汇总数据", "key": "monitoring-risk-wtd-summary", "method": "get", "permission_class": "api"},
            {"name": "查看网页篡改风险类别占比", "key": "monitoring-risk-wtd-proportion", "method": "get",
             "permission_class": "api"},
            {"name": "查看网页篡改风险统计", "key": "monitoring-tasks-wtd-statistics", "method": "get",
             "permission_class": "api"},
            {"name": "处理网页篡改问题", "key": "monitoring-risk-wtd-status", "method": "put", "permission_class": "api"},
            {"name": "网页篡改问题导出", "key": "monitoring-risk-wtd-export", "method": "get", "permission_class": "api"},

        ]},
        {"name": "挂马检测", "key": "monitoring-risk-trj", "permission_class": "tag", "children": [
            {"name": "查看挂马列表", "key": "monitoring-risk-trj-list", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "查看挂马详情", "key": "monitoring-risk-trj", "method": "get", "permission_class": "api"},
            {"name": "查看挂马快照", "key": "monitoring-risk-trj-snapshot", "method": "get", "permission_class": "api"},
            {"name": "查看挂马汇总数据", "key": "monitoring-risk-trj-summary", "method": "get", "permission_class": "api"},
            {"name": "查看挂马风险类别占比", "key": "monitoring-risk-trj-proportion", "method": "get", "permission_class": "api"},
            {"name": "查看挂马风险统计", "key": "monitoring-tasks-trj-statistics", "method": "get", "permission_class": "api"},
            {"name": "处理挂马问题", "key": "monitoring-risk-trj-status", "method": "put", "permission_class": "api"},
            {"name": "挂马问题导出", "key": "monitoring-risk-trj-export", "method": "get", "permission_class": "api"},

        ]},
        {"name": "暗链检测", "key": "monitoring-risk-bhs", "permission_class": "tag", "children": [
            {"name": "查看暗链列表", "key": "monitoring-risk-bhs-list", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "查看暗链详情", "key": "monitoring-risk-bhs", "method": "get", "permission_class": "api"},
            {"name": "查看暗链快照", "key": "monitoring-risk-bhs-snapshot", "method": "get", "permission_class": "api"},
            {"name": "查看暗链汇总数据", "key": "monitoring-risk-bhs-summary", "method": "get", "permission_class": "api"},
            {"name": "查看暗链风险等级占比", "key": "monitoring-risk-bhs-level-proportion", "method": "get",
             "permission_class": "api"},
            {"name": "查看暗链匹配类型", "key": "monitoring-tasks-bhs-match-type", "method": "get", "permission_class": "api"},
            {"name": "处理暗链问题", "key": "monitoring-risk-bhs-status", "method": "put", "permission_class": "api"},
            {"name": "暗链问题导出", "key": "monitoring-risk-bhs-export", "method": "get", "permission_class": "api"},

        ]},

    ]},

    {"name": "报告管理", "key": "reports-manage", "permission_class": "tag", "children": [
        {"name": "查看报告列表", "key": "reports-manage-list", "method": "get", "permission_class": "api", "hook_func": ""},
        {"name": "查看报告详情", "key": "reports-manage-detail", "method": "get", "permission_class": "api"},
        {"name": "查看报告基本信息", "key": "reports-manage-detail-info", "method": "get", "permission_class": "api"},
        {"name": "查看报告今日发现风险", "key": "reports-manage-detail-risk-found-today", "method": "get",
         "permission_class": "api"},
        {"name": "查看报告网站健康值统计", "key": "reports-manage-detail-url-statistics", "method": "get",
         "permission_class": "api"},
        {"name": "查看报告监测项得分", "key": "reports-manage-detail-risk-score", "method": "get", "permission_class": "api"},
        {"name": "查看报告风险占比", "key": "reports-manage-detail-risk-proportion", "method": "get",
         "permission_class": "api"},
        {"name": "查看报告敏感内容", "key": "reports-manage-detail-stc", "method": "get", "permission_class": "api"},
        {"name": "查看报告网页篡改", "key": "reports-manage-detail-wtd", "method": "get", "permission_class": "api"},
        {"name": "查看报告挂马检测", "key": "reports-manage-detail-trj", "method": "get", "permission_class": "api"},
        {"name": "查看报告暗链检测", "key": "reports-manage-detail-bhs", "method": "get", "permission_class": "api"},
        {"name": "导出报告", "key": "reports-manage-detail-export", "method": "get", "permission_class": "api"},

    ]},
    {"name": "资源配置", "key": "resource-manage", "permission_class": "tag", "children": [
        {"name": "资产配置", "key": "asset-configure", "permission_class": "tag", "children": [
            {"name": "查看资产列表", "key": "aasset-configure-list", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "编辑资产", "key": "asset-configure-api", "method": "put", "permission_class": "api"},
            {"name": "添加重点页面", "key": "asset-configure-important-url-api", "method": "post", "permission_class": "api"},
            {"name": "编辑重点页面", "key": "asset-configure-important-url-api", "method": "put", "permission_class": "api"},
            {"name": "删除重点页面", "key": "asset-configure-important-url-api", "method": "delete",
             "permission_class": "api"},
        ]},
        {"name": "资产统计", "key": "asset-statistics", "permission_class": "tag", "children": [
            {"name": "查看已统计主域列表", "key": "asset-statistics-domain-list", "method": "get", "permission_class": "api"},
            {"name": "查看资产数据统计", "key": "asset-statistics-data", "method": "get", "permission_class": "api",
             "hook_func": ""},
            {"name": "查看主域数据统计", "key": "asset-statistics-domain-data", "method": "get", "permission_class": "api"},
            {"name": "查看主域资产地域分布", "key": "asset-statistics-domain-area", "method": "get", "permission_class": "api"},
            {"name": "查看主域资产网络图谱", "key": "asset-statistics-domain-mapping", "method": "get",
             "permission_class": "api"},
            {"name": "查看主域资产待处理风险", "key": "asset-statistics-domain-risk", "method": "get", "permission_class": "api"},
            {"name": "查看子域列表", "key": "asset-statistics-subdomain-list", "method": "get", "permission_class": "api"},
            {"name": "查看IP列表", "key": "asset-statistics-ip-list", "method": "get", "permission_class": "api"},
            {"name": "查看端口列表", "key": "asset-statistics-port-list", "method": "get", "permission_class": "api"},
        ]},
        {"name": "预警规则", "key": "rules", "permission_class": "tag", "children": [
            {"name": "查看规则列表", "key": "rules-list", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "查看规则详情", "key": "rules-api", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "添加规则", "key": "rules-api", "method": "post", "permission_class": "api"},
            {"name": "编辑规则", "key": "rules-api", "method": "put", "permission_class": "api"},
            {"name": "删除规则", "key": "rules-api", "method": "delete", "permission_class": "api"},
            {"name": "启用或停用规则", "key": "rules-enable", "method": "put", "permission_class": "api"},
            {"name": "查看规则关联任务列表", "key": "rules-related-tasks-list", "method": "delete", "permission_class": "api"},
            {"name": "查看预警等级", "key": "rules-warn-level", "method": "delete", "permission_class": "api"},
            {"name": "查看预警指标", "key": "rules-warn-norm", "method": "delete", "permission_class": "api"},

        ]},
    ]},

    {"name": "自定义风险库", "key": "risk-library", "permission_class": "tag", "children": [
        {"name": "敏感词设置", "key": "sensitive-configure", "permission_class": "tag", "children": [
            {"name": "新增敏感词", "key": "sensitive-configure-api", "method": "post", "permission_class": "api",
             "hook_func": ""},
            {"name": "删除敏感词", "key": "sensitive-configure-api", "method": "delete", "permission_class": "api"},
            {"name": "风险类型词库启用停用", "key": "sensitive-configure-type-enable", "method": "put",
             "permission_class": "api"},
            {"name": "查看敏感词库列表", "key": "sensitive-configure-list", "method": "get", "permission_class": "api"},
            {"name": "查看敏感词库详情", "key": "sensitive-configure-api", "method": "get", "permission_class": "api"},
            {"name": "新增白名单", "key": "sensitive-configure-white", "method": "post", "permission_class": "api"},
            {"name": "删除白名单", "key": "sensitive-configure-white", "method": "delete", "permission_class": "api"},
            {"name": "查看白名单列表", "key": "sensitive-configure-white-list", "method": "get", "permission_class": "api"},

        ]},

        {"name": "信任链接", "key": "white-link", "permission_class": "tag", "children": [
            {"name": "查看信任链接列表", "key": "white-link-list", "method": "get", "permission_class": "api", "hook_func": ""},
            {"name": "添加信任链接", "key": "white-link-api", "method": "post", "permission_class": "api"},
            {"name": "删除信任链接", "key": "white-link-api", "method": "delete", "permission_class": "api"},
        ]},
    ]},

    {"name": "组织架构", "key": "organization", "permission_class": "tag", "children": [
        {"name": "用户设置", "key": "users-manage", "permission_class": "tag", "children": [
            {"name": "查看用户列表", "key": "users-manage-list", "method": "get", "permission_class": "api"},
            {"name": "新增用户", "key": "users-manage-api", "method": "post", "permission_class": "api"},
            {"name": "编辑用户", "key": "users-manage-api", "method": "put", "permission_class": "api"},
            {"name": "禁用启用用户", "key": "users-manage-enable", "method": "put", "permission_class": "api"},
        ]},

    ]},

    {"name": "用户中心", "key": "user-center", "permission_class": "tag", "children": [
        {"name": "个人主页", "key": "user-center-personal", "permission_class": "tag", "children": [
            {"name": "查看个人基本信息", "key": "user-center-personal-info", "method": "get", "permission_class": "api"},
            {"name": "编辑个人基本信息", "key": "user-center-personal-info", "method": "put", "permission_class": "api"},
            {"name": "修改个人密码", "key": "user-center-personal-pwd", "method": "put", "permission_class": "api"},
            {"name": "修改个人手机号", "key": "user-center-personal-number", "method": "put", "permission_class": "api"},
            {"name": "修改个人邮箱", "key": "user-center-personal-email", "method": "put", "permission_class": "api"},
            {"name": "上传头像", "key": "user-center-personal-header-upload", "method": "post", "permission_class": "api"},
            {"name": "下载头像", "key": "user-center-personal-header-download", "method": "get", "permission_class": "api"},
            {"name": "获取个人处理风险问题", "key": "user-center-personal-risk-question", "method": "get",
             "permission_class": "api"},

        ]},
        {"name": "站内信", "key": "message-center", "permission_class": "tag", "children": [
            {"name": "查看站内信列表", "key": "message-center-list", "method": "get", "permission_class": "api"},
            {"name": "编辑站内信状态", "key": "message-center-status", "method": "put", "permission_class": "api"},
            {"name": "查看站内信详情", "key": "message-center-detail", "method": "get", "permission_class": "api"},
            {"name": "查看站内信未读数量", "key": "message-center-unread-number", "method": "get", "permission_class": "api"},
        ]},

    ]},

]

# 系统管理端权限
system_permissions = []

# 业务端角色
service_groups = [
    {"name": "网站管理员", "desc": "主账号", "permissions": {}},
    {"name": "网站运营人员", "desc": "安全管理员", "permissions": {}},
    {"name": "普通用户", "desc": "数据分析师、运营人员等", "permissions": {}},
    {"name": "体验用户", "desc": "", "permissions": {}},
]
# 系统管理端角色
system_groups = [
    {"name": "系统管理员", "desc": "", "permissions": {}},
    {"name": "管理员", "desc": "", "permissions": {}},
    {"name": "研发人员", "desc": "", "permissions": {}},
    {"name": "测试人员", "desc": "", "permissions": {}},
]

if __name__ == '__main__':
    pass