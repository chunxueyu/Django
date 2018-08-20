import random

# 生成随机颜色
def get_random_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r,g,b)