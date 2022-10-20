import time, os, inspect, importlib
from code_util.markdown import markdowndoc


class apidoc_generation():
    """
    动态生成所有API文档的Markdown格式
    """

    def __init__(self, tar_path, module_names, exclude_name):
        """
        初始化函数
        :param tar_path: 生成文件的路径
        :param module_names: 模块的列表
        :param exclude_name: 排除的关键字列表
        """
        self.module_names = module_names
        self.exclude_names = exclude_name
        self.tar_path = tar_path

        self.markdown = markdowndoc(self.tar_path, True)

    def _output_function(self, fun_name, funcls, class_cls=None):
        doc_str = funcls.__doc__
        if doc_str is None:
            if class_cls is not None:
                class_buffer_pointer = class_cls
                while True:
                    if fun_name not in class_buffer_pointer.__dict__:
                        break
                    base_method = getattr(class_buffer_pointer, fun_name)
                    if base_method is None:
                        break
                    doc_str = base_method.__doc__
                    if doc_str is None:
                        class_buffer_pointer = class_buffer_pointer.__bases__[0]
                    else:
                        break
            if doc_str is None:
                self.markdown.write_line("无文档")
                return

        doc_str_split = [x for x in doc_str.split('\n')]
        doc_str_split = [x.strip() for x in doc_str_split]
        doc_str_split = [x for x in doc_str_split if len(x) > 0]

        methods_str = []
        parameters_data = []
        for line in doc_str_split:
            if line.startswith(':param'):
                split_maohao = line.find(':', 2)
                key = line[6: split_maohao]
                value = line[split_maohao + 1:]
                parameters_data.append([key, value])
                continue
            if line.startswith(':return'):
                split_maohao = line.find(':', 2)
                return_str = line[split_maohao + 1:]
                parameters_data.append(['return', return_str])
                continue
            methods_str.append(line)

        self.markdown.write_line("\n\n".join(methods_str))
        self.markdown.write_table(['name', 'note'], parameters_data)

    def _validate_memeber_base_module(self, base_module, memeberslist):
        new_list = []
        for item, item_cls in memeberslist:
            if base_module in item_cls.__module__:
                new_list.append((item, item_cls))
        return new_list

    def generation(self):
        """
        生成文档的方法
        :return:
        """
        result_dict = {}

        for module_ in self.module_names:
            if module_ not in result_dict:
                result_dict[module_] = {
                    'class': [],
                    'function': [],
                    'modules': []
                }

            for path, dir_name, file_names in os.walk(module_):
                path_pre = ".".join([x for x in os.path.split(path) if x])

                if len([1 for x in self.exclude_names if x in path]) > 0 or path.startswith('_'):
                    continue

                for filename in file_names:
                    if len([1 for x in self.exclude_names if x in filename]) > 0 or filename.startswith('_'):
                        continue

                    module_name = path_pre + "." + filename.replace('.py', '')

                    module_obj = importlib.import_module(module_name)
                    all_classes = inspect.getmembers(module_obj, inspect.isclass)
                    all_function = inspect.getmembers(module_obj, inspect.isfunction)
                    all_module = inspect.getmembers(module_obj, inspect.ismodule)

                    all_classes = self._validate_memeber_base_module(module_name, all_classes)
                    all_function = self._validate_memeber_base_module(module_name, all_function)

                    result_dict[module_]['class'] += all_classes
                    result_dict[module_]['function'] += all_function
                    result_dict[module_]['modules'] += all_module

        # print
        for l1 in result_dict.keys():
            self.markdown.write_title(l1, 1)

            if len(result_dict[l1]['class']) > 0:
                self.markdown.write_title(f"Class", 2)

            for l2_class, l2_cls in result_dict[l1]['class']:
                self.markdown.write_title(l2_class, 3)
                if '__doc__' in l2_cls.__dict__ and l2_cls.__dict__['__doc__'] is not None:
                    self.markdown.write_line(l2_cls.__dict__['__doc__'].strip())

                self.markdown.write_line("method", True)

                for func, func_cls in inspect.getmembers(l2_cls, inspect.isfunction):
                    if func.startswith('_') and not func.startswith('__'):
                        continue
                    self.markdown.write_line(f"- {func}")
                    self._output_function(func, func_cls, l2_cls)

            if len(result_dict[l1]['function']) > 0:
                self.markdown.write_title(f"Function", 2)

            for func, l2_cls in result_dict[l1]['function']:
                if func.startswith('_') and not func.startswith('__'):
                    continue
                self.markdown.write_title(func, 3)
                self._output_function(func, l2_cls)

        self.markdown.flush()
        time.time()
