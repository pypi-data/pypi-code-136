import django
import os
from collections import Iterable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jydsj.settings")# project_name 项目名称
django.setup()
from django.db import connection
from textwrap import dedent
import re


def text_indent(s):
    dedentString = lambda s: dedent(s[1:])[:-1]
    return dedentString(s)


f = """<pre style="margin: 0px 2em 1em; font-family: monospace,
serif; font-size: 1em; white-space: pre; overflow-wrap: normal; 
padding: 0.5em; overflow: auto; border-left: 5px solid rgba(41, 42, 136, 0.2);">import textwrap
from textwrap_example import sample_text

def should_indent(line):
print('Indent {!r}?'.format(line))
return len(line.strip()) % 2 == 0

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ',
predicate=should_indent)

print('\nQuoted block:\n')
print(final)
</pre>
"""

if 1 == 1:
    a = """
    serif; font-size: 1em; white-space: pre; overflow-wrap: normal; 
    padding: 0.5em; overflow: auto; border-left: 5px solid rgba[(]([\w\W]*?)[)];">import textwrap
    """
    #三引号必须放在文本上下两边
    b = text_indent(a)

e = re.search(b, f)
# print(e.group(1))


def my_custom_sql(sqlstring):
    # 建立游标
    cursor = connection.cursor()
    cursor.execute(sqlstring)

    row = cursor.fetchall()
    # 美化输出
    # print(row)
    # 打印列名
    if isinstance(row, tuple):
        # 是元组就一直迭代
        # 第一层元组
        for ro in row:
            if isinstance(ro, tuple):
                for r in ro:
                    print(r, end="\t\t")
            print('\n', end="")
    indentation = 0
    if len(connection.queries) > 0:
        # width = terminal_width()
        width = 160
        total_time = 0.0
        for query in connection.queries:
            # print("query是什么---", query)
            nice_sql = query['sql'].replace('"', '').replace(',', ', ')
            sql = "\033[1;31m[%s]\033[0m %s" % (query['time'], nice_sql)
            total_time = total_time + float(query['time'])
            while len(sql) > width - indentation:
                print("%s%s" % (" " * indentation, sql[:width - indentation]))
                sql = sql[width - indentation:]
            print("%s%s\n" % (" " * indentation, sql))
        replace_tuple = (" " * indentation, str(total_time))
        print("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)

    return row


if __name__ == "__main__":
    sql = """
SELECT last_name,department_name,commission_pct
FROM employees e,departments d
WHERE e.department_id=d.department_id
AND e.commission_pct IS NOT NULL
    """
    my_custom_sql(sql)