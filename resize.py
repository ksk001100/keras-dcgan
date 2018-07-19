import os
import glob
from PIL import Image

files = glob.glob('outputs/*.jpg')
a = 0
for f in files:
    a = a+1
    img = Image.open(f)
    img_resize = img.resize((64, 64))
    ftitle, fext = os.path.splitext(f)
    img_resize.save('train_images/' + str(a) + '_(64)' + fext)
