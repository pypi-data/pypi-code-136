# -*- coding: utf8 -*-
# 文件:  mini_app_template.py
# 日期:  2022/1/22 17:55
from .tools import JdTools
from .logs import logger


__all__ = ['template_dict', 'get_template', "JdMiniAppTemplate", "jd_parse_template"]
_author__ = 'WXG'
__version__ = '1.2'


template_dict = {}  # template id: (编号, 模板ID, 标题)


def get_template(temp_id):
    # 根据模板值，获取模板ID
    return template_dict.get(temp_id, (0, 0))[1]


def jd_parse_template(template_file):
    with open(template_file, 'r', encoding='utf8') as f:
        content = f.read()

        size = len(content)
        i = 0
        while i < size:

            s, i = get_template_section(content, i)
            if i == -1:
                break

            i += 3  # 跳过 ``` 的长度
            if 'type' not in s:
                continue

            key = single_info(s, 'type')
            code = single_info(s, '编号')
            template_id = single_info(s, '模版ID')
            if not template_id:
                template_id = single_info(s, '模板ID')
            template_name = single_info(s, '标题')
            if not template_name:
                template_name = single_info(s, '模版标题')
            if key:
                template_dict[int(key)] = (code, template_id, template_name)


def get_template_section(content, start):
    # 从 内容 content 的 start 起始位置(0 开始), 查询 ``` 和 ``` 之间的内容
    p1 = content.find('```', start)
    if p1 == -1:
        return '', -1
    p2 = content.find('```', p1 + 3)
    return content[p1 + 3: p2], p2


def single_info(template_msg, key):
    p1 = template_msg.find(key)
    if p1 == -1:
        return ''
    k = p1 + len(key)
    p2 = template_msg.find('\n', k)
    line = template_msg[k: p2]
    line = line.replace('=', '').replace('：', '').replace(':', '')
    line = JdTools.trim(line)
    return line


class JdMiniAppTemplate(object):

    def __init__(self):
        self._show_template = True

    def set_show_template(self, is_show):
        self._show_template = is_show

    def show(self, force_show=False):
        if self._show_template or force_show:
            logger.debug(f'微信模板 读取完成！ 数量：{len(template_dict)}')
            for m in template_dict.items():
                logger.debug(f'{m}')
