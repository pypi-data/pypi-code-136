#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseModel
from model.schema.permission_schema import GroupsSchema, CompanyGroupsSchema, PermissionsSchema
from utils.rbac import permission_hook


class RBACPermissionModel(BaseModel, PermissionsSchema):

    @classmethod
    def _parse_data(cls, doc, **kwargs):
        """
        组装、修正单条记录
        该方法若存在，框架会自动使用
        若不存在，则模式使用框架内置方法
        :param doc: 单条数据
        :param kwargs:
        :return:
        """
        if not doc:
            return {}

        if "parent_id" in doc and doc["parent_id"] == None:
            doc["parent_id"] = 0
        doc = cls.format_datetime(doc)

        return doc

    @classmethod
    def has_permission(cls, handler):
        '''
        根据用户权限条目判断当前用户是否有权限请求
        :param request:
        :param permission_dict:
        :return:
        '''
        msg = None
        has_perm = False

        current_path = handler.request.path
        current_url_name = handler.__class__.__name__
        current_method = handler.request.method.lower()

        # # 企业账号免校验，拥有所有权限
        # if request.user.is_superuser:
        #     return True, msg

        # 是否启用权限系统
        if cls.is_enable(0) != True:
            return True, msg

        groups_permission = cls.model.GroupsModel.get_groups_mapping(0)
        # 支持用户有多个角色，只要其中一个角色有权限，即代表有权限
        for group_id in str(handler.member["group_id"]).split(','):
            if str(group_id) not in groups_permission:
                continue

            permission_dict = groups_permission[str(group_id)]
            if permission_dict["state"]:  # 角色禁用，视为无权限
                key = current_url_name + ":" + current_method
                val = permission_dict["permissions"].get(key)
                if val:  # 1有权限，0无权限, None
                    has_perm = True
                    permission_mapping = cls.get_permissions_mapping(0)
                    if key in permission_mapping:
                        permission = permission_mapping[key]
                        hook_func = permission["hook_func"]
                        if hook_func and hasattr(permission_hook, hook_func):
                            try:
                                results = getattr(permission_hook, hook_func)(handler.request)
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

    @classmethod
    def create_permission(cls, key, name, permission_class, content_type, **kwargs):
        """
        新增权限条目
        :param id:
        :param kwargs:
        :return:
        """
        if content_type not in [0, 1]:
            raise Exception("参数错误")
        if cls.get_datas_by_spec(sql_and=dict(key=key)):
            raise Exception("`%s`已被使用" % key)
        if cls.get_datas_by_spec(sql_and=dict(name=name, content_type=content_type)):
            raise Exception("`%s`已被使用" % name)
        if kwargs.get("hook_func") and cls.get_datas_by_spec(sql_and=dict(hook_func=kwargs.get("hook_func"))):
            raise Exception("`%s`已存在" % kwargs.get("hook_func"))
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

        cls.rmcache(content_type)
        return cls.create_data(**kwargs)

    @classmethod
    def update_permission(cls, permission_id, content_type, **kwargs):
        """
        单条更新权限信息: 名称 描述 状态（启用停用） 钩子 父级
        :param id:
        :param kwargs:
        :return:
        """
        kwargs.pop("id", "")
        kwargs.pop("key", "")
        # kwargs.pop("method", "")
        kwargs.pop("permission_class", "")
        if kwargs:
            cls.rmcache(content_type)
            cls.update_data(permission_id, **kwargs)

    @classmethod
    def remove_permission(cls, permission_id, content_type):
        """
        删除权限条目:物理删除
        :param id:
        :param kwargs:
        :return:
        """
        cls.rmcache(content_type)
        return cls.mysql.execute(f"delete from {cls.collection} where id=%s", [permission_id])

    @classmethod
    def get_permissions_list(cls, content_type=1):
        """
        前端
        权限条目
        导出为json,该数据结构返回给前端
        :return:
        """
        permissions = cls.redis.get("permissions:%s" % content_type)
        if permissions:
            permissions = cls.utils.to_python(permissions)
        else:
            permissions = []  # 顶级
            all_mapping = {}  # 所有数据的key：value
            datas = list(cls.get_datas_by_spec(sql_and=dict(state=1, content_type=content_type)))  # 按id正序读取
            for p in datas:
                if not p["parent_id"]:
                    p["parent_id"] = 0
                    permissions.append(p)
                all_mapping[p["id"]] = p
                if p["parent_id"]:
                    all_mapping[p["parent_id"]].setdefault("children", [])
                    all_mapping[p["parent_id"]]["children"].append(p)

            if permissions:
                cls.redis.set("permissions:%s" % content_type, cls.utils.to_json(permissions))
        return permissions

    @classmethod
    def get_permissions_mapping(cls, content_type=1):
        """
        权限是否启用：1是，0禁用
        :return:
        {
            key:method: 1 or 0, # methods含多个方法时，平铺为多个key和单方法，例如key:method
            key:get: 1,         # 键：权限key:方法(单个方法)
            key:post: 1,        # 键：权限key:方法(单个方法)
        }
        """
        permissions = cls.get_permissions_list(content_type)
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

    @classmethod
    def enable_permission(cls, content_type=1):
        """
        启用权限系统
        :param content_type:
        :return:
        """
        cls.redis.set("permission_enable:%s" % content_type, 1)

    @classmethod
    def disable_permission(cls, content_type=1):
        """
        停用权限系统
        :param content_type:
        :return:
        """
        cls.redis.set("permission_enable:%s" % content_type, 0)

    @classmethod
    def is_enable(cls, content_type=1):
        """
        是否需要权限拦截
        """
        return cls.redis.get("permission_enable:%s" % content_type) == b'1'

    @classmethod
    def rmcache(cls, content_type=1):
        cls.remove_redis(content_type)
        cls.set_version(content_type)

    @classmethod
    def remove_redis(cls, content_type=1):
        cls.redis.delete("groups:%s" % content_type)
        cls.redis.delete("permissions:%s" % content_type)
        cls.redis.delete("company_groups:%s" % content_type)

    @classmethod
    def set_version(cls, content_type=1):
        """
        每一次修改权限，版本号为当前时间戳
        :param content_type:
        :return:
        """
        cls.redis.set("permission_version:%s" % content_type, cls.utils.now())

    @classmethod
    def get_version(cls, content_type=1):
        """
        获取当前版本号
        :param content_type:
        :return:
        """
        current_version = cls.redis.get("permission_version:%s" % content_type) or 0
        return int(current_version)

    @classmethod
    def has_update(cls, client_version, content_type=1):
        """
        客户端是否需要更新权限
        当客户端请求的header.permission_version<当前版本号时，
        设置响应header.permission_version=current_version
        客户端判断响应头里包含header.permission_version时，重新请求权限数据，并刷新客户端权限配置
        :param client_version:
        :param content_type:
        :return:
        """
        return cls.get_version(content_type) > client_version

    @classmethod
    def autoload_permission(cls, routes_hander_mp, permissions):
        """
        自动收集并创建权限条目
        该方法由进程启动时调用，请勿手动调用
        routers： self.application.handlers
        routes_hander_mp： key对应的hendler对象
        permissions: {"key": [get, post], "key1": [get, put]}
        """
        method_title = {"get": "查看", "post": "创建", "put": "修改", "delete": "删除"}
        datas = []
        for key, methods in permissions.items():
            handler = routes_hander_mp[key]
            class_docs = handler.__doc__
            for method in methods:
                method_docs = getattr(handler, method).__doc__
                # 优先选取方法描述
                if not method_docs:
                    # 其次选取类描述
                    if not class_docs:
                        name = method_title[method] + key
                        describes = "自动载入的权限"
                    else:
                        class_docs_list = class_docs.split("\n")
                        docs = class_docs_list[0] or class_docs_list[1]
                        name = method_title[method] + docs.replace(" ", "")[:10]
                        describes = class_docs.replace("\n", "").replace(" ", "")[:100]
                else:
                    method_docs_list = method_docs.split("\n")
                    docs = method_docs_list[0] or method_docs_list[1]
                    name = docs.replace(" ", "")[:10]
                    describes = method_docs.replace("\n", "").replace(" ", "")[:100]

                data = cls.create_data(**{
                    "key": key,
                    "name": name or method_title[method] + key,
                    "method": method,
                    "permission_class": "api",
                    "describes": describes,
                    "content_type": 0
                })
                datas.append(data)
        if datas:
            cls.rmcache(0)
        return datas


