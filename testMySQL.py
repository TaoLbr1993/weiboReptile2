#-*- coding:utf-8 –*-
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',charset='utf8')
cursor=conn.cursor()

cursor.execute('use test')
#cursor.execute('create table test (id CHAR(50),time DATETIME, content TEXT) ENGINE=MyISAM DEFAULT CHARSET=gbk')
#cursor.execute(u"""insert into test (..,2014-07-24 10:10,<img src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/)""")
mid= u"兲芐烏鴉1瘢黒";
print mid;
time='2014-07-24 10:10'
#cursor.execute(u'insert into test (..,2014-07-24 10:10,)')
content='<img src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/91\/lazu_org.gif\" title=\"[蜡烛]\" alt=\"[蜡烛]\" type=\"face\" \/>而我们的连尸体都找不到，唉..\/\/<a href=\"\/n\/%E5%A7%9A%E6%99%A8\" usercard=\"name=姚晨\" >@姚晨<\/a>: 对生命的敬畏。<img src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/91\/lazu_org.gif\" title=\"[蜡烛]\" alt=\"[蜡烛]\" type=\"face\" \/> \/\/<a href=\"\/n\/%E6%96%B0%E6%B5%AA%E8%A7%86%E9%A2%91\" usercard=\"name=新浪视频\" >@新浪视频<\/a>:以尊严，送别逝者。<img src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/91\/lazu_org.gif\" title=\"[蜡烛]\" alt=\"[蜡烛]\" type=\"face\" \/>'
para=(mid,time,content)
cursor.execute(u'insert into test (id,time,content) values(%s,%s,%s)',para)


#cursor.execute(u'insert into test (id,time,content) values(asdf,2014-07-24 10:10,img)')
conn.commit()
cursor.close()