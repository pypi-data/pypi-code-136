"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564

MIT License
Copyright (c) 2022 Dear PyGui, LLC
"""
import dearpygui.dearpygui as dpg
import webbrowser
import os
import requests
import itertools
import subprocess
import sys


def run():
    dpg.create_context()

    with open("NotoSans-Regular.ttf", "wb") as f:
        f.write(requests.get('https://github.com/Superior-GitHub/superior6564/raw/main/superior6564/NotoSans-Regular.ttf').content)

    big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
    big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
    small_let_end = 0x00FF  # small "я" in cyrillic alphabet
    remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
    alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
    alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped
    # chars_remap = {OLD: NEW}
    chars_remap = {0x00A8: 0x0401,  # Ё
                   0x00B8: 0x0451,  # ё
                   0x00AF: 0x0407,  # Ї
                   0x00BF: 0x0457,  # ї
                   0x00B2: 0x0406,  # І
                   0x00B3: 0x0456,  # і
                   0x00AA: 0x0404,  # Є
                   0x00BA: 0x0454}  # є

    with dpg.font_registry():
        with dpg.font("NotoSans-Regular.ttf", 20) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            biglet = remap_big_let  # Starting number for remapped cyrillic alphabet
            for i1 in range(big_let_start, big_let_end + 1):  # Cycle through big letters in cyrillic alphabet
                dpg.add_char_remap(i1, biglet)  # Remap the big cyrillic letter
                dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Remap the small cyrillic letter
                biglet += 1  # choose next letter
            for char in chars_remap.keys():
                dpg.add_char_remap(char, chars_remap[char])

    def to_cyr(instr):  # conversion function
        out = []  # start with empty output
        for i in range(0, len(instr)):  # cycle through letters in input string
            if ord(instr[i]) in chars_remap:
                out.append(chr(chars_remap[ord(instr[i])]))
            elif ord(instr[i]) in range(big_let_start, small_let_end + 1):  # check if the letter is cyrillic
                out.append(chr(ord(instr[i]) + alph_shift))  # if it is change it and add to output list
            else:
                out.append(instr[i])
        return ''.join(out)

    def print_name_def(name: str):
        print("-", end="")
        for i in range(len(name)):
            print("-", end="")
        print("-")
        print(f"|{name}|")
        print("-", end="")
        for i in range(len(name)):
            print("-", end="")
        print("-")

    def generator_ru_words():
        print_name_def("generator_ru_words()")

        with open("russian_nouns.txt", "wb") as f:
            f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/Superior6564/main/superior6564/russian_nouns.txt').content)

        with open("russian_nouns_without_io.txt", "wb") as f:
            f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/superior6564/russian_nouns_without_io.txt').content)

        with open("degget_elite.jpg", "wb") as f:
            f.write(requests.get('https://github.com/Superior-GitHub/superior6564/raw/main/superior6564/degget_elite.jpg').content)

        width, height, channels, data = dpg.load_image('degget_elite.jpg')

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag="image_1", parent="generator_group")

        global speed
        speed = 1

        def fast():
            dpg.delete_item('mode_group', children_only=True)
            global speed
            speed = 1
            dpg.add_text(tag="Status for fast", pos=[490, 365], default_value="Fast",
                         parent='mode_group')

        def slow():
            dpg.delete_item('mode_group', children_only=True)
            global speed
            speed = 0
            dpg.add_text(tag="Status for slow", pos=[490, 365], default_value="Slow",
                         parent='mode_group')

        dpg.add_text(tag="Text for choosing mode", pos=[290, 365], default_value="Choose mode:",
                     parent="generator_group")
        dpg.add_button(tag="Button for fast mode", label="Fast", callback=fast, pos=[295, 390],
                       parent="generator_group")
        dpg.add_button(tag="Button for slow mode", label="Slow", callback=slow, pos=[340, 390],
                       parent="generator_group")
        dpg.add_text(tag="Text for status of mode", pos=[440, 365], default_value="Mode:",
                     parent="generator_group")

        def print_value():
            print_name_def("Generator of words")
            raw_letters = dpg.get_value('Input all letters')
            raw_length = dpg.get_value('Input length of words')

            if raw_letters == '':
                raw_letters = "ëóïîãð"  # "лупогр"
                print(f"Example letters: {to_cyr(raw_letters)}")
            else:
                print(f"Input all letters: {to_cyr(raw_letters)}")

            if raw_length == '':
                raw_length = 3
                print(f"Example length of words: {raw_length}")
            else:
                print(f"Input length of words: {raw_length}")

            all_of_letters = to_cyr(raw_letters)
            length_of_words = int(raw_length)
            global speed
            if speed == 1:
                print("Mode: Fast")
                with open('russian_nouns_without_io.txt', encoding='utf-8') as f1:
                    with open("results_gen_ru_words.txt", "w", encoding='utf-8') as f2:
                        list_of_ru_words = []
                        number_of_words_txt = 51301
                        for j in range(number_of_words_txt):
                            if j != (number_of_words_txt - 1):
                                list_of_ru_words.append(f1.readline()[0:-1])
                            else:
                                list_of_ru_words.append(f1.readline()[0:])
                        f2.write(f"Слова из {length_of_words} букв:\n")
                        words = set(itertools.permutations(all_of_letters, r=length_of_words))
                        # global count_2
                        count_2 = 1
                        for word in words:
                            count = 0
                            generate_word = "".join(word)
                            for j in range(len(list_of_ru_words)):
                                if generate_word == list_of_ru_words[j] and count == 0:
                                    f2.write(f"{count_2} слово: {generate_word}\n")
                                    count += 1
                                    count_2 += 1
                        print(f"Count of words: {count_2 - 1}")
            else:
                print("Mode: Slow")
                with open('russian_nouns.txt', encoding='utf-8') as f1:
                        list_of_ru_words = []
                        list_of_ru_gen_words = []
                        list_of_counts_of_words = []
                        number_of_words_txt = 51301
                        for j in range(number_of_words_txt):
                            if j != (number_of_words_txt - 1):
                                list_of_ru_words.append(f1.readline()[0:-1])
                            else:
                                list_of_ru_words.append(f1.readline()[0:])

                        words = set(itertools.permutations(all_of_letters, r=length_of_words))
                        # global count_2
                        count_2 = 1
                        for word in words:
                            count = 0
                            generate_word = "".join(word)
                            for j in range(len(list_of_ru_words)):
                                if generate_word == list_of_ru_words[j] and count == 0 and generate_word not in list_of_ru_gen_words:
                                    list_of_counts_of_words.append(count_2)
                                    list_of_ru_gen_words.append(generate_word)
                                    count += 1
                                    count_2 += 1
                        if "е" in all_of_letters:
                            all_of_letters = all_of_letters.replace("е", "ё")
                            words = set(itertools.permutations(all_of_letters, r=length_of_words))
                            for word in words:
                                count = 0
                                generate_word = "".join(word)
                                for j in range(len(list_of_ru_words)):
                                    if generate_word == list_of_ru_words[j] and count == 0 and generate_word not in list_of_ru_gen_words:
                                        list_of_counts_of_words.append(count_2)
                                        list_of_ru_gen_words.append(generate_word)
                                        count += 1
                                        count_2 += 1

                        with open("results_gen_ru_words.txt", "w", encoding='utf-8') as f2:
                            f2.write(f"Слова из {length_of_words} букв:\n")
                            for i in range(len(list_of_ru_gen_words)):
                                f2.write(f"{list_of_counts_of_words[i]} слово: {list_of_ru_gen_words[i]}\n")
                        print(f"Count of words: {count_2 - 1}")

            with open('results_gen_ru_words.txt', encoding='utf-8') as f3:
                dpg.delete_item('text_group', children_only=True)
                left_pos = 8
                right_pos = 440
                f3.readline()
                count = 0
                for line in f3.readlines():
                    dpg.add_text(pos=[left_pos, right_pos], default_value=line[:-1], parent='text_group')
                    right_pos += 20
                    count += 1
                    if count == 8:
                        count = 0
                        left_pos += 160
                        right_pos = 440

        combo_values = ["3", "4", "5", "6", "7"]
        dpg.add_text(tag="Text for writing letters", pos=[290, 215], default_value="Write all of letters which do you have:", parent="generator_group")
        dpg.add_input_text(tag="Input all letters", width=270, height=300, pos=[284, 245], parent="generator_group")
        dpg.add_text(tag="Text for choosing length of words", pos=[290, 275], default_value="Choose length of words do you need:", parent="generator_group")
        dpg.add_combo(tag="Input length of words", width=270, pos=[285, 305], items=combo_values, parent="generator_group")
        dpg.add_button(tag="Button for sending parameters", label="Send parameters", callback=print_value, pos=[355, 340], parent="generator_group")
        dpg.add_text(tag="Text for results", pos=[8, 415], default_value="Results:", parent="generator_group")
        dpg.add_image(tag="Image of Elite Degget 1", texture_tag="image_1", pos=[79, 215], parent="generator_group")
        dpg.add_image(tag="Image of Elite Degget 2", texture_tag="image_1", pos=[559, 215], parent="generator_group")
        dpg.draw_line(p1=(-10, 382), p2=(820, 382), parent="generator_group")
        dpg.draw_line(p1=(-4, 382), p2=(-4, 580), parent="generator_group")
        dpg.draw_line(p1=(805, 382), p2=(805, 580), parent="generator_group")
        dpg.draw_line(p1=(-10, 580), p2=(820, 580), parent="generator_group")
        dpg.bind_font(default_font)
        dpg.bind_item_font("Input all letters", default_font)
        with dpg.group(tag='text_group', parent="generator_group"):
             pass
        with dpg.group(tag='mode_group', parent="generator_mode"):
             pass

    def get_info():
        print_name_def("get_info()")

        def open_home_page():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/Superior6564")

        def open_download_url():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/Superior6564/archive/refs/heads/main.zip")

        def open_wiki():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/superior6564/wiki")

        with open("readme.md", "wb") as f:
            f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/README.md').content)

        path = os.getcwd() + "/readme.md"
        line_need = []
        name_need = ["Name", "Vers", "Desc", "Home", "Down", "Wiki", "Auth", "Lice"]

        with open(path) as f:
            for i in range(19):
                line = f.readline()
                if line[:4] in name_need:
                    line_need.append(line)

        with open(path) as f:
            dictionary = {"Name": line_need[0], "Version": line_need[1], "Description": line_need[2],
                          "Home-Page": line_need[3], "Download-URL": line_need[4], "Wiki": line_need[5],
                          "Author": line_need[6], "Author-email": line_need[7], "License": line_need[8]}
        dpg.add_text(tag="Name", pos=[5, 40], default_value=dictionary["Name"], parent="info_group")
        dpg.add_text(tag="Version", pos=[5, 60], default_value=dictionary["Version"], parent="info_group")
        dpg.add_text(tag="Home-Page", pos=[5, 80], default_value=dictionary["Home-Page"][:10], parent="info_group")
        dpg.add_text(tag="Download-URL", pos=[5, 100], default_value=dictionary["Download-URL"][:14], parent="info_group")
        dpg.add_text(tag="Wiki", pos=[5, 120], default_value=dictionary["Wiki"][:6], parent="info_group")
        dpg.add_text(tag="Author", pos=[5, 140], default_value=dictionary["Author"], parent="info_group")
        dpg.add_text(tag="Author-email", pos=[5, 160], default_value=dictionary["Author-email"], parent="info_group")
        dpg.add_text(tag="License", pos=[5, 180], default_value=dictionary["License"][:-19], parent="info_group")
        dpg.add_button(tag="Open Home-Page", label="Open", callback=open_home_page, pos=[100, 80], parent="info_group")
        dpg.add_button(tag="Open Download-URL", label="Open", callback=open_download_url, pos=[120, 100], parent="info_group")
        dpg.add_button(tag="Open Wiki", label="Open", callback=open_wiki, pos=[45, 120], parent="info_group")
        dpg.draw_line(p1=(270, -10), p2=(270, 382), parent="info_group")
        dpg.draw_line(p1=(-10, 180), p2=(270, 180), parent="info_group")

    def install_package():
        print_name_def("install_package()")

        def get_and_install():
            print_name_def("Install of package")
            dpg.delete_item("install_error", children_only=True)
            package = dpg.get_value("Input name of package")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
                print(f"Package {package} installed.")
                dpg.add_text(tag="Good description 1", pos=[285, 160], default_value=f"Package {package} installed.", parent="install_error")
            except subprocess.CalledProcessError:
                print("ERROR: Bad name.")
                print("Write the correct name of the package.")
                dpg.add_text(tag="Error description 1", pos=[285, 160], default_value="ERROR: Bad name.", parent="install_error")
                dpg.add_text(tag="Error description 2", pos=[285, 180], default_value="Write the correct name of the package.", parent="install_error")
            except "Requirement already satisfied":
                print("Requirement already satisfied")

        dpg.add_text(tag="Install package", pos=[285, 20], default_value="Install packages:", parent="install_package")
        dpg.add_text(tag="Install package description", pos=[285, 40], default_value="Write the correct name of the package:", parent="install_package")
        dpg.add_input_text(tag="Input name of package", width=265, height=300, pos=[285, 70], parent="install_package")
        dpg.add_button(tag="Button for sending name of package", label="Send", callback=get_and_install, pos=[285, 105], parent="install_package")
        dpg.add_text(tag="Text for status of installing", pos=[285, 135], default_value="Status:", parent="install_package")
        dpg.draw_line(p1=(270, 180), p2=(550, 180), parent="install_package")
        with dpg.group(tag="install_error"):
            pass

    def pip_upgrade():
        print_name_def("pip_upgrade()")

        def upgrade():
            print_name_def("Pip upgrade")
            dpg.delete_item("pip_upgrade", children_only=True)
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            print("Pip upgraded")
            dpg.add_text(tag="Text of status for pip upgrading", pos=[560, 110], default_value="Pip upgraded", parent="pip_upgrade")

        dpg.add_text(tag="Pip upgrade", pos=[560, 20], default_value="Pip upgrade:", parent="pip_upgrade")
        dpg.add_text(tag="Pip upgrade description", pos=[560, 40], default_value="Click on the button to upgrade pip.", parent="pip_upgrade")
        dpg.add_button(tag="Button for upgrading pip", label="Send", callback=upgrade, pos=[660, 65], parent="pip_upgrade")
        dpg.add_text(tag="Text for status of upgrading", pos=[560, 90], default_value="Status:", parent="pip_upgrade")
        dpg.draw_line(p1=(550, -10), p2=(550, 382), parent="pip_upgrade")
        dpg.draw_line(p1=(550, 180), p2=(820, 180), parent="pip_upgrade")

    with dpg.window(tag='main_window', label="Main", width=820, height=655, no_move=True, no_resize=True, no_close=True):
        dpg.add_text(tag="Information", pos=[5, 20], default_value="Information:")
        get_info()
        generator_ru_words()
        install_package()
        pip_upgrade()
        with dpg.group(tag='info_group'):
            pass
        with dpg.group(tag='generator_group'):
            pass
        with dpg.group(tag='install_package'):
            pass
        with dpg.group(tag="pip_upgrade"):
            pass

    dpg.create_viewport(title='App', width=831, height=655, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
