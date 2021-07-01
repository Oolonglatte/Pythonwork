from PIL import Image, ImageDraw, ImageFont

def add_num(img,count):
    # 给图像增加数字
    Im = ImageDraw.Draw(img)
    drawfont = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', size=40)
    
    width, height = img.size
    # 在给定位置绘制一个字符串
    Im.text((width-40, 0), str(count), font=drawfont, fill="blue")
    img.save('result.jpg','jpeg')

    return 0

if __name__ == '__main__':
    # 打开并识别图像
    Imm=Image.open('Tom.jpg')
    Imm.show('Tom.jpg')
    add_num(Imm,30)
    ImRESULT=Image.open('result.jpg')
    ImRESULT.show('result.jpg')