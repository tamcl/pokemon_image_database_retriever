import os
import urllib.request
import organise
import numpy as np
import shutil
from PIL import Image

gen1 = 151
path = 'standard/'
def createStandardFiles(path=path):
    print('initiate {}'.format(path))
    try:
        os.mkdir(path)
    except:
        pass
        #print('"{}" branch already exist'.format(path))
    p = path
    for i in range(gen1):
        try:
            os.mkdir(p+str(i+1))
        except:
            pass
            #print('{} is already been created'.format(i+1))
        
def extractimg(i):
    try:
        if 'serebii-pokemon-art-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokemon/art/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-art-{}.png'.format(i+1,i+1))
    except:
        pass
    try:
        if 'serebii-pokearth-sprites-dp-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/dp/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-dp-{}.png'.format(i+1,i+1))
    except:
        pass
    try:
        if 'serebii-pokearth-sprites-hgss-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/hgss/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-hgss-{}.png'.format(i+1,i+1))
    except:
        pass
    try:
        if 'serebii-pokemon-blackwhite-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
            urllib.request.urlretrieve('https://www.serebii.net/blackwhite/pokemon/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-blackwhite-{}.png'.format(i+1,i+1))
    except:
        pass

    if 'serebii-pokemon-art-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
        urllib.request.urlretrieve('https://www.serebii.net/pokemon/art/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-art-{}.png'.format(i+1,i+1))
    if 'serebii-pokearth-sprites-dp-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
        urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/dp/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-dp-{}.png'.format(i+1,i+1))
    if 'serebii-pokearth-sprites-hgss-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
        urllib.request.urlretrieve('https://www.serebii.net/pokearth/sprites/hgss/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokearth-sprites-hgss-{}.png'.format(i+1,i+1))
    if 'serebii-pokemon-blackwhite-{}.png'.format(i+1) not in os.listdir(path+'{}/'.format(i+1)):
        urllib.request.urlretrieve('https://www.serebii.net/blackwhite/pokemon/{}.png'.format(str(i+1+1000)[1:]),path+'{}/serebii-pokemon-blackwhite-{}.png'.format(i+1,i+1))


        # print('standard {} complete download'.format(str(i+1+1000)[1:]))

def compare(pokeIndex, patht, threshold):
    try:
        
        minimum = 0
        maximum = 0
        start = True
        test = np.array(organise.crop(Image.open(patht)))
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
        if threshold < maximum:
            os.remove(patht)
            print('remove {}'.format(patht))
        return (minimum, maximum)
    except:
        os.remove(patht)
        return(0,99999999999999999999)

