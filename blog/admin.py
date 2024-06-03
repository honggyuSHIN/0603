from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('date',)


admin.site.register(Blog,BlogAdmin)

# 기능을 앱 별로 분리
# 기능이 다르면 app을 분리해주는 게 좋음
#
