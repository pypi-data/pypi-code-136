import os, sys, json, time
from functools import wraps





class RBACPermission(object):
    """
    权限拦截尽量不入侵到model层，哪怕是逻辑权限也尽可能在handler层处理
    """

    def __init__(self, handler):
        self.handler = handler
        # self.model = handler.model

    def has_permission(self, request):
        '''
        根据用户权限条目判断当前用户是否有权限请求
        :param request:
        :param permission_dict:
        :return:
        '''
        msg = None
        has_perm = False

        resolve_url_obj = request.path
        current_url_name = resolve_url_obj.url_name
        current_method = request.method.lower()

        # # 企业账号免校验，拥有所有权限
        # if request.user.is_superuser:
        #     return True, msg

        # 是否启用权限系统
        if self.is_enable(1) != True:
            return True, msg

        groups_permission = self.get_groups_mapping()
        # 支持用户有多个角色，只要其中一个角色有权限，即代表有权限
        for group_id in str(request.user.group_id).split(','):
            if str(group_id) not in groups_permission:
                continue

            permission_dict = groups_permission[str(group_id)]
            if permission_dict["state"]:         # 角色禁用，视为无权限
                key = current_url_name + ":" + current_method
                val = permission_dict["permissions"].get(key)
                if val:               # 1有权限，0无权限, None
                    has_perm = True
                    permission_mapping = self.get_permissions_mapping()
                    if key in permission_mapping:
                        permission = permission_mapping[key]
                        hook_func = permission["hook_func"]
                        if hook_func and hasattr(permission_hook, hook_func):
                            try:
                                results = getattr(permission_hook, hook_func)(request)
                                if isinstance(results, tuple) and len(results) == 2:
                                    flag, msg = results
                                else:
                                    flag, msg = results, ""
                            except Exception as e:
                                print(str(e))
                            else:
                                if flag:
                                    has_perm = True
                    if has_perm:
                        break
                    else:
                        continue

        return has_perm, msg


    def check_permission(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            has_per, msg = self.has_permission(*args, **kwargs)
            if not has_per:
                return JsonResponse({
                    'code': 403,
                    'msg': '没有权限'
                })
            return func(*args, **kwargs)

        return inner

    def rmcache(self, func):
        @wraps(func)
        def remove(*args, **kwargs):
            self.remove_redis()
            self.set_version()
            return func(*args, **kwargs)

        return remove

    def remove_redis(self):
        content_type = 1
        redis.delete("groups:%s" % content_type)
        redis.delete("permissions:%s" % content_type)
        redis.delete("company_groups:%s" % content_type)

    def set_version(self):
        """
        每一次修改权限，版本号为当前时间戳
        :param content_type:
        :return:
        """
        content_type = 1
        redis.set("permission_version:%s" % content_type, int(time.time()))

    def get_version(self, content_type=1):
        """
        获取当前版本号
        :param content_type:
        :return:
        """
        current_version = redis.get("permission_version:%s" % content_type) or 0
        return int(current_version)

    def has_update(self, client_version, content_type=1):
        """
        客户端是否需要更新权限
        当客户端请求的header.permission_version<当前版本号时，
        设置响应header.permission_version=current_version
        客户端判断响应头里包含header.permission_version时，重新请求权限数据，并刷新客户端权限配置
        :param client_version:
        :param content_type:
        :return:
        """
        return self.get_version(content_type) > client_version

    def create_groups(self, name, content_type, **group):
        """
        创建角色
        name = models.CharField(max_length=128)
        state = models.IntegerField(default=1)
        desc = models.CharField(max_length=128, default="", verbose_name='描述')
        permissions = models.JSONField(default=dict)
        content_type = models.IntegerField(default=1, verbose_name='1业务角色，2管理端角色')
        assign = models.IntegerField(default=1, verbose_name='是否默认分配给商户,1是0否')
        :return:
        """

        if content_type not in [0, 1]:
            raise Exception("参数错误")
        if Groups.objects.filter(name=name, content_type=content_type):
            raise Exception("已存在同名角色")
        group["name"] = name
        group["content_type"] = content_type
        return Groups.objects.create(**group)

    @rmcache
    def update_group(self, group_id, **kwargs):
        """
        更新角色信息: 名称 描述 状态 分配
        :param id:
        :param kwargs:
        :return:
        """
        kwargs.pop("id", "")
        kwargs.pop("permissions", "")
        kwargs.pop("content_type", "")
        if kwargs:
            Groups.objects.filter(id=group_id).update(**kwargs)

    @rmcache
    def update_user_group(self, *uids, group_id=None):
        """
        修改用户的角色
        :param uids:
        :param group_id: "gid1,gid2,gid3"
        :return:
        """
        try:
            user = User.objects.get(id=uids[0])
            company = Company.objects.get(id=user.company_id)
        except Exception as e:
            return
        if not CompanyGroups.objects.filter(company_id=company.id, group_id=group_id):
            return
        User.objects.filter(id__in=uids).update(group_id=group_id)

    @rmcache
    def update_company_group(self, company_id, group_ids):
        """
        修改、新增商户的角色
        :param old_group:
        :param new_group:
        :return:
        """
        group_ids = [group_ids] if not isinstance(group_ids, (list, tuple)) else group_ids
        for group_id in group_ids:
            CompanyGroups.objects.update_or_create(company_id=company_id, group_id=group_id)

    @rmcache
    def remove_company_group(self, company_id, group_ids):
        """
        移除商户的某个角色：所有已分配该角色的用户，将被解除角色绑定
        :param company_id:
        :param group_id:
        :return:
        """
        group_ids = [str(i) for i in ([group_ids] if not isinstance(group_ids, (list, tuple)) else group_ids)]
        # 删除角色
        for group_id in group_ids:
            try:
                data = CompanyGroups.objects.get(company_id=company_id, group_id=group_id)
                data.delete()
            except Exception as e:
                pass

        # 从该用户角色中剔除这些角色
        for user in User.objects.filter(company_id=company_id):
            user_group_ids = set(user.group_id.split(","))
            group_ids = set(group_ids)
            user.group_id = ",".join(user_group_ids.difference_update(group_ids))
            user.save()

    @rmcache
    def update_group_permission(self, group_id, key, method, val):
        """
        勾选、取消权限
        :param group_id:
        :param key:
        :param method:
        :return:
        """
        group = Groups.objects.get(id=group_id)
        if group:
            permissions = group.permissions
            for method in method.split(","):
                if val:
                    permissions[key+":"+method] = val
                else:
                    permissions.pop(key+":"+method, "")
            group.save()

    @rmcache
    def create_permission(self, key, name, permission_class, content_type, **kwargs):
        """
        新增权限条目
        :param id:
        :param kwargs:
        :return:
        """
        if content_type not in [0, 1]:
            raise Exception("参数错误")
        if Permissions.objects.filter(key=key):
            raise Exception("<%s>已被使用" % key)
        if Permissions.objects.filter(name=name, content_type=content_type):
            raise Exception("<%s>已被使用" % name)
        if kwargs.get("hook_func") and Permissions.objects.filter(hook_func=kwargs.get("hook_func")):
            raise Exception("<%s>已存在" % kwargs.get("hook_func"))
        if permission_class not in ["tag", "api", "logic逻辑权限"]:
            raise Exception("permission_class只能是tag，api，logic中的一个")
        if permission_class != "tag":
            if not kwargs.get("method"):
                raise Exception("没有提供方法名method")
            for method in kwargs.get("method").split(","):
                if method not in ["get", "delete", "put", "post"]:
                    raise Exception("不支持该方法名" % method)
        kwargs["name"] = name
        kwargs["key"] = key
        kwargs["permission_class"] = permission_class
        kwargs["content_type"] = int(content_type)
        kwargs.setdefault("state", 1)
        return Permissions.objects.create(**kwargs)

    @rmcache
    def update_permission(self, permission_id, **kwargs):
        """
        更新权限信息: 名称 描述 状态 钩子 父级
        :param id:
        :param kwargs:
        :return:
        """
        kwargs.pop("id", "")
        kwargs.pop("key", "")
        kwargs.pop("method", "")
        kwargs.pop("permission_class", "")
        kwargs.pop("content_type", "")
        if kwargs:
            Permissions.objects.filter(id=permission_id).update(**kwargs)


    @rmcache
    def remove_permission(self, permission_id):
        """
        删除权限条目
        :param id:
        :param kwargs:
        :return:
        """
        return Permissions.objects.filter(id=permission_id).delete()

    def get_permissions_list(self, content_type=1):
        """
        前端
        权限条目
        导出为json,该数据结构返回给前端
        :return:
        """
        permissions = redis.get("permissions:%s" % content_type)
        if permissions:
            permissions = json.loads(permissions)
        else:
            permissions = []     # 顶级
            all_mapping = {}     # 所有数据的key：value
            datas = list(Permissions.objects.filter(state=1, content_type=content_type))   # 按id正序读取
            for p in datas:
                p = model_to_dict(p)
                if not p["parent_id"]:
                    permissions.append(p)
                all_mapping[p["id"]] = p
                if p["parent_id"]:
                    all_mapping[p["parent_id"]].setdefault("children", [])
                    all_mapping[p["parent_id"]]["children"].append(p)

            if permissions:
                redis.set("permissions:%s" % content_type, json.dumps(permissions))
        return permissions

    def get_permissions_mapping(self, content_type=1):
        """
        权限是否启用：1是，0禁用
        :return:
        {
            key:method: 1 or 0, # methods含多个方法时，平铺为多个key和单方法，例如key:method
            key:get: 1,         # 键：权限key:方法(单个方法)
            key:post: 1,        # 键：权限key:方法(单个方法)
        }
        """
        permissions = self.get_permissions_list(content_type)
        permissions_mapping = {}
        def collect_api_permission(item, mapping):
            if item.get("children"):
                childrens = item.pop("children")
                for children in childrens:
                    collect_api_permission(children, mapping)
            else:
                # 权限禁用后，不再进行权限校验等同于有权访问
                if item["permission_class"] == "api" and item["state"]:
                    for method in item["method"].split(","):
                        mapping[item["key"] + ":" + method] = item
                else:
                    return mapping

        for p in permissions:
            collect_api_permission(p, permissions_mapping)
        return permissions_mapping

    def get_groups_list(self, content_type=1):
        """
        前端
        返回角色（含权限）
        :return:
        [
            {
                "id": "id",
                "name": "角色名称",
                # "group_class": "技术部",             # 预留，自定义标签
                "state": 1,                           # 1可以 0 禁用 默认1
                "content_type": 1 or 0,             # 1 业务端使用，0系统管理端
                "assign": 0,                        # 是否默认分配给商户 1是0否
                "permissions": {
                    "control2-xxx-api:get": 1,        # 1勾选，0未勾选
                    "control2-xxx-api2:get,post,put,delete": 1,  # 组合方法
                    "monitoring-tasks-api:post": 1
                }
            },
            ...
        ]
        """
        groups = redis.get("groups:%s" % content_type)
        if groups:
            groups = json.loads(groups)
        else:
            groups = []
            for g in Groups.objects.filter(state=1, content_type=content_type):
                groups.append(model_to_dict(g))
            if groups:
                redis.set("groups:%s" % content_type, json.dumps(groups))
        return groups

    def get_groups_mapping(self, content_type=1):
        """
        获取角色拥有的权限，多个方法组合为一个权限时，会得到多条k：v
        :return:
        {
            1: {
                "...": **groups,                  # 角色基础信息
                "permissions": {
                    groups.key:get: 1,         # 键：权限key:方法(单个方法)
                    groups.key:post: 1,        # 键：权限key:方法(单个方法)
                    ...
                }
            }
        }
        """
        groups = {str(g["id"]): g for g in self.get_groups_list(content_type)}
        for id, group in groups.items():
            temp = {}
            permissions = group.pop("permissions")
            # get,post 多个方法平铺
            for keys, val in permissions.items():
                if not val:
                    continue  # 0代表没有权限，跳过
                key, methods = keys.split(":")
                if "," in methods:
                    for method in methods.split(","):
                        temp[key + ":" + method] = val
                else:
                    temp[keys] = val
            group["permissions"] = temp
        return groups

    def get_system_groups(self):
        """
        获取系统角色
        :return:
        """
        return self.get_company_groups(0)

    def get_company_groups(self, content_type=1):
        """
        商户对应的角色
        :param content_type:
        :return:
        """
        company_groups = {}
        cache_datas = redis.get("company_groups:%s" % content_type)
        if cache_datas:
            company_groups = json.loads(cache_datas)
        else:
            company_groups[str(content_type)] = []
            if content_type == 1:
                datas = CompanyGroups.objects.all()
                for item in datas:
                    if str(item.company_id) not in company_groups:
                        company_groups[str(item.company_id)] = []
                    company_groups[str(item.company_id)].append(item.group_id)
            else:
                for group in Groups.objects.filter(content_type=content_type):
                    company_groups[str(content_type)].append(group.id)

            if company_groups:
                redis.set("company_groups:%s" % content_type, json.dumps(company_groups))

        return company_groups

    def enable_permission(self, content_type=1):
        """
        启用权限系统
        :param content_type:
        :return:
        """
        redis.set("permission_enable:%s" % content_type, 1)

    def disable_permission(self, content_type=1):
        """
        停用权限系统
        :param content_type:
        :return:
        """
        redis.set("permission_enable:%s" % content_type, 0)

    def is_enable(self, content_type=1):
        return redis.get("permission_enable:%s" % content_type) == b'1'

if __name__ == '__main__':
    # create_groups(**{"name": "新角色"})
    # update_group(19, name="单位主账号", desc="dSsd")
    # create_permission("xxx-key", "xxx-name", "api", 1, method="get")
    # remove_permission(274)
    # update_permission(154, desc="修改钩子", hook_func="func1,func2", parent_id=145)
    # # update_company_group(2, [5,8])
    # # update_user_group(58, group_id=5)
    # # remove_company_group(2, 5)
    # # update_group_permission(5, "user_detail", "get", 1)
    #
    # print(get_permissions_list(1))
    # print(get_permissions_mapping(1))
    # print(get_groups_list(1))
    print(get_company_groups(1))
    # print(get_system_groups())
    # enable_permission()
    # disable_permission()
    # print(is_enable())

    # 版本
    # print(get_version(1))
    # print(has_update(0, 1))
    pass