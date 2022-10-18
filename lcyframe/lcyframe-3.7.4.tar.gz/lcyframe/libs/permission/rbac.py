import os, sys, django, json
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


keys = []
names = []
class RBACPermission(object):
    PERMISSION_TABLE = "permission_group"
    PERMISSION_CLASS_TABLE = "permission_class"

    CURRENT_PERMISSION_GROUP = None
    CURRENT_PERMISSION_CLASS = None
    __VERSION__ = 0
    MAX_NUMS = 63
    IS_DEBUG = False
    default_group_config = None
    default_class_config = None
    mongo = MongoCon._database

    @classmethod
    def initial(cls):
        if cls.mongo is None:
            cls.mongo = MongoCon._database
            if cls.mongo is None:
                raise Exception("you must get a mongo isinstance!")

        if cls.CURRENT_PERMISSION_GROUP is None:
            cls.__load_permission_group()
        if cls.CURRENT_PERMISSION_CLASS is None:
            cls.__load_permission_class()

        return cls

    def has_permission(request):
        '''
        根据用户权限条目判断当前用户是否有权限请求
        :param request:
        :param permission_dict:
        :return:
        '''
        msg = None
        has_perm = False

        resolve_url_obj = resolve(request.path)
        current_url_name = resolve_url_obj.url_name
        current_method = request.method.lower()
        groups_permission = get_groups_mapping()
        if request.user.group_id in groups_permission:
            permission_dict = groups_permission[request.user.group_id]
            if permission_dict["state"]:         # 角色禁用，视为无权限
                key = current_url_name + ":" + current_method
                val = permission_dict["permissions"].get(key)
                if val:               # 1有权限，0无权限, None
                    has_perm = True
                    permission_mapping = get_permissions_mapping()
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

        return has_perm, msg


    def init_permission(current_user, request):
        '''
        初始化所有权限条目
        :param current_user:
        :param request:
        :return:
        '''
        return None   # 不需要初始化
        # 获取当前用户的所有权限条目
        permission_item_queryset = get_permissions()
        permission_dict = {}
        for item in permission_item_queryset:
            permission_dict[item.code_name] = [
                item.url_name,
                item.permission_method,
                item.permission_args,
                item.permission_kwargs,
                item.permission_hook_func,
                item.menu_id,
            ]
        request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
        logger.debug("%s", permission_dict)


    def check_permission(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if not has_permission(*args, **kwargs):
                return JsonResponse({
                    'code': 403,
                    'msg': '没有权限'
                })
            return func(*args, **kwargs)

        return inner

    def rmcache(func):
        @wraps(func)
        def remove(*args, **kwargs):
            redis.delete("groups:%s" % 1)
            redis.delete("permissions:%s" % 1)
            redis.delete("company_groups:%s" % 1)
            redis.delete("groups:%s" % 0)
            redis.delete("permissions:%s" % 0)
            redis.delete("company_groups:%s" % 0)
            return func(*args, **kwargs)

        return remove

    def create_groups(**group):
        """
        创建角色
        name = models.CharField(max_length=128)
        state = models.IntegerField(default=1)
        desc = models.CharField(max_length=128, default="", verbose_name='描述')
        permissions = models.JSONField(default=dict)
        content_type = models.IntegerField(default=1)
        :return:
        """
        if Groups.objects.filter(name=group["name"]):
            return False
        else:
            return Groups.objects.create(**group)

    @rmcache
    def update_user_group(*uids, group_id=None):
        """
        修改用户的角色
        :param uids:
        :param kwargs: 新角色的id或0
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
    def update_company_group(company_id, group_ids):
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
    def remove_company_group(company_id, group_ids):
        """
        移除商户的某个角色：所有已分配该角色的用户，将被重置为无角色
        :param company_id:
        :param group_id:
        :return:
        """
        group_ids = [group_ids] if not isinstance(group_ids, (list, tuple)) else group_ids
        for group_id in group_ids:
            User.objects.filter(company_id=company_id, group_id=group_id).update(group_id=0)
            try:
                data = CompanyGroups.objects.get(company_id=company_id, group_id=group_id)
                data.delete()
            except Exception as e:
                pass

    @rmcache
    def update_group_permission(group_id, key, method, val):
        """
        勾选、取消权限
        :param group_id:
        :param val:
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


    def get_permissions_list(content_type=1):
        """
        权限条目导出为json,该数据结构返回给前端
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

    def get_permissions_mapping(content_type=1):
        """
        key与权限映射: 若用户某个权限值为1，则根据权限的基础信息，如hook_func执行对应操作
        :return:
        {
            key:method: 1 or 0, # methods含多个方法时，平铺为多个key和单方法，例如key:method
            key:get: 1,         # 键：权限key:方法(单个方法)
            key:post: 1,        # 键：权限key:方法(单个方法)
        }
        """
        permissions = get_permissions_list(content_type)
        permissions_mapping = {}
        def collect_api_permission(item, mapping):
            if item.get("children"):
                childrens = item.pop("children")
                for children in childrens:
                    collect_api_permission(children, mapping)
            else:
                # 权限禁用后，不做校验，视为有权限
                if item["permission_class"] == "api" and item["state"]:
                    for method in item["method"].split(","):
                        mapping[item["key"] + ":" + method] = item
                else:
                    return mapping

        for p in permissions:
            collect_api_permission(p, permissions_mapping)
        return permissions_mapping

    def get_groups_list(content_type=1):
        """
        返回角色（含权限），返回给前端
        :return:
        [
            {
                "name": "角色名称",
                "group_class":
                "state": 1,                           # 1可以 0 禁用 默认1
                "permissions": {
                    "control2-xxx-api:get": 1,
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

    def get_groups_mapping(content_type=1):
        """
        获取角色-权限映射
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
        groups = {g["id"]: g for g in get_groups_list(content_type)}
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

    def get_company_groups(content_type=1):
        """
        商户对应的角色
        :param content_type:
        :return:
        """
        company_groups = {}
        rmcache_datas = redis.get("company_groups:%s" % content_type)
        if rmcache_datas:
            company_groups = json.loads(rmcache_datas)
        else:
            datas = CompanyGroups.objects.all()
            for item in datas:
                if item.company_id not in company_groups:
                    company_groups[item.company_id] = []
                company_groups[item.company_id].append(item.group_id)
            if company_groups:
                redis.set("company_groups:%s" % content_type, json.dumps(company_groups))

        return company_groups

if __name__ == '__main__':
    # create_groups(**{"name": "新角色"})
    # update_company_group(2, [5,8])
    # update_user_group(58, group_id=5)
    # remove_company_group(2, 5)
    # update_group_permission(5, "user_detail", "get", 1)

    print(get_permissions_list(1))
    print(get_permissions_mapping(1))
    print(get_groups_list(1))
    print(get_company_groups(1))
    pass