import urllib.request

def download(comin):
    url, index, iden, formatFile = comin
    path = 'DB'
    filename = '{}-{}.{}'.format(index,iden,formatFile)
    p = 'DB'
    if path[-1] != '/':
        p += '/'
    p+=filename
    try:
        urllib.request.urlretrieve(url,p)
        #print("OK: {}".format(url))
    except:
        #print("Fail: {}".format(url))
        pass
        