class GroupsModel(BaseModel, GroupsSchema):

    @classmethod
    def _parse_data(cls, doc, **kwargs):
        """
        组装、修正单条记录
        该方法若存在，框架会自动使用
        若不存在，则模式使用框架内置方法
        :param doc: 单条数据
        :param kwargs:
        :return:
        """
        if not doc:
            return {}

        if "permissions" in doc:
            doc["permissions"] = cls.utils.to_python(doc["permissions"])
        doc = cls.format_datetime(doc)

        return doc

    @classmethod
    def get_members_count(cls, company_id, *groups):
        """
        属于某商户的角色的成员数
        """
        groups_mp = {}
        members = cls.model.AdminModel.get_datas_by_spec()
        for user in members:
            if company_id and company_id != user["company_id"]:
                continue
            for gid in user["group_id"].split(","):
                groups_mp.setdefault(gid, 0)
                groups_mp[gid] += 1

        for group in groups:
            group["counts"] = groups_mp.get(str(group["id"]), 0)

        return list(groups)

    @classmethod
    def get_members(cls, company_id, groups):
        """
        属于某商户且是该角色的成员
        """
        members = []
        for user in cls.model.AdminModel.get_datas_by_spec():
            if company_id and company_id != user["company_id"]:
                continue
            if groups["id"] in list(map(int, user["group_id"].split(","))):
                members.append(user)

        return members

    @classmethod
    def get_group_list_by_page(cls, page, count, **kwargs):
        """
        列表
        :return:
        :rtype:
        """

        datas, counts = cls.get_list_by_page(page, count, **kwargs)
        return datas, counts

    @classmethod
    def create_groups(cls, name, content_type, **group):
        """
        创建角色
        name = models.CharField(max_length=128)
        state = models.IntegerField(default=1)
        describes = models.CharField(max_length=128, default="", verbose_name='描述')
        permissions = models.JSONField(default=dict)
        content_type = models.IntegerField(default=1, verbose_name='1业务角色，2管理端角色')
        assign = models.IntegerField(default=1, verbose_name='是否默认分配给商户,1是0否')
        :return:
        """

        if content_type not in [0, 1]:
            raise Exception("参数错误")
        if cls.model.GroupsModel.get_data_by_spec(sql_and={"name": name, "content_type": content_type}):
            raise Exception("已存在同名角色")
        group["name"] = name
        group["content_type"] = content_type
        cls.model.RBACPermissionModel.rmcache(content_type)
        return cls.create_data(**group)

    @classmethod
    def update_group(cls, group_id, content_type, **kwargs):
        """
        更新角色信息: 名称 描述 状态 分配
        :param id:
        :param kwargs:
        :return:
        """
        kwargs.pop("id", "")
        kwargs.pop("permissions", "")
        if kwargs:
            cls.update_data(group_id, **kwargs)
            cls.model.RBACPermissionModel.rmcache(content_type)

    @classmethod
    def update_user_group(cls, *uids, group_id=None):
        """
        修改用户的角色
        :param uids:
        :param group_id: "gid1,gid2,gid3"
        :return:
        """
        try:
            user = cls.model.AdminModel.get_admin(id=uids[0])
            company = cls.model.CompanyModel.get_company(user["company_id"])
        except Exception as e:
            return
        if not cls.get_data_by_spec(sql_and={"company_id": company["id"], "group_id": group_id}):
            return

        for uid in uids:
            cls.model.AdminModel.update_data(uid, group_id=group_id)

    @classmethod
    def update_group_permission(cls, group_id, key, method, val):
        """
        单条勾选、取消权限
        :param group_id:
        :param key:
        :param method: get or get,post 多个方法用逗号隔开
        :return:
        """
        group = cls.get_data_by_kv(id=group_id)
        if group:
            permissions = group["permissions"]
            if val:
                permissions[key + ":" + method] = val
            else:
                permissions.pop(key + ":" + method, "")

            group.pop("group_id", "")
            cls.update_data(group_id, **group)
            cls.model.RBACPermissionModel.rmcache(group["content_type"])

    @classmethod
    def update_group_permissions(cls, group_id, permissions):
        """
        批量勾选、取消权限
        :param group_id:
        :param permissions:
            {
                "key:get": 1,
                "key:get,post": 1
            }
        :return:
        """
        group = cls.get_data_by_kv(id=group_id)
        if group:
            cls.update_data(group_id, permissions=cls.utils.to_json(permissions))
            cls.model.RBACPermissionModel.rmcache(group["content_type"])

    @classmethod
    def get_groups_list(cls, content_type=1):
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
        groups = cls.redis.get("groups:%s" % content_type)
        if groups:
            groups = cls.utils.to_python(groups)
        else:
            groups = []
            for g in cls.get_datas_by_spec(sql_and=dict(state=1, content_type=content_type)):
                groups.append(g)
            if groups:
                cls.redis.set("groups:%s" % content_type, cls.utils.to_json(groups))
        return groups

    @classmethod
    def get_groups_mapping(cls, content_type=1):
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
        groups = {str(g["id"]): g for g in cls.get_groups_list(content_type)}
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

    @classmethod
    def get_system_groups(cls):
        """
        获取系统角色
        :return: [1, 2, 3]
        """
        return cls.model.CompanyGroupsModel.get_company_groups(0)


