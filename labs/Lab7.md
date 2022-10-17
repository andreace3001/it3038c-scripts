Here are the steps I did to create Lab 7:

virtualenv ~/venv/webscraping/Scripts/activate.ps1
pip install pillow
python

from PIL import Image,ImageFilter

myImage = Image.open('C:/Users/Administrator/Pictures/Saved Pictures/bbh.jpg')
myImage.load

myImage.format
myImage.size
myImage.show()


blur = myImage.filter(ImageFilter.BLUR)
blur.show()

from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE)
img2 = myImage.filter(EDGE_ENHANCE)
img2.show()

img3 = myImage.filter(CONTOUR)
img3.show
img3.show()


quit()

```deactivate```
