import urllib
import urllib.request

#总共586话

def downImage():

    for n in range(587):
        print('n=%s' % n)

        for m in range(20):
            print('m=%s' %  m)
            #把文件读取
            linkUrl = "http://mhpic.manhualang.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E6%8B%86%E5%88%86%E7%89%88%2F" + '%d' %n + "%E8%AF%9D%2F" + '%d' %m + ".jpg-smh.middle";
            down(linkUrl,n,m)


def down(linkUrl,n,m):
    try:
        req = urllib.request.Request(linkUrl);
        codeFile = urllib.request.urlopen(req).read();
        print(codeFile)
        # 保存本地
        with open('斗罗大陆%d话%d页.png' % (n, m), 'wb') as fn:
            fn.write(codeFile)

    except BaseException:
        print('出现异常')



downImage()