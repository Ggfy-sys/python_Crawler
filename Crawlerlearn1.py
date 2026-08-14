# 简易html爬虫(含文件存档)
# from urllib.request import urlopen

# url = "https://www.baidu.com"   #百度

# response = urlopen(url)
# html = response.read()

# with open("baidu.html", "w", encoding="utf-8") as f:
#     f.write(html.decode("utf-8"))
# print("over")
# resp.close()  #关闭连接

# 爬虫翻译
# import requests

# url = "https://fanyi.baidu.com/sug"  #翻译网页

# s = input("请输入要翻译的单词：")
# dat = {                              #词典
#     "kw": s
# }

# #发送post请求
# resp = requests.post(url, data=dat)

# print(resp.json())  #打印返回的json数据
# resp.close()  #关闭连接

# 搜狗爬虫（小反爬）
# import requests

# query = input("请输入要搜索的内容：")

# url =  "https://www.sogou.com/web?query={query}"  #搜狗搜索
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
# }

# resp = requests.get(url, headers=headers)  #发送get请求

# print(resp) 
# print(resp.text)  #打印返回的网页源码
# resp.close()  #关闭连接

# requests入门（伪装）
# import requests

# url = "https://movie.douban.com/j/chart/top_list"  #豆瓣喜剧电影排行

# #重新封装参数
# params = {
#     "type": 24,
#     "interval_id": "100:90",
#     "action": "",
#     "start": 0,
#     "limit": 20
# }

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
# }

# resp = requests.get(url, params=params, headers=headers)  #发送get请求

# print(resp.json())  #打印返回的json数据
# resp.close()  #关闭连接
