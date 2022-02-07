from PIL import Image
img = Image.open('D:/cat.png')#write image locaion here

filter_img=img.rotate(90)
resize=img.resize((1300,300))

resize.save("shubh.png",'png')
