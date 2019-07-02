import time
from datetime import datetime
from App import db, uid
from models import Article, Category, Tag, Status, Secret
from sqlalchemy import and_, func

'''
:func >  json mysql
:logic > 取出当前展示所有的文章数counts，取出最后一条文章lid， 新取出的文章数条件：int(lid)<Article.articls_id<int(lid)+25
:return >  返回10条新的文章记录
'''
def json_mysql(lid,cid):

    lid = db.session.query(Article).filter(lid == Article.articls_title).first().articls_id
    if cid ==4:
        articles_1 = db.session.query(Article).filter(
            and_(Article.category_id < cid, int(lid) < Article.articls_id)).limit(10).all()
    else:
        articles_1 = db.session.query(Article).filter(
            and_(Article.category_id == cid, int(lid) < Article.articls_id)).limit(10).all()
    for i in range(len(articles_1)): articles_1[i].articls_posttime = str(articles_1[i].articls_posttime)
    articles_list = [{'title': art.articls_title, 'create_time': art.articls_posttime, 'des': art.articls_desc,
                      'cate': art.category.category_title, 'pic': art.articls_headimg, 'cid': art.articls_id} for art in
                     articles_1]
    return articles_list

'''
:func >  json mysql
:logic > 反爬
return > 总数及最后一篇文章id
'''
def get_counts_lid(timestamp,request):
    t = int(time.time())
    dt1 = datetime.utcfromtimestamp(int(timestamp))
    dt2 = datetime.utcfromtimestamp(t)
    if (dt2 - dt1).seconds < 15000:  # 3.5小时内,根据path传入内容
        counts = request.args.get('length')
        lid = request.args.get('lid')
        return counts, lid
    else:
        return None, None


