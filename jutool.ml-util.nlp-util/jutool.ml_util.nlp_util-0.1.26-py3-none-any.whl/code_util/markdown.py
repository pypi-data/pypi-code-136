class markdowndoc():
    """
    生成Markdown文本的辅助类
    """
    def __init__(self, path, need_toc=True):
        """
        初始化函数
        :param path: 生成的目标目录
        :param need_toc: 是否建立目录
        """
        self.file_lines = []
        self.path = path

        if need_toc:
            self.file_lines.append('[toc] \n')

    def _convert_char(self, ss: str):
        ss = ss.replace('\\', "\\\\")
        ss = ss.replace("__", "\_\_")
        ss = ss.replace("#", "\#")
        return ss

    def _generate_count_char(self, char, count):
        s = ""
        for _ in range(count):
            s += char

        return s

    def write_title(self, str, level):
        """
        打印标题
        :param str: 标题内容
        :param level: 标题级别
        :return: 无返回
        """
        self.file_lines.append(f"{self._generate_count_char('#', level)} {self._convert_char(str)} \n")

    def write_line(self, str, is_block=None):
        """
        打印文字
        :param str: 文字内容
        :param is_block: 是否粗体打印
        :return: 无返回
        """
        if is_block:
            self.file_lines.append(f"**{self._convert_char(str)}** \n")
        else:
            self.file_lines.append(f"{self._convert_char(str)} \n")

    def write_table(self, title: [], data: [[]]):
        """
        打印表格
        :param title: 标题，list【str】
        :param data: 表格内容， list【list【列内容】】
        :return: 无返回
        """
        title = [self._convert_char(x) for x in title]
        self.file_lines.append(f"| {'|'.join(title)} | \n")
        self.file_lines.append(f"| {'|'.join(['----' for _ in title])} | \n")
        for row in data:
            row_new = [self._convert_char(x).replace('\n','<br>') for x in row]
            self.file_lines.append(f"| {'|'.join(row_new)} | \n")

    def flush(self):
        """
        输出文件的实际命令
        :return: 无返回
        """
        with open(self.path, 'w') as f:
            f.writelines(self.file_lines)
