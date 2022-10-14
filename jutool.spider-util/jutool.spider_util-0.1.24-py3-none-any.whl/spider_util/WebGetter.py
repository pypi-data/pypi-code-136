import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from code_util.log import log_error


# driver = webdriver.Chrome('/Users/jiangke/Code/Python/basepackage/chromedriver')
# curr_handle = driver.current_window_handle
# driver.get("https://www.baidu.com")
# driver.execute_script('''window.open("", "_blank");''')
# driver.switch_to.window(driver.window_handles[-1])
# driver.get("https:/www.taobao.com")
# hanlders=driver.window_handles
# time.time()

class BrowserSession():
    def __init__(self, drive_path):
        self.driver = webdriver.Chrome(drive_path)
        self.blank_state = True

    def __del__(self):
        self.driver.quit()

    def _get_new_tab(self):
        if self.blank_state:
            self.blank_state = False
            return self.driver.current_window_handle
        else:
            self.driver.execute_script('''window.open("", "_blank");''')
            return self.driver.window_handles[-1]

    def get_web_page(self, url):
        new_handle = self._get_new_tab()
        self.driver.switch_to.window(new_handle)
        self.driver.get(url)
        return web_page(self.driver, new_handle, url)


class page_item():
    def __init__(self, xpath, page, driver):
        self.Xpath = xpath
        self._driver = driver
        self._page = page
        self.item = self._driver.find_element(by=By.XPATH, value=self.Xpath)

        self.text = self.item.text
        if self.text == '':
            self.text = self.item.accessible_name
        self.class_value = self.item.get_attribute("class")

    def __str__(self):
        return f"{self.text} -> {self.class_value}"

    def click(self):
        current_tab_count = len(self._driver.window_handles)
        self.item.click()

        if current_tab_count == len(self._driver.window_handles):
            return self._page
        else:
            new_handle = self._driver.window_handles[-1]
            return web_page(self._driver, new_handle, self._driver.current_url)


class web_page():
    def __init__(self, driver, window_handle, url: str):
        self.driver = driver
        self.handle = window_handle
        self.url = url

    def parse_page(self, parse_content_xpath_dic: {}):

        if len(parse_content_xpath_dic) == 0:
            log_error("需要解析的目标")
        else:
            fxpath = [key for key in parse_content_xpath_dic.values()][0].replace('*', '')

        self.driver.switch_to.window(self.handle)
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, fxpath)))

        result_xpath_list = {}
        for url_key in parse_content_xpath_dic.keys():
            url = parse_content_xpath_dic[url_key]
            url_cuted, url_element_name, url_cuted_class, url_index = self._split_xpath(url)
            result_current_key_list = []

            tree_base_node = ['/' + url_element_name[0]]
            for i in range(1, len(url_element_name)):
                if url_index[i] == 0:
                    # tree_base_node = [x + '/' + url_element_name[i] for x in tree_base_node]
                    new_tree_base_node = []
                    for x in tree_base_node:
                        path = x + '/' + url_element_name[i]
                        if self._has_item_by_xpath(path):
                            new_tree_base_node.append(path)
                    tree_base_node = new_tree_base_node
                else:
                    new_tree_base_node = []
                    for tbn_item in tree_base_node:
                        counter = 1
                        while True:
                            new_xpath = f"{tbn_item}/{url_element_name[i]}[{counter}]"
                            if self._has_item_by_xpath(new_xpath):
                                new_tree_base_node.append(new_xpath)
                                counter += 1
                            else:
                                break
                    tree_base_node = new_tree_base_node

            for tbn_item in tree_base_node:
                item = self.driver.find_element(by=By.XPATH, value=tbn_item)
                class_value = item.get_attribute("class")
                if class_value == url_cuted_class[-1]:
                    result_current_key_list.append(tbn_item)

            result_xpath_list[url_key] = [page_item(x, self, self.driver) for x in result_current_key_list]

        return result_xpath_list

    def scroll_parse_page(self, parse_content_xpath: str, max_length=100):
        scroll_pre_result = self.parse_page({'v': parse_content_xpath})

        if len(scroll_pre_result['v']) < 2:
            log_error("一个返回元素无法进行增量分析")

        url_cuted, url_element_name, url_cuted_class, index_list1 = self._split_xpath(scroll_pre_result['v'][0].Xpath)
        _, _, _, index_list2 = self._split_xpath(scroll_pre_result['v'][-1].Xpath)

        ## 找增量
        delta_count = 0
        delta_index = -1
        index = 0
        for x, y in zip(index_list1, index_list2):
            if x == y:
                pass
            else:
                delta_count += 1
                delta_index = index
            index += 1

        if delta_count != 1:
            log_error("多个增量元素")

        def generation_delta_xpath(element_name, index_list):
            str_path = "/"
            for e_name, i in zip(element_name, index_list):
                if i == 0:
                    str_path += e_name + "/"
                else:
                    str_path += f"{e_name}[{i}]" + "/"
            return str_path[0:-1]

        all_result = []
        self.driver.switch_to.window(self.handle)
        i_count = 0
        while True:
            index_gen_list = [x for x in index_list1]
            index_gen_list[delta_index] += i_count
            path = generation_delta_xpath(url_element_name, index_gen_list)
            if self._has_item_by_xpath(path):
                all_result.append(page_item(path, self, self.driver))
                i_count += 1
            else:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                try:
                    WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, path)))
                except:
                    break

            if len(all_result) > max_length:
                break
        return all_result

    def _split_xpath(self, xpath):
        url = xpath
        url_cuted = [x for x in url.split('/') if x]
        url_element_name = []
        url_cuted_class = []
        url_index = []

        for i in range(len(url_cuted)):
            new_xpath = "/" + "/".join(url_cuted[0:i + 1])
            item = self.driver.find_element(by=By.XPATH, value=new_xpath.replace('*', ''))
            url_cuted_class.append(item.get_attribute("class"))
            if '[' not in url_cuted[i] or url_cuted[i][-1] == '*':
                url_index.append(0)
                if not url_cuted[i][-1] == '*':
                    url_element_name.append(url_cuted[i])
                else:
                    url_element_name.append(url_cuted[i][0:-1])
            else:
                split_temp = url_cuted[i].split('[')
                url_element_name.append(split_temp[0])
                url_index.append(int(split_temp[1][:-1]))

        return url_cuted, url_element_name, url_cuted_class, url_index

    def _has_item_by_xpath(self, path):
        f_items = self.driver.find_elements(by=By.XPATH, value=path)
        if len(f_items) > 0:
            return True
        else:
            return False

    def __del__(self):
        self.driver.switch_to.window(self.handle)
        self.driver.close()
