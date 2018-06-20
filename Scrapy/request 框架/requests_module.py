# import requests
#
# r = requests.get("http://www.baidu.com")
#
# print(r.text)


import requests
r = requests.get("http://www.baidu.com")

'''
Response(self)

The :class:Response <Response> object, which contains a server's response to an HTTP request.

'''
#HTTP请求的返回状态，比如，200表示成功，404表示失败
print (r.status_code)
#HTTP请求中的headers
print (r.headers)
#从header中猜测的响应的内容编码方式
print (r.encoding)
#从内容中分析的编码方式（慢）
print (r.apparent_encoding)
#响应内容的二进制形式
print (r.content)
