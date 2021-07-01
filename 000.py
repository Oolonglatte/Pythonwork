from PIL import Image, ImageDraw, ImageFont

def add_num(img,count):
    # 给图像增加数字
    Im = ImageDraw.Draw(img)
    drawfont = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', size=100)
    
    width, height = img.size
    # 在给定位置绘制一个字符串
    Im.text((width-100, 0), str(count), font=drawfont, fill="red")
    img.save('result.jpg','jpeg')

    return 0

if __name__ == '__main__':
    # 打开并识别图像
    Img_original=Image.open('Tom.jpg')
    Img_original.show('Tom.jpg')
    add_num(Img_original,30)
    Im_result=Image.open('result.jpg')
    Im_result.show('result.jpg')
