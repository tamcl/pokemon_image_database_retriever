import os
import shutil
from PIL import Image
from PIL import ImageFilter

path = 'database'

def crop(img):
  length = img.width
  if img.height < length:
    length = img.height
  left = 0
  top = 0
  right = img.width
  bottom = img.height
  if length == img.width:
    difference = (img.height - length)/2
    top += difference
    bottom -= difference
  else:
    difference = (img.width - length)/2
    left += difference
    right -= difference
  # return img.crop((left,top,right,bottom)).resize((50,50)).convert('L').filter(ImageFilter.FIND_EDGES)
  return img.crop((left,top,right,bottom)).resize((50,50)).convert('L')

def output():
    fpath = 'filtered'
    try:
        shutil.rmtree(fpath)
        print('remove original output folder')
    except:
        print('create new output folder')
    os.mkdir(fpath)
    outputpath = fpath
    print('initiate filter process')
    for x in os.listdir(path):
        count = 1
        for y in os.listdir(path+'/'+x):
            try:
                img = Image.open(path+'/'+x+'/'+y)
                img = crop(img)
                img.save(outputpath+'/'+x+'-'+str(count)+'.jpg','JPEG')
            except:
                print('{} {} error during formatting'.format(x,y))
            count+=1
    print('filter complete')







    