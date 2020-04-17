import urllib.request, re, request

urlopenheader={ 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def find(search):
    request_url = 'https://www.bing.com/images/async?q='+search
    request=urllib.request.Request(request_url,None,headers=urlopenheader)
    response=urllib.request.urlopen(request)
    html = response.read().decode('utf8')
    links = re.findall('murl&quot;:&quot;(.*?)&quot;',html)
    return links


