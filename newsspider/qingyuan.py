import time, requests, json, pymysql, datetime,redis,hashlib
from lxml import etree
from dingtalkchatbot.chatbot import DingtalkChatbot


class Qingyuan(object):

    def __init__(self, r):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Origin': 'http://yuqing.gsdata.cn'}
        r.headers = self.headers
        self.r = r

    def _login(self):
        u = '18606216606'
        p = ''

        login_url = 'https://u.gsdata.cn/member/ajax_login'
        post_data = {'username': u, 'password': p, 'login_from': 2}
        res = self.r.post(login_url, post_data)
        resp = json.loads(res.text)
        if resp.get('error') == 0:
            return 1
        else:
            self.login_error(self._login.__name__)

    def _yuqing(self):
        yuqing_url = 'http://yuqing.gsdata.cn/yuqingSubscribe/index'
        post_data = {'con': '', 'page': '1', 'sk': ''}
        res = self.r.post(yuqing_url, data=post_data)
        resp = json.loads(res.text)
        # hot_news_list = resp.get('data').get('hot_scheme_list')
        # for n in hot_news_list:
        #     print(n.get('sname'), n.get('sdesc'), n.get('icon'))
        general_news_list = resp.get('data').get('latest_scheme_list')
        for n in general_news_list:
            items = {'title': n.get('sname'), 'desc': n.get('sdesc'), 'pic': n.get('icon'), 'platform': 'yq'}
            yield self.data_inmysql(items)

    def _weixin(self):
        wx_url = 'http://www.gsdata.cn/rank/wxarc?'
        self.r.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}
        res = self.r.get(wx_url)
        resp = etree.HTML(res.text)
        cate_id = resp.xpath('//ul[@id="select-typs"]/li/a/text()')
        for id in cate_id:
            if id != '全部':
                url_wx_cate = 'http://www.gsdata.cn/rank/ajax_wxarc?post_time=2&page=1&types={0}&industry=all&proName='.format(
                    id)
                time.sleep(1)
                yield self.get_wxnew_list(url_wx_cate, id)

    def get_wxnew_list(self, url, id):
        self.r.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'X-Requested-With': 'XMLHttpRequest',
        }
        res = self.r.get(url)
        resps = json.loads(res.text)
        if resps.get('error') == 0:
            resp = etree.HTML(resps.get('data'))
            tr = resp.xpath('//tr')
            for t in tr:
                title = t.xpath('./td[1]//a/text()')[0].replace('\r\n', '').replace('\/', '/')
                href = t.xpath('./td[1]//a/@href')[0].replace('\r\n', '').replace('\/', '/')
                author = t.xpath('./td[2]/text()')[0].replace('\r\n', '').replace('\/', '/')
                reads = t.xpath('./td[3]/text()')[0].replace('\r\n', '').replace('\/', '/')
                items = {'title': title, 'href': href, 'author': author, 'reads': reads, 'platform': 'wx', 'cate': id}
                yield self.data_inmysql(items)

        else:
            self.login_error(self.get_wxnew_list.__name__)

    def _toutiao(self):
        toutiao_url = 'http://www.gsdata.cn/rank/toutiao_arc?'
        res = self.r.get(toutiao_url)
        resp = etree.HTML(res.text)
        toutiao_list_news = resp.xpath("//table[@id='rank_data']/tbody//tr")
        for t in toutiao_list_news:
            title = t.xpath('./td[1]/a/text()')[0]
            href = t.xpath('./td[1]/a/@href')[0]
            author = t.xpath('./td[2]/text()')[0]
            reads = t.xpath('./td[3]/text()')[0]
            items = {'title': title, 'href': href, 'author': author, 'reads': reads, 'paltform': 'tt'}
            yield self.data_inmysql(items)

    def login_error(self, s):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=b618ec29fcaaf30aa429f8634b9a011ce571cef77765391a52f4eb2f6c3e4e40'
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg='清源数据error。error_func：' + s)
        time.sleep(300)
        # xiaoding.send_text(msg=msg)

    def data_inmysql(self, items):

        host = 'localhost'
        port = 6379
        r = redis.Redis(host=host, port=port)
        cate, title, descs, img, paltform, author, readcounts, crawled_time, create_time = items.get('cate'), items.get(
            'title'), items.get(
            'desc'), items.get('pic'), items.get('platform'), items.get('author'), items.get(
            'reads'), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), items.get('create_time')
        m2 = hashlib.md5()
        m2.update(title.encode())
        md5_title = m2.hexdigest()
        if not r.sismember('qy',md5_title):
            r.sadd('qy',md5_title)
            sql = '''INSERT INTO news(news_cate,news_title, news_desc, news_img, news_paltform, news_author, news_readcounts, crawled_time)  VALUES('%s', '%s', '%s', '%s', '%s','%s', '%s', '%s')''' \
                  % (cate, title, descs, img, paltform, author, readcounts, crawled_time)
            sql = sql.replace('None', "Null")
            db = pymysql.connect('localhost', 'root', '123456', 'web')
            cursor = db.cursor()
            # cate, title, descs, img, paltform, author, readcounts, crawled_time, create_time
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                print(sql)
                # self.login_error(self.data_inmysql.__name__)
                db.rollback()
            db.close()
        else:
            print(111111111111)

if __name__ == '__main__':
    r = requests.session()
    a = Qingyuan(r)
    if a._login():
        for i in a._yuqing(): pass
        for i in a._weixin():
            for x in i: pass
        for i in a._toutiao(): pass
