import os
import urllib.request
import organise
import numpy as np
import shutil
from PIL import Image

gen1 = 151
path = 'standard/'
def createStandardFiles(path=path):
    print('initiate database')
    try:
        os.mkdir(path)
    except:
        print('"{}" branch already exist'.format(path))
    p = path
    for i in range(gen1):
        try:
            os.mkdir(p+str(i+1))
        except:
            print('{} is already been created'.format(i+1))
        
def extractimg():
    for i in range(gen1):
        if 'serebii-pokemon-art-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokemon/art/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-art-{}.png'.format(i+1,i+1))
        if 'serebii-pokearth-sprites-dp-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/dp/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-dp-{}.png'.format(i+1,i+1))
        if 'serebii-pokearth-sprites-hgss-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/hgss/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-hgss-{}.png'.format(i+1,i+1))
        if 'serebii-pokemon-blackwhite-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/blackwhite/pokemon/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-blackwhite-{}.png'.format(i+1,i+1))
        # print('standard {} complete download'.format(str(i+1+1000)[1:]))

def compare(pokeIndex, url):
    if 'test' not in os.listdir():
        os.mkdir('test')
    else:
        shutil.rmtree('test')
        os.mkdir('test')
    param = len(url.split('.'))
    fileformat = url.split('.')[param-1]
    try:
        urllib.request.urlretrieve(url, 'test/test.'+fileformat)
        test = 'test/test.'+fileformat
        minimum = 0
        maximum = 0
        start = True
        test = np.array(organise.crop(Image.open(test)))
        for standardI in os.listdir(path+'{}/'.format(pokeIndex)):
            target = Image.open(path+'{}/'.format(pokeIndex)+standardI)
            target = np.array(organise.crop(target))
            result = 0
            for x in range(50):
                for y in range(50):
                    result += (target[x][y]-test[x][y])**2
            if start == True:
                minimum = result
                maximum = result
                start = False
            else:
                if result < minimum:
                    minimum = result
                if result > maximum:
                    maximum = result
        shutil.rmtree('test')
        return (minimum, maximum)
    except:
        return(0,99999999999999999999)

