from pathlib import Path
from lxml import etree


def get_methods_src_str_list(root):
    methods = []
    for m in root.xpath("POU/Method"):
        dec = m.find('./Declaration').text
        imp = m.find('./Implementation/ST').text if m.find('./Implementation/ST') is not None else ''
        methods.append(f'\n{dec}\n{imp}\nEND_METHOD')
    return methods


def get_property_src_str_list(root):
    properties = []
    for m in root.xpath("POU/Property"):
        dec = m.find('./Declaration').text
        getter_dec = m.find('./Get/Declaration').text if m.find('./Get/Declaration') is not None else ''
        getter_imp = m.find('./Get/Implementation/ST').text if m.find('./Get/Implementation/ST') is not None else ''
        setter_dec = m.find('./Set/Declaration').text if m.find('./Set/Declaration') is not None else ''
        setter_imp = m.find('./Set/Implementation/ST').text if m.find('./Set/Implementation/ST') is not None else ''

        properties.append(f'\n{dec}\nPROPERTY_GETTER\n{getter_dec}\n{getter_imp}\nEND_PROPERTY_GETTER\nPROPERTY_SETTER\n{setter_dec}\n{setter_imp}\nEND_PROPERTY_SETTER\nEND_PROPERTY')
    return properties


def get_action_src_str_list(root):
    actions = []
    for m in root.xpath("POU/Action"):
        act_imp = m.find('./Implementation/ST').text if m.find('./Implementation/ST') is not None else ''

        actions.append(f'\nACTION {m.get("Name")}\n{act_imp}\nEND_ACTION')
    return actions


def get_transition_src_str_list(root):
    transitions = []
    for m in root.xpath("POU/Transition"):
        act_imp = m.find('./Implementation/ST').text if m.find('./Implementation/ST') is not None else ''

        transitions.append(f'\nTRANSITION {m.get("Name")}\n{act_imp}\nEND_TRANSITION')
    return transitions


def get_src_str_from_pou(file_path):
    root = etree.parse(file_path).getroot()
    pou_dec = root.find('./POU/Declaration').text
    pou_imp = root.find('./POU/Implementation/ST').text if root.find('./POU/Implementation/ST') is not None else ''
    properties_str = "".join(get_property_src_str_list(root))
    methods_str = "".join(get_methods_src_str_list(root))
    actions_str = "".join(get_action_src_str_list(root))
    transitions_str = "".join(get_transition_src_str_list(root))

    return f'\n{pou_dec}\n{pou_imp}\n{properties_str}\n{methods_str}\n{actions_str}\n{transitions_str}'


def get_src_str_from_gvl(file_path):
    root = etree.parse(file_path).getroot()
    return root.find('./GVL/Declaration').text if root.find('./GVL/Declaration') is not None else ''


def get_src_str_from_dut(file_path):
    root = etree.parse(file_path).getroot()
    return root.find('./DUT/Declaration').text if root.find('./DUT/Declaration') is not None else ''


def get_sources_of_project(project_path):
    """

    :param project_path: absolute path to the TwinCAT proejct folder
    :return:
    """
    for file_ending in ['*.TcIO', '*.TcDUT', '*.TcGVL', '*.TcPOU']:
        for path in Path(project_path).rglob(file_ending):
            match file_ending:
                case '*.TcDUT':
                    src_str = get_src_str_from_dut(path)
                case '*.TcGVL':
                    src_str = get_src_str_from_gvl(path)
                case '*.TcPOU':
                    src_str = get_src_str_from_pou(path)
                case '*.TcIO':
                    src_str = ''
                case _:
                    src_str = ''

            tmp = path.relative_to(project_path)
            pou_name = tmp.name.replace(file_ending[1:], '')
            sub_folder_path = str(tmp).split(pou_name)[0]

            yield pou_name, sub_folder_path, src_str


def create_source_files_of_project(project_path, destination_path):
    """

    :param project_path:
    :param destination_path:
    :return:
    """
    for file_name, sub_folder, src_str in get_sources_of_project(src_folder):
        dst_folder = f'{destination_path}/{sub_folder}'
        Path(dst_folder).mkdir(parents=True, exist_ok=True)
        with open(f'{dst_folder}/{file_name}.st', 'w', encoding="utf-8") as file:
            file.write(src_str)