class CompanyGroupsModel(BaseModel, CompanyGroupsSchema):

    @classmethod
    def _parse_data(cls, doc, **kwargs):
        """
        组装、修正单条记录
        该方法若存在，框架会自动使用
        若不存在，则模式使用框架内置方法
        :param doc: 单条数据
        :param kwargs:
        :return:
        """
        if not doc:
            return {}

        doc = cls.format_datetime(doc)

        return doc

    @classmethod
    def update_company_group(cls, company_id, group_ids):
        """
        修改、新增商户的角色
        :param old_group:
        :param new_group:
        :return:
        """
        groups_mp = cls.get_company_groups(1)
        groups_mp.update({"1": cls.get_system_groups()})
        old_group_id = groups_mp.get(str(company_id), [])
        group_ids = [group_ids] if not isinstance(group_ids, (list, tuple)) else group_ids
        diff_group_id = set(old_group_id) - set(group_ids)
        for group_id in group_ids:
            data = cls.get_data_by_spec(sql_and=dict(company_id=company_id, group_id=int(group_id)))
            if not data:
                cls.create_data(company_id=company_id, group_id=group_id)
            else:
                cls.update_data(data["id"], company_id=company_id, group_id=group_id)

        # 其他的角色，移除
        if diff_group_id:
            cls.remove_company_group(company_id, list(diff_group_id))
        cls.model.RBACPermissionModel.rmcache(1)

    @classmethod
    def remove_company_group(cls, company_id, group_ids):
        """
        移除商户的某个角色：所有已分配该角色的用户，将被解除角色绑定
        :param company_id:
        :param group_id:
        :return:
        """
        group_ids = [str(i) for i in ([group_ids] if not isinstance(group_ids, (list, tuple)) else group_ids)]
        # 删除角色
        for group_id in group_ids:
            cls.mysql.execute(f"delete from {cls.collection} where company_id=%s and group_id=%s",
                              [company_id, int(group_id)])

        # 从该用户角色中剔除这些角色
        for user in cls.model.AdminModel.get_datas_by_spec(sql_and=dict(company_id=company_id)):
            user_group_ids = set(user["group_id"].split(","))
            group_ids = set(group_ids)
            user_group_ids.difference_update(group_ids)
            user["group_id"] = ",".join(list(user_group_ids))
            cls.model.AdminModel.update_data(user["id"], group_id=user["group_id"])

        cls.model.RBACPermissionModel.rmcache(1)

    @classmethod
    def get_system_groups(cls):
        """
        获取系统角色
        :return: [1, 2, 3]
        """
        return cls.get_company_groups(0)

    @classmethod
    def get_company_groups(cls, content_type=1):
        """
        商户对应的角色
        :param content_type:
        :return:["2": [1, 2, 3], "3": [4, 5, 6]]
        """
        company_groups = {}
        cache_datas = cls.redis.get("company_groups:%s" % content_type)
        if cache_datas:
            company_groups = cls.utils.to_python(cache_datas)
        else:
            if content_type == 1:
                datas = cls.get_datas_by_spec()
                for item in datas:
                    if str(item["company_id"]) not in company_groups:
                        company_groups[str(item["company_id"])] = []
                    company_groups[str(item["company_id"])].append(item["group_id"])
            else:
                company_groups = []
                for group in cls.model.GroupsModel.get_datas_by_spec(sql_and=dict(content_type=content_type)):
                    company_groups.append(group["id"])

            if company_groups:
                cls.redis.set("company_groups:%s" % content_type, cls.utils.to_json(company_groups))

        return company_groups