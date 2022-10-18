import qrunner
from qrunner import story, title


class PatentPage(qrunner.Page):
    url = None
    LOC_SEARCH_INPUT = {'id_': 'driver-home-step1', 'desc': '查专利首页输入框'}
    LOC_SEARCH_SUBMIT = {'id_': 'driver-home-step2', 'desc': '查专利首页搜索确认按钮'}
    
    def simple_search(self):
        self.elem(self.LOC_SEARCH_INPUT).set_text('无人机')
        self.elem(self.LOC_SEARCH_SUBMIT).click()


@story('专利检索')
class TestClass(qrunner.TestCase):
    
    def start(self):
        self.pp = PatentPage(self.driver)
    
    @title('专利简单检索')
    def testcase(self):
        self.pp.open()
        self.pp.simple_search()
        self.assertTitle('无人机专利检索-企知道')


if __name__ == '__main__':
    qrunner.main(
        platform='web',
        base_url='https://patents.qizhidao.com/'
    )
