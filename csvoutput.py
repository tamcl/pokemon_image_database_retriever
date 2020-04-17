import os
import shutil
import numpy as np
from PIL import Image

def retr(path = 'filtered'):
    output = 'csvFile'
    try:
        shutil.rmtree(output)
        print('remove original output folder')
    except:
        print('create new output folder')
    os.mkdir(output)
    for x in os.listdir(path):
        filename = x.split('.')[0]
        out = np.array(Image.open(path+'/'+x))
        np.savetxt(output+'/'+filename+'.csv',out, delimiter=',')