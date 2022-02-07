from PIL import Image,ImageFilter
img = Image.open('D:/cat.png')#write image locaion here
filter_img=img.filter(ImageFilter.BLUR)
filter_img.save("blur",'png')