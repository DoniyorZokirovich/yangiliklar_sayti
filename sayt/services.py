from contextlib import closing
from django.db import connection

def dict_fetchall(cursor):
    ustun = []
    for i in cursor.description:
        ustun.append(i[0])
    a = cursor.fetchall()
    img = None
    if "img" in ustun:
        img = ustun.index('img')

    natija = []
    for i in a:
        i = list(i)
        if img:
            i[img]="http://127.0.0.1:8000/media/"+i[img]
        b = dict(zip(ustun, i))
        natija.append(b)
    return natija

def get_all_ctg():
    sql = 'select * from sayt_category where is_menu = true'

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dict_fetchall(cursor)
        return result

def search_new(savol):
    sql = f"""
select ne.id ,ne.title , ne.short_des, ne.img, ne."view", ctg.name as ctg_name  from sayt_new ne
left join sayt_category ctg on ctg.id = ne.cate_id 
where  lower(ne.title) like lower('%{savol}%') 

order by "view" desc
"""
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dict_fetchall(cursor)
        return result
