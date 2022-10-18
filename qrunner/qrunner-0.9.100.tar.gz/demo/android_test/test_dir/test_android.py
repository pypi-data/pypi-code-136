import qrunner
from qrunner import story, title


class HomePage(qrunner.Page):
    LOC_AD_CLOSE = {'id_': 'id/bottom_btn', 'desc': '首页广告关闭按钮'}
    LOC_MY = {'id_': 'id/bottom_view', 'index': 3, 'desc': '首页底部我的入口'}
    
    def go_my(self):
        self.elem(self.LOC_AD_CLOSE).click()
        self.elem(self.LOC_MY).click()


@story('首页')
class TestClass(qrunner.TestCase):
    
    def start(self):
        self.hp = HomePage(self.driver)
    
    @title('从首页进入我的页')
    def testcase(self):
        self.start_app()
        self.hp.go_my()
        self.assertText('我的订单')
        self.stop_app()


if __name__ == '__main__':
    qrunner.main(
        platform='android',
        device_id='UJK0220521066836',
        pkg_name='com.qizhidao.clientapp'
    )
