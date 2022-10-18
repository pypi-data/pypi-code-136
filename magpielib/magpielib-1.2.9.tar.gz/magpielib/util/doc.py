from magpielib.parse import ShRouter
doc_admin_path = ''
server_name = ''
fo: any
fo = None


def init(path, name):
    global doc_admin_path
    global fo
    global server_name
    server_name = name
    doc_admin_path = path
    fo = open(doc_admin_path, "w")


def generate_doc4router(router: ShRouter):
    if not doc_admin_path or not fo:
        raise Exception('还没有初始化路径')
    router_uri = router.uri
    router_type = router.type
    router_desc = router.desc
    for detail in router.router_details:
        p_schema = detail.p_schema
        r_schema = detail.r_schema
        behavior = detail.behavior
        method = detail.method
        if router_desc:
            desc = router_type + "-" + router_desc + "-" + detail.desc
        else:
            desc = router_type + "-" + detail.desc
        if behavior:
            content = "\"\"\"" + "\n"
            content += '@apiGroup' + ' ' + server_name + '\n'
            content += '@api' + ' ' + '{' + method + '}' + ' ' + router_uri + ' ' + desc + '\n'
            content += '@apiName' + ' ' + desc + '\n'
            content += "@apiParam" + ' ' + '{string}' + ' ' + 'behavior' + ' ' + '行为' + "\n"
            content += "@apiParam" + ' ' + '{object}' + ' ' + behavior + ' ' + '' + "\n"
            content += parse_schema(p_schema)
            content += "@apiExample 请求示例:\n"
            content += _get_api_example(behavior, p_schema)
            if r_schema:
                content += "@apiSuccessExample 返回示例:\n"
                content += _get_api_example(None, r_schema)
                content += parse_schema(r_schema, '@apiSuccess')
            content += "\"\"\"" + "\n"
            fo.write(content)
        else:
            content = "\"\"\"" + "\n"
            content += '@apiGroup' + ' ' + server_name + '\n'
            content += '@api' + ' ' + '{' + method + '}' + ' ' + router_uri + ' ' + desc + '\n'
            content += '@apiName' + ' ' + desc + '\n'
            content += parse_schema(p_schema)
            content += "@apiExample 请求示例:\n"
            content += _get_api_example(None, p_schema)
            if r_schema:
                content += "@apiSuccessExample 返回示例:\n"
                content += _get_api_example(None, r_schema)
                content += parse_schema(r_schema, '@apiSuccess')
            content += "\"\"\"" + "\n"
            fo.write(content)
        _flush()


def parse_schema(schema, doc_param_type='@apiParam'):
    """
    @apiParam 代表请求参数
    @apiSuccess 成功代表返回参数
    """

    params = ''
    if schema and 'properties' in schema:
        required = schema.get('required')
        for name, value in schema.get('properties').items():
            param_type = value.get('type')
            param_desc = value.get('desc') or ''
            if not param_type:
                if 'not' in value:
                    param_type = 'not' + '_' + value.get('not').get('type')
                else:
                    continue
            if param_type == "array":
                items = value.get('items')
                if items:
                    r = parse_schema(items, doc_param_type)
                    params += r
            # added by cui 2021-10-21
            elif param_type == "object":
                params += parse_schema(value, doc_param_type)
            if required and name in required:
                param_desc += " **"
            if isinstance(param_type, list):
                param_type = '/'.join(param_type)
                param_type = '{' + param_type + '}'
            else:
                param_type = '{' + param_type + '}'
            params += doc_param_type + ' ' + param_type + ' ' + str(name) + ' ' + param_desc + "\n"
    return params


def _parse_schema4format(schema, apace_count=2):
    """

    :param schema:
    :param apace_count:  空格个数
    :return:
    """
    tc = ''
    for i in range(apace_count):
        tc += ' '
    example = ''
    example += '\n'
    example += tc + '{'
    example += '\n'
    if schema is None or schema.get('properties') is None:
        pass
    else:
        for name, desc in schema.get('properties').items():
            _type = ''
            if desc.get('type') == 'integer':
                _type = '0'
            elif desc.get('type') == 'string':
                _type = '""'
            elif desc.get('type') == 'array':
                _type = '[]'
                items = desc.get('items')
                _type = _parse_schema4format(items, apace_count + 4)
            # add by cui 2021-10-21
            elif desc.get('type') == 'object':
                _type = '[]'
                _type = _parse_schema4format(desc, apace_count + 4)
            line = tc + ' ' + str(name) + " : " + _type + '\n'
            example += line
    example += tc + '}'
    example += '\n'
    return example


def _get_api_example(behavior, schema):
    example = ''
    if behavior:
        example += '{'
        example += '\n'
        example += ' ' + 'behavior : ' + behavior + ','
        example += '\n'
        example += ' ' + behavior + ' : '
    example += _parse_schema4format(schema, 4)
    if behavior:
        example += '}'
        example += '\n'
    return example


def _flush():
    if fo:
        fo.flush()


def close():
    if fo:
        fo.close()


def mock_data(r_schema):
    if not r_schema:
        return
    result = None
    r_schema_type = r_schema.get('type')
    if isinstance(r_schema_type, list):
        r_schema_type = r_schema_type[0]
    if 'object' == r_schema_type:
        result = {}
        if r_schema.get('properties'):
            for key, value in r_schema.get('properties').items():
                result[key] = mock_data(value)
    elif 'array' == r_schema_type:
        result = []
        if r_schema.get('items'):
            r_list = mock_data(r_schema.get('items'))
            result = [r_list for _ in range(2)]
    elif 'string' == r_schema_type:
        result = 'this is a string'
    elif 'number' == r_schema_type:
        result = 88.88
    elif 'integer' == r_schema_type:
        result = 88
    elif 'boolean' == r_schema_type:
        result = True
    elif 'null' == r_schema_type:
        result = None
    return result
