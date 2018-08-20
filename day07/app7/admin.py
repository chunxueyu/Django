from django.contrib import admin
from .models import Person,Home

# Register your models here.

class PersonInfo(admin.TabularInline):
    model = Person
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    inlines = [PersonInfo]

# 针对于人的站点管理类
class PersonAdmin(admin.ModelAdmin):
    def get_oldman(self):
        if self.age >= 18:
            return "精英"
        else:
            return "太嫩"

    # 设置显示的字段
    list_display = ['name','age',get_oldman]

    get_oldman.short_description = "精英否"
    # 添加过滤条件
    list_filter = ["name"]
    search_fields = ["name"]
    list_per_page = 10
    ordering = ['age']

    # 信息的分组显示
    fieldsets = [
        ("姓名",{"fields": ("name",)}),
        ("年纪",{"fields": ("age",)})
    ]

# 将需要管理的类注册到
# admin.site.register(Person,PersonAdmin)
# admin.site.register(Home,HomeAdmin)

class MySite(admin.AdminSite):
    site_url = "http://www.baidu.com"
    site_header = "呵呵"
    site_title = "头"

site = MySite()
site.register(Home,HomeAdmin)