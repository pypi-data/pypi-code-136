import os.path

run_content = """import qrunner


if __name__ == '__main__':
    qrunner.main(
        base_url='https://www-pre.qizhidao.com',
        android_id='UJK0220521066836',
        android_pkg='com.qizhidao.clientapp',
        ios_id='00008101-000E646A3C29003A',
        ios_pkg='com.qizhidao.company'
    )
"""

case_content_android = """import qrunner
from qrunner import AndroidElement, story, title


class HomePage:
    ad_close_btn = AndroidElement(id_='id/bottom_btn', desc='首页广告关闭按钮')
    bottom_my = AndroidElement(id_='id/bottom_view', index=3, desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.AndroidTestCase):
    
    def start(self):
        self.hp = HomePage()
    
    @title('从首页进入我的页')
    def testcase(self):
        self.start_app()
        self.hp.ad_close_btn.click_exists(timeout=5)
        self.hp.bottom_my.click()
        self.assertText('我的订单')
        self.stop_app()


if __name__ == '__main__':
    qrunner.main(
        android_id='UJK0220521066836',
        android_pkg='com.qizhidao.clientapp'
    )
"""

case_content_ios = """import qrunner
from qrunner import IosElement, story, title


class HomePage:
    ad_close_btn = IosElement(label='close white big', desc='首页广告关闭按钮')
    bottom_my = IosElement(label='我的', desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.IosTestCase):

    def start(self):
        self.hp = HomePage()

    @title('从首页进入我的页')
    def testcase(self):
        self.start_app()
        self.hp.ad_close_btn.click_exists(timeout=5)
        self.hp.bottom_my.click()
        self.assertText('我的订单')
        self.stop_app()


if __name__ == '__main__':
    qrunner.main(
        ios_id='00008101-000E646A3C29003A',
        ios_pkg='com.qizhidao.company'
    )
"""

case_content_web = """import qrunner
from qrunner import WebElement, story, title, Page


class PatentPage(Page):
    url = None
    search_input = WebElement(id_='driver-home-step1', desc='查专利首页输入框')
    search_submit = WebElement(id_='driver-home-step2', desc='查专利首页搜索确认按钮')


@story('专利检索')
class TestClass(qrunner.WebTestCase):
    
    def start(self):
        self.pp = PatentPage(self.driver)
    
    @title('专利简单检索')
    def testcase(self):
        self.pp.open()
        self.pp.search_input.set_text('无人机')
        self.pp.search_submit.click()
        self.assertTitle('无人机专利检索-企知道')


if __name__ == '__main__':
    qrunner.main(base_url='https://patents-pre.qizhidao.com/')
"""

case_content_api = """import qrunner
from qrunner import title, file_data, story


@story('PC站首页')
class TestClass(qrunner.TestCase):

    @title('查询PC站首页banner列表')
    @file_data('card_type', 'data.json')
    def test_getToolCardListForPc(self, card_type):
        path = '/api/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
        payload = {"type": card_type}
        self.post(path, json=payload)
        self.assertEq('code', 0)

if __name__ == '__main__':
    qrunner.main(base_url='https://www-pre.qizhidao.com')
"""

data_content = """{
  "card_type": [0, 1, 2]
}
"""


def create_scaffold(project_name):
    """ create scaffold with specified project name.
    """

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    create_folder(project_name)
    # 新增测试用例目录
    create_folder(os.path.join(project_name, 'test_dir'))
    create_file(
        os.path.join(project_name, 'test_dir', "__init__.py"),
        '',
    )
    # 新增测试数据目录
    create_folder(os.path.join(project_name, 'test_data'))
    create_file(
        os.path.join(project_name, 'test_data', "data.json"),
        data_content,
    )
    # 新增框架入口程序
    create_file(
        os.path.join(project_name, "run.py"),
        run_content,
    )
    # 新增接口测试用例
    create_file(
        os.path.join(project_name, 'test_dir', "test_api.py"),
        case_content_api,
    )
    # 新增安卓测试用例
    create_file(
        os.path.join(project_name, 'test_dir', "test_adr.py"),
        case_content_android,
    )
    # 新增ios测试用例
    create_file(
        os.path.join(project_name, 'test_dir', "test_ios.py"),
        case_content_ios,
    )
    # 新增web测试用例
    create_file(
        os.path.join(project_name, 'test_dir', "test_web.py"),
        case_content_web,
    )



