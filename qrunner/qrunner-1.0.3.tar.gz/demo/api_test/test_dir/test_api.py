import qrunner
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
    qrunner.main(
        platform='api',
        base_url='https://www-pre.qizhidao.com'
    )
