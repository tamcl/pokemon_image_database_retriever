import urllib.request

def download(path, filename, url):
    p = path
    if path[-1] != '/':
        p += '/'
    p+=filename
    try:
        urllib.request.urlretrieve(url,p)
        #print("OK: {}".format(url))
    except:
        # print("Fail: {}".format(url))
        pass