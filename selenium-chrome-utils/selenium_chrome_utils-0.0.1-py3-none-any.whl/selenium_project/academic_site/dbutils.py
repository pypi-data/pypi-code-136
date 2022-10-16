
import os
import sqlite3
import time
class SqlUtils:
    def __init__(self):
        if not os.path.exists('config'):
            os.makedirs("config")
        self.init()
    def init(self):
        self.cu = sqlite3.connect("config/article.db")
        self.cur = self.cu.cursor()
        self.dbName = 'article'
        self.articledb = 'articleInfo'
        sqls = '''CREATE TABLE If Not Exists %s(
                                "id"	INTEGER NOT NULL UNIQUE,
                                "article_id"	TEXT,
                                key_word TEXT,
                                "insert_time"	timestamp,
                                "update_time"	timestamp,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );''' % self.dbName
        self.cur.execute(sqls)
        self.cu.commit()
        sql = '''CREATE TABLE If Not Exists %s(
                                        "id"	INTEGER NOT NULL UNIQUE,
                                        "author"	TEXT,
                                        link_id     TEXT,
                                        public_date TEXT,
                                        "insert_time"	timestamp,
                                        "update_time"	timestamp,
                                        PRIMARY KEY("id" AUTOINCREMENT)
                                    );''' % self.articledb
        self.cur.execute(sql)
        self.cu.commit()
    def findAll(self):
        sql = "select *  from %s "%self.dbName
        self.cur.execute(sql)
        self.cu.commit()
        fect = self.cur.fetchall()
        return fect
    def close(self):
        self.cur.close()
        self.cu.close()
    def findAppByName(self,articleId):
        try:
            sql = 'select *  from %s where article_id="%s"' % (self.dbName,articleId)
            self.cur.execute(sql)
            self.cu.commit()
            fect = self.cur.fetchone()
            return fect
        except Exception as e:
            print(e)

    def addArticleId(self,articleid,key_word):
        try:
            currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sql = 'insert into %s(key_word,article_id,insert_time) values("%s","%s","%s")' % (self.dbName,
            key_word,articleid,currentTime)
            self.cur.execute(sql)
            self.cu.commit()
            print('添加成功')
        except Exception as e:
            print(e)
            print('添加失败:%s:%s'%(articleid,key_word))
    def addArticleAuthor(self,author,lid,pDate):
        try:
            currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sql = 'insert into %s(author,link_id,public_date,insert_time) values("%s","%s","%s","%s")' % (self.articledb,
            author,lid,pDate,currentTime)
            self.cur.execute(sql)
            self.cu.commit()
            print('添加成功')
        except Exception as e:
            print(e)
            print('添加失败:%s:%s'%(author,pDate))

    def updateByName(self,sku,goods_name,current_price,low_price,update_time):
        sql='update %s set sku="%s" and goods_name="%s" and current_price="%s" and low_price="%s" and update_time="%s" where sku="%s" and goods_name="%s"'%(self.dbName,sku,goods_name,current_price,low_price,update_time,sku,goods_name)
        self.cur.execute(sql)
        self.cu.commit()
    def clearData(self):
        sql="delete from %s"%self.dbName
        self.cur.execute(sql)
        self.cu.commit()
    def deleteByarticleId(self,articleid):
        try:
            sql = 'delete from %s where article_id="%s"' % (self.dbName,articleid)
            self.cur.execute(sql)
            self.cu.commit()
            print('删除成功')
        except Exception as e:
            print(e)
            print('删除失败')

if __name__=="__main__":
    print(float(32.2)>float(9.0))
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # print(currentTime)
    # sql=SqlUtils()
    # # sql.addAmazon('RP-1TPJ-5CLZ','PKQIU High Basketball Shoes High-top Basketball Shoes Sports Shoes Breathable Wear-Resistant Non-Slip Shock-Absorbing for Men and Women Blue, 5.5…B09CPXC9KZ',60.00,50.00,currentTime)
    # f=sql.findAppByName('T1-EAW4-S266',"PKQIU High Basketball Shoes Sneakers Men's Breathable Basketball Sneakers Non-Slip Wear-Resistant White, 5.5")
    # print(f)
    # print(sql.findAll())
    # print(f)