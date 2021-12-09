import web
from PIL import Image
import zqr
import time
import os
site = "http://ifist.tech:8080"

urls = (
    '/' , 'index' ,
    '/upload', 'upload',
    '/redirect','redirect'
    )
class index:
    def GET(self):
        a = web.input(url={})
        astr = a['url']
        if(len(astr) != 0):
            print(astr)
            f = open("top.html",encoding='UTF-8')
            top = f.read()
            f.close()
            f = open("bottom.html",encoding='UTF-8')
            bottom = f.read()
            f.close()
            f = open(astr+".txt",encoding='UTF-8')
            a = f.readline().split('\n')[0]
            b = f.readline().split('\n')[0]
            f.close()
            print(a,b)
            return top+"\nvar iosLinkUrl=\""+a+"\"\n" + "var androidLinkUrl=\"" + b + "\"\n" + bottom
        else:
            f = open("index.html",encoding='UTF-8')
            return f.read()
class upload:
    def POST(self):
        t = time.time()
        id = str(t).split('.')[0]

        x = web.input(file={})
        fileName = x['file'].filename
        ext = os.path.splitext(fileName)[1]
        fn = id+ext
        print(fn)
        a = web.input(ios_url={})
        b = web.input(android_url={})
        ios_url = a['ios_url']
        android_url = b['android_url']
        fpath = "./"+fn
        with open(fpath, 'wb') as f:
            f.write(x['file'].value)
            #f.close()
        logo = Image.open(fpath)
        logo = logo.convert('RGB')
        fn = id+'.png'

        zqr.proc(site+"/?url="+id,logo,fn)

        with open(id+".txt", "w") as f:
            f.write(ios_url)
            f.write("\n")
            f.write(android_url)
            f.write("\n")
            #f.close() with open 不需要close
        f = open(fn,'rb')
        return f.read()

class redirect:
    def GET(self):
        f = open("top.html",encoding='UTF-8')
        top = f.read()
        f.close()
        f = open("bottom.html",encoding='UTF-8')
        bottom = f.read()
        f.close()
        a = web.input(url={})
        print(a['url'])
        #f = open("bottom.html",encoding='UTF-8')
        #bottom = f.read()

        #middle = ""
        return "hekl"




app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
