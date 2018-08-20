import os
import random

from PIL import Image,ImageDraw,ImageFont
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person
from .util import get_random_color
import io

# Create your views here.
PAGE_PEER_NUM = 10

def persons_api(req,current_page):
    # 拿到全部数据
    persons = Person.objects.all()
    # 实例化分页对象
    paginator = Paginator(
        persons,
        PAGE_PEER_NUM
    )
    # 需要知道用户点了第几页的数字按钮，所以需要前端传递的页码参数
    datas = []
    try:
        # 通过参数拿到对应得page对象
        page = paginator.page(current_page)
        # 获得页码里得数据
        datas = page.object_list
    except:
        pass
    data = {
        "persons": datas,#page.object_list
        "page_range": paginator.page_range,
        "page":page,
        "last_page":paginator.num_pages
    }
    return render(req,"paginator.html",data)

def get_confirm_img(req):
    # 有一个颜色
    bg = get_random_color()
    # 设置画布大小
    img_size = (150,50)  # 第一个参数是宽度  第二个是高度
    # 实例化一个画布
    image = Image.new("RGB",img_size,bg)
    # 实例化 一个画笔
    draw = ImageDraw.Draw(image)
    # 实例化一个字体
    font_path = os.path.join(settings.BASE_DIR,"static/fonts/ADOBEARABIC-BOLDITALIC.OTF")
    font_size = 30
    my_font = ImageFont.truetype(font_path, font_size)
    # 验证字母得数据源
    source = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890"
    # 循环次数
    loop = 4
    confirm_code = ""
    for i in range(loop):
        # 生成一个随机数字
        tmp = random.randrange(len(source))
        # 获得随机数字对应下标得字母
        tmp_str = source[tmp]
        # 记录生成的每个字符
        confirm_code += tmp_str
        # 生成随机颜色
        font_color = get_random_color()
        # 将字母画到画布
        draw.text((20+30*i, 10), tmp_str, font_color, font=my_font)
    # draw.text((20,10),"y",font_color,font=my_font)

    # 保存
    buf = io.BytesIO()
    # 将图片保存到路由里
    image.save(buf,"png")

    # 设置session  将生成的四位的验证码保存到session
    req.session["c_code"] = confirm_code
    return HttpResponse(buf.getvalue(),content_type="image/png")

def my_login(req):
    return render(req,"login.html")

def confirm_api(req):
    # 先拿到用户传递过来得参数
    user_code = req.POST.get("code")
    # 从session里拿生成得验证码字符
    bg_code = req.session.get("c_code")
    # 不区分大小写验证  lower
    # 根据不同得比对结果给予不同的反馈
    if user_code.lower() == bg_code.lower():
        data = {
            "code": 1,
            "msg": 'ok',
            "data": []
        }
        return JsonResponse(data)
    else:
        data = {
            "code": 2,
            "msg": "验证码错误",
            "data": []
        }
        return JsonResponse(data)

