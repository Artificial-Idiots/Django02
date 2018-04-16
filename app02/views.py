from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.timezone import now


class Student(object):
    name = 'Tom'


def index(request):
    """首页"""
    # 方式一
    my_dict = {'key01': 'value01', 'key02': 'value02'}
    my_list = ['list01', 'list02', 'list03', 'list04']
    my_obj = Student()
    my_date = now()
    my_html = '<font color="red">红色</font>'
    context = {
        'number': 5,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_obj': my_obj,
        'my_date': my_date,
        'my_html': my_html,
    }

    return render(request, 'index.html', context)


def inherit(request):
    """进入模板继承演示界面"""
    return render(request, 'child.html')


def login(request):
    """进入登录界面"""
    return render(request, 'login.html')


def do_login(request):
    """处理登录操作"""

    # 处理登录操作
    username = request.GET.get('username')
    password = request.GET.get('password')

    if username == 'admin' and password == '123':
        # 登录成功,进入发帖界面
        # 通过session保存登陆用户名（用户id）
        request.session['username'] = 'admin'
        return redirect('/post')
    else:
        # 登录失败,回到登录界面
        return redirect('/login')


def post(request):
    """进入发帖界面"""
    # 判断是否有登陆，如果没有，则回到有登陆界面
    if 'username' not in request.session: # 没有登陆
        return redirect('/login')
    return render(request, 'post.html')


def do_post(request):
    """执行发帖操作"""

    title = request.POST.get('title')
    content = request.POST.get('content')

    text = '成功发表了一篇帖子：%s  %s ' % (title, content)
    return HttpResponse(text)


from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


# /verify_code
def create_verify_code(request):
    """使用Pillow包生成验证码图片"""

    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100), 255)  # RGB

    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'

    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def show_verify_code(request):
    """进入显示验证码界面"""
    return render(request, 'show_verify_code.html')


def do_verify(request):
    """校验验证码"""

    # 获取用户填写的验证码
    code = request.POST.get('verify_code')
    # 读取session中保存的验证码
    code2 = request.session.get('verifycode')

    if code.upper() == code2.upper():
        return HttpResponse('校验通过')
    else:
        return HttpResponse('校验不通过')