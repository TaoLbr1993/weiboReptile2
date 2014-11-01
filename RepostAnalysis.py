#-*- coding:utf-8 –*-
import os
import MySQLdb
import re
def get_repost(content):
    pattern=re.compile(r'''\\/\\/<a.*?href=.*?>@(.*?)<\\/a>''')
    res=pattern.search(content)
    if res == None:
        return None
    return res.group(1)
def set_polvl_table(cursor,table):
    cursor.execute("select * from %s where polvl is NULL;" % table)
    repolist=cursor.fetchall();
    #print repolist;
    for repo in repolist[::-1]:
        pofrom=repo[3]
        pofromlvl=get_polvl(cursor,table,pofrom)
        if pofromlvl==-1:
            polvl=-1;
        else:
            polvl=pofromlvl+1;
        cursor.execute("update %s set polvl=%s where id='%s';"%(table,polvl,repo[0]))
        
def set_polvl_database(cursor,database):
    cursor.execute("use %s;" % database)
    cursor.execute("show tables;")
    tablelist=cursor.fetchall()
    #print tablelist
    for table in tablelist:
        set_polvl_table(cursor,table[0])
        
def get_polvl(cursor,table,reponame):
    cursor.execute("select polvl from %s where id='%s'  order by time limit 1;" % (table,reponame))
    repoform=cursor.fetchall()
    if repoform==None or repoform==():
        return -1;
    #print repoform
    return repoform[0][0]

if __name__=='__main__':
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',charset='utf8')
    cursor=conn.cursor()
    
    set_polvl_database(cursor,'userid1260555362')
    #cursor.execute("use userid3229125510;")
    
    
