from turtle import *
from random import *
from math import *
from PIL import Image
from PIL import ImageEnhance

#绘制樱花树
def tree(n, l):
    pd()#下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25# radians() 将角度转化为弧度  heading()返回目前朝向度数
    pencolor(t, t, t)
    pensize(n/3)
    forward(l)#画树枝

    if n > 0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        right(b)
        tree(n-1, d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1, d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n = cos(radians(heading()-45))/4+0.5# radians() 将角度转化为弧度  heading()返回目前朝向度数
        pencolor(n*1.1, n*0.8, n*0.9)
        circle(3)
        left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            pu()
            #飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画花
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5# radians() 将角度转化为弧度  heading()返回目前朝向度数
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()
            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)#退回

setup(1500, 1000, 0, 0)
bgcolor(0.5,0.5,0.5)
ht()#隐藏turtle
speed(0)#速度 1-10渐进，0 最快
tracer(0,0)
pu()#抬笔
backward(100)
left(90)#左转90度
pu()#抬笔
backward(300)#后退300
tree(12,100)



#绘制地面飘落花瓣
def ground(ground_line_count):
    for i in range(ground_line_count):
        penup()  # 抬起画笔
        x = randint(-550, 450)
        y = randint(-300, -220)
        goto(x,y)  # 让画笔移动到此位置
        pencolor('pink')
        pendown()
        pensize(1)
        circle(2)

ground(120)



#绘制“战疫必胜”字样
def xiezi(ziti,x,y,size=70,left=80,down=80):#传入绘画的画面以及落笔的位置
#ziti参数：输入字体格式;x&y：落笔的坐标，size：字体大小
#left:下一个字体的向右缩进位置；down:下一行字体向下移动的位置
    sx,sy=x,y#绘字的起始位置
    penup()
    goto(sx,sy)
    pendown()
    write('战疫',font=(ziti,size,'normal'))
    penup()
    goto(sx+left,sy-down)
    pendown()
    write('必胜',font=(ziti,size,'normal'))
    penup()

pencolor(1,0.84,0)
xiezi('STXINWEI',300,150)



# 绘制国旗
def Flag():
    color("red")
    fillcolor("red")
    begin_fill()
    penup()
    goto(-630,132)
    pendown()
    for i in range(2):
        forward(185)
        right(90)
        forward(260)
        right(90)
    end_fill()

#绘制五角星
def star1(a):
    color("yellow")        #五角星边框颜色
    fillcolor("yellow")    #五角星填充颜色
    begin_fill()
    for i in range(5):       #绘制五角星的路径
        forward(a)
        right(144)
    end_fill()

#将画笔移到副星开始绘制的位置
def star2(b,c,d):
    up()
    goto(b,c)
    setheading(d)
    down()
    star1(18)
Flag()

#绘制主星
up()
goto(-612,233)
setheading(73)
down()
star1(50)

#绘制副星
star2(-570,305,305)            #第一颗副星
star2(-550,275,30)               #第二颗副星
star2(-550,240,5)             #第三颗副星
star2(-570,220,300)           #第四颗副星



#处理背景图片
def Pic():
    # 读取图像
    im = Image.open('pic.jpg')
    # 色度增强
    enh_col = ImageEnhance.Color(im.convert('RGB'))
    color = 1.5
    image_colored = enh_col.enhance(color)
    # 对比度增强
    enh_con = ImageEnhance.Contrast(image_colored.convert('RGB'))
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image_contrasted.convert('RGB'))
    sharpness = 2.0
    image_sharped = enh_sha.enhance(sharpness)
    # image_sharped.show()
    image_sharped.save("sunshine.jpg")



#插入背景图片
def backgroundsolve(dizhi,wid,hei):
#dizhi：图片的索引地址；wid：turtle画面的宽度；hei:turtle画面的高度
    picformat(dizhi)
    dizhi1=picsize(dizhi,wid,hei)
    bgpic(dizhi1)
def picsize(dizhi,wid,hei):
#处理图片的大小
    im = Image.open(dizhi)
    x,y = wid,hei
    re = im.resize((x,y),Image.ANTIALIAS)
    re.save(dizhi, format='gif')
    return dizhi
def picformat(dizhi):
#修改图片格式
    im = Image.open(dizhi)
    k = im.format
    if k != 'gif':
        im.save(dizhi,format='gif')
Pic()
backgroundsolve("C:/Users/yuki/Desktop/sunshine.jpg",1500,1000)
img = getscreen()
img.getcanvas().postscript(file="bpic.eps")
im=Image.open('bpic.eps')
im.save('bpic.eps','JPEG')
done()
