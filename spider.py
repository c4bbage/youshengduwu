# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

# import requests
# headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'Host':'zhannei.baidu.com',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
# mc = "mc_3"
# for i in range(100):
#     response = requests.get("http://www.whxywh.cn/{}/{}.png".format(mc,i),headers=headers)
#     if response.status_code == 200:
#         print(i)
#         with open("{}/{}.png".format(mc,i),'w') as f:
#             f.write(response.content)
#             response = requests.get("http://www.whxywh.cn/{}/{}.mp3".format(mc,i),headers=headers)
#             with open("{}/{}.mp3".format(mc,i),'w') as f:
#                 f.write(response.content)
step =3
total=41
f = open('index.html','w')
f.write("<html><body><table>\n")
for i in range(1,total,step):
    f.write('   <tr class="img">\n')
    for a in range(step):
        if i+a>=total:
            break
        f.write('       <td><a href="mc_2.html?{}"><img src="mc_2/{}.png" /></a></td>\n'.format(i+a,i+a))
    f.write("   </tr>\n")
f.write("</table></body></html>")
f.close()