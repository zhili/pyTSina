# coding=utf-8
import urllib,urllib2
import re
import cookielib
# def unescape(text):
#    """Removes HTML or XML character references 
#       and entities from a text string.
#    from Fredrik Lundh
#    http://effbot.org/zone/re-sub.htm#unescape-html
#    """
#    def fixup(m):
#        text = m.group(0)
#        if text[:2] == "&#":
#            # character reference
#            try:
#                if text[:3] == "&#x":
#                    return unichr(int(text[3:-1], 16))
#                else:
#                    return unichr(int(text[2:-1]))
#            except ValueError:
#                pass
#        else:
#            # named entity
#            try:
#                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
#            except KeyError:
#                pass
#        return text # leave as is
#    return re.sub("&#?\w+;", fixup, text)

def send_sina_msgs(username,password,msg):
      cj = cookielib.CookieJar()
      opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
      urllib2.install_opener(opener)      
      result = urllib2.urlopen(url="https://login.sina.com.cn/sso/login.php?username=%s&password=%s&returntype=TEXT" % (username,password))
      print result.read()
      # msg=unescape(msg)
      form_fields = {
        "content": msg,          
      }
      headers={'Referer':'http://t.sina.com.cn'}
      url="http://t.sina.com.cn/mblog/publish.php"
      form_data = urllib.urlencode(form_fields)
      req = urllib2.Request(url, form_data, headers)
      response = urllib2.urlopen(req)
      print  response.read()
      # print result.content

if __name__ == '__main__':
    send_sina_msgs('jack.hu.cool@gmail.com', 'xxx', 'mix中文rar')
