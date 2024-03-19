from PIL import Image, ImageDraw
#ширина  X
width = 500

#высота  Y
height = 300

im = Image.new('RGB', (width, height), (168, 216, 245))
draw = ImageDraw.Draw(im)

#Дом
draw.rectangle((width * 0.03, height - 170, width * 0.35, height - 30), fill=(150, 75, 0))
draw.rectangle((width * 0.06, height - 170, width * 0.32, height - 30), fill=(164, 158, 119))

#Окно
draw.rectangle((width * 0.07, height - 155, width * 0.18, height - 75),fill=('brown'))
draw.rectangle((width * 0.08, height - 150, width * 0.17, height - 80),fill=(51, 51, 245))

#Крыша
draw.polygon((width * 0.03, height - 170, (width * 0.19, height - 250), (width * 0.35, height - 170)), fill=(204, 27, 0))

#Снеговик
draw.ellipse((width // 2 - 30, height - 130, width // 2 + 30, height - 70), fill=(230, 230, 230))
draw.ellipse((width // 2 - 20, height - 170, width // 2 + 20, height - 130), fill=(230, 230, 230))

#Глаза снеговика
draw.ellipse((width // 2 - 10, height - 163, width // 2 -5, height - 158), fill=('brown'))
draw.ellipse((width // 2 + 8, height - 163, width // 2 + 13, height - 158), fill=('brown'))
draw.ellipse((width // 2 , height - 150, width // 2 + 4, height - 140), fill=(204, 112, 0))

#Руки Снеговика
draw.line((width // 2 + 29 , height - 110, width // 2 + 40, height -130), fill='Brown')
draw.line((width // 2 - 29 , height - 110, width // 2 - 40, height -130), fill='Brown')



draw.ellipse((0, height - 80, width, height + 80), fill='white', outline=('gray'))




im.show()
