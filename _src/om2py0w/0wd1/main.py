# -*- coding: utf-8 -*-
# using PIL https://pypi.python.org/pypi/Pillow/2.2.1
# fork this https://github.com/JiYouMCC/python-show-me-the-code/blob/e0c7c1c37ccba38671078e0b0ff6238992a11499/0000/0000.py
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def write_number(image_file_name_in_current_dir, number = 1):
	img = Image.open(image_file_name_in_current_dir) # open image 
	font_size = img.size[0] if img.size[0] < img.size[1] else img.size[1] # img.size(width, height)
	font_size = font_size / 4	# 字体 数字 尺寸 取小 
	number_txt = str(number) + ' ' if number < 100 else '99+' # 数字文本
	
	font = ImageFont.truetype("arial.ttf", size = font_size) # creat a font object
	if font.getsize(number_txt)[0] > img.size[0] or font.getsize(number_txt)[1] > img.size[1]:
		return img 	# font.getsize(text) -> (width, height) 字比图片大了 不行
	position = img.size[0] - font.getsize(number_txt)[0]	# 字体位置
	ImageDraw.Draw(img).text((position, 0), number_txt, (255, 0, 0), font) 
						# draw.text(position, string, options) 
	return img

# need an image 'nar.png'
write_number('nar.png').save('nar_result.png') # 调用 并 保存 与 当前文件夹
# if number > 100, shows '99+'
write_number('nar.png', 100).save('nar_result100.png')