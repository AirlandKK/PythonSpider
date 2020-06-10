import sqlite3
import requests, time,random
import urllib3

urllib3.disable_warnings()

db = '../db.sqlite3'
table = 'pyjobs_pythonjob'
conn = sqlite3.connect(db)
c = conn.cursor()


# sql = 'select * from pyjobs_pythonjob'
# data = c.execute(sql)
# for i in data:
#     print(i[0], i[1])
def get_position(pn):
    # 原始的url
    urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    # keyword = 'linux'
    payload = {
        'first': 'true',
        'pn': '%s' % pn,
        # 'kd': 'linux',
        'kd': 'python',
    }
    # print(payload)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
    # 建立session
    s = requests.Session()
    # 获取搜索页的cookies
    s.get(urls, headers=header, timeout=3, verify=False)
    # 请求的URL
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    # 为此次获取的cookies
    cookie = s.cookies
    # 获取此次json数据
    response = s.post(url, data=payload, headers=header, cookies=cookie, timeout=5, verify=False).json()
    # print(response)
    res_li = response['content']['positionResult']['result']
    time.sleep(random.random())
    # print(res_li)
    for res in res_li:
        # 职位名称
        positionName = res['positionName']
        # 公司名称
        companyFullName = res['companyFullName']
        # 公司规模
        companySize = res['companySize']
        # 需要的学历
        education = res['education']
        # 工作经验
        workYear = res['workYear']
        # 技能需求
        skillLables = ','.join(res['skillLables'])
        if not skillLables:
            skillLables = '无'
        # 工资
        salary = res['salary']
        # print(res['companyId'])

        try:
            # 公司所在地
            address = res.get('city', '')
        except TypeError:
            address = '其他'
        # 职位发布时间
        createTime = res['createTime']

        # print(positionName, companyFullName, companySize, education, workYear, skillLables, salary, address, createTime)
        sql = 'insert into pyjobs_pythonjob values(null,"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(
            positionName, companyFullName, companySize, education, workYear, skillLables, salary, address, createTime)
        c.execute(sql)
        conn.commit()


if __name__ == '__main__':
    for pn in range(50):
        get_position(pn)
    c.close()
    conn.close()
