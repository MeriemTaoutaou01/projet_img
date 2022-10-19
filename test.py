import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('C:\\Users\\hp\\exo1_meca.png')
plt.imshow(image)
plt.show()
from PIL import ImageDraw
from PIL import ImageFont
I1 = ImageDraw.Draw(image)
font = ImageFont.truetype('calibri',25)
I1.text((331, 142), "L1=104,7", fill=(255, 255, 255, 255) ,font=font)
I1.text((375, 54), "a=10°", fill=(255, 255, 255, 255) ,font=font)
I1.text((211, 129), "V1=5m/s", fill=(0,255, 255) ,font=font)
I1.text((174, 129), "D1=20mm", fill=(255, 255, 255, 255) ,font=font)
I1.text((465, 101), "D2", fill=(255, 255, 255, 255) ,font=font)

