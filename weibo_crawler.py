#!/usr/bin/env python
# _*_ UTF-8 _*_

import weibo
import urllib
import urllib2
import re
import time

def weibo():
    APP_KEY = "2282143806"
    APP_SECRET = "bae8982e5539f7426ef2f71f553b514e"
    CALLBACK_URL = "http://api.weibo.com/livan/default.html"
    AUTH_URL = "http://api.weibo.com/livan/default.html"
    USERID = "2577633693"
    PASSWD = "xujingboyy123"

    client = weibo.APIClient(app_key=APP_KEY,
                             app_secret=APP_SECRET,
                             redirect_uri=CALLBACK_URL)

    referer_url = client.get_authorize_url()
    print "referer url is: %s" % refer_url

    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)
    postdata = {
        "client_id":APP_KEY,
        "userId":USERID,
        "passwd":PASSWD,
        "isLoginSina":"0",
        "action":"submit",
        "response_type":"code",
    }

    headers = {
        "User-Agent":"",
        "Host":"api.weibo.com",
        "Referer":referer_url
    }

    req = urllib2.Request(
        url = AUTH_URL,
        data = urllib.urlencode(postdata),
        headers = headers
    )

    try:
        resp = urllib2.urlopen(req)
        print "callback url is: %s" % resp.geturl()
        pat = "code=(.*?)$"
        print(resp.geturl())
        code = input()
        print "code is : %s" % code
    except Exception, e:
        print e

    r = client.request_access_token(code)
    access_token1 = r.access_token
    expires_in = r.expires_in

    print "access_token=", access_token1
    print "expires_in=", expires_in
    client.set_access_token(access_token1, expires_in)
    return client, access_token1

# 定义确定转发页面数量的函数：
def getPageNum(mid):
    count = client.get.statuses__count(ids = mid)
    repostNum = count[0]['reposts']
    if repostNum%200 ==0:
        pages = repostNum/200
    else:
        pages = int(repostNum/200)+1
    return pages

# 定义抓取转发的函数：
def getReposts(mid, page):
    r = client.get.statuses__profile_list(access_token=mid, uid = , capital="A")
    print("r:"+str(r))
    if len(r) == 0:
        pass
    else:
        m = int(len(r['reposts'])) # 该页面里的微博转发数量
    try:
        for i in range(0, m): # 使用for循环遍历该页面里的所有转发微博
            #转发微博的属性
            mid = r['reposts'][i].id
            text = r['reposts'][i].text.replace(",","")
            created = r['reposts'][i].created_at
            reposts_count = r['reposts'][i].comments_count

            # 微博转发者的属性
            user = r['reposts'][i].user
            user_id = user.id
            user_name = user.name
            user_province = user.province
            user_city = user.city
            user_gender = user.gender
            user_url = user.url
            user_followers = user.followers_count
            user_friends = user.friends_count
            user_statuses = user.statuses_count
            user_created = user.created_at
            user_verified = user.verfied

            # 原微博的属性
            rts = r['reposts'][i].retweeted_status
            rts_mid = rts.id
            rts_created = rts.created_at
            rts_reposts_count = rts.reposts_count
            rts_comments_count = rts.comments_count

            # 原微博发出者的属性
            rtsuser_id = rts.user.id
            rtsuser_name = rts.user.name
            rtsuser_province = rts.user.province
            rtsuser_city = rts.user.city
            rtsuser_gender = rts.user.gender
            rtsuser_url = rts.user.url
            rtsuser_followers = rts.user.followers_count
            rtsuser_friends = rts.user.friends_count
            rtsuser_statuses = rts.user.statuses_count
            rtsuser_created = rts.user.created_at
            rtsuser_verfied = rts.user.verfied
            timePass = clock()-start
            if round(timePass) % 2 == 0:
                print mid, rts_mid, "I have been working for %s seconds" % round(timePass)
                time.sleep(random.randrange(3, 9, 1))
            print >>dataFile, "%s, '%s', %s" % (mid, created, text)

    except Exception, e:
        print >>sys.stderr, 'Encountered Exception:', e, page
        time.sleep(120)
        pass

client, access_token1 = weiboClient() # 连接到API接口
# mid为微博的mid，即在转发——私信中确定的路径后几位。
mid = client.get.statuses__queryid(mid = 'EqXcf9AyW', isBase62 = 1, type = 1)['id']
mid = "EqXKmhj85"
# 定义存储文档地址
dataFile = open("F:/python_workspace/file/weibo/weibo_repost_all.csv", "wb")
pageNum = 10
for page in range(1, pageNum+1):
    thisdata = getReposts(access_token1, page)
    print(thisdata)
dataFile.close()



































































    







