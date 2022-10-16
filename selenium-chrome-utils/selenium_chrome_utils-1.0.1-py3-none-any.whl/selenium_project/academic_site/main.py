# 学术网信息采集
import logging
from threading import Thread
from selenium.webdriver.common.by import By
from selenium_project.academic_site.dbutils import SqlUtils
from selenium_utils.seleniumObject import SeleniumUtils

class AcademicSite(SeleniumUtils):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT, filename='runLog.log',
                        filemode="w")
    def __init__(self):
        super().__init__(debug=True)
        self.sql = SqlUtils()
        # with open('关键词.txt', 'r', encoding='utf8') as f:
        #     data = f.read().split('\n')
        self.keywords = ['w','x']
        self.driver.get('https://www.ncbi.nlm.nih.gov/sra')
    def run(self):
        self.openNewTap()
        self.driver.implicitly_wait(3)
        search=self.find_by_xpath('//*[@id="term"]')
        self.set_text(search,'ww')
        self.click_element(self.find_by_xpath('//*[@id="search"]'))
        # input('请输入完成后按回车键继续:')
        while True:
            articleLinks = self.getAllAtric()
            print(articleLinks)
            for link in articleLinks:
                self.driver.switch_to.window(self.towWin)
                self.driver.get(link['link'])
                Thread(target=self.closePop).start()
                self.getSubmiterAndRun()
                self.sql.addArticleId(link['id'], '')
                print('下一条文章：' + link['id'])
            print('下一页')
            self.driver.switch_to.window(self.win)
            pageno = self.find_by_object(By.XPATH, '//*[@id="pageno"]')
            if pageno is not None:
                with open('page.txt', 'w', encoding='utf') as f:
                    f.write('当前浏览到:' + pageno.get_attribute('value'))
            result = self.nextPage()
            if not result:
                print('浏览完毕')
                return

    def nextPage(self):
        next = self.find_by_object(By.XPATH, '//*[text()="Next >"]')
        # next=self.find_by_object(By.XPATH,'//*[@id="EntrezSystem2.PEntrez.Sra.Sra_ResultsPanel.Entrez_Pager.Page"]')
        result = self.click_element(next)
        if result is False:
            self.logger.warning('翻页失败')
            return False
        else:
            self.logger.info('翻页成功')
            return True

    def openNewTap(self):
        self.win = self.driver.current_window_handle
        self.driver.switch_to.new_window()
        self.towWin = self.driver.current_window_handle
        print(self.driver.title)
        self.driver.switch_to.window(self.win)
        print(self.driver.title)
    # 获取所有的文章
    def getAllAtric(self):
        articles = self.finds_by_object(By.XPATH, '//div[@class="rprt"]')
        allLinks = []
        for article in articles:
            a = article.find_element(By.XPATH, 'div[2]/p/a')
            id = article.find_element(By.CLASS_NAME, 'rprtid').text.split(":")[1].replace(" ", "")
            result = self.sql.findAppByName(id)
            if result is not None:
                self.logger.warning('此文章已浏览过:' + id)
                continue
            temp = {}
            temp['id'] = id
            temp['link'] = a.get_attribute('href')
            allLinks.append(temp)
        return allLinks
    # common
    def getSubmiterAndRun(self):
        artier = self.find_by_object(By.XPATH, '//*[@id="ResultView"]/div[2]/span')
        #     //*[@id="ResultView"]/table/tbody/tr
        print(artier.text)
        name = artier.text
        runLog = self.finds_by_object(By.XPATH, '//*[@id="ResultView"]/table/tbody/tr')
        allViewLinks = []
        print('查询所有的run记录')
        logging.error("查询所有的run记录")
        for viewLink in runLog:
            link = viewLink.find_element(By.XPATH, 'td/a')
            date = viewLink.find_element(By.XPATH, 'td[5]').text
            print(link.get_attribute('href'))
            temp = {}
            temp['link'] = link.get_attribute('href')
            temp['date'] = date
            temp['linkId']=link.text
            allViewLinks.append(temp)
        logging.error("获得所有的run记录:")
        logging.error(allViewLinks)
        self.logger.info('开始搜索关键词')
        for link in allViewLinks:
            self.viewRunlog(link, name)
        print(allViewLinks)
    # 第三步
    def viewRunlog(self, link=None, name=None):
        self.driver.get(link['link'])
        try:
            analysis = self.find_by_object(By.XPATH, '//*[@id="ph-run_browser"]/div[2]/a[2]')
            self.click_element(analysis)
            viruses = self.find_by_object(By.XPATH, '//*[@id="ph-run-browser-analysis-tree"]/div[2]/ul/li[2]/div/b')
            self.click_element(viruses)
            nodes = self.finds_by_object(By.XPATH, '//*[@id="ph-run-browser-analysis-tree"]/div[2]/ul/li[2]/ul/li')
            for node in nodes:
                nodeNames = node.text.split("\n")
                for n in nodeNames:
                    nodeName = n.split(':')[0]
                    for keyword in self.keywords:
                        if keyword in nodeName and keyword != "":
                            print('找到了')
                            logging.error('找到了关键词:' + keyword)
                            self.sql.addArticleAuthor(name,link['linkId'], link['date'])
                            return True
            self.logger.error('没有找到关键词')
            logging.error('没有找到关键词')
            return False
        except Exception as e:
            print(e)
            self.logger.error('查询关键词失败')
            logging.error(e)
            return False
    def closePop(self):
        self.driver.implicitly_wait(1)
        close = self.find_by_object(By.XPATH, '//*[text()="No Thanks"]',log_print=False)
        self.driver.implicitly_wait(3)
        if close is None:
            return
        self.click_element(close)

if __name__ == '__main__':
    g = AcademicSite()
    g.run()
