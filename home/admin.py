from django.contrib import admin
from home.models import feedback, userdata, basicPython, Cprog, websites, code_desc, c_code
# Register your models here.

class codeAdmin(admin.ModelAdmin):
    list_display = ('title','image','code')

class C_admin(admin.ModelAdmin):
    list_display = ('title','image', 'code')


admin.site.register(feedback)
admin.site.register(userdata)
admin.site.register(basicPython)
admin.site.register(Cprog)
admin.site.register(websites)
admin.site.register(code_desc, codeAdmin)
admin.site.register(c_code, C_admin)

# admin.site.register(basic_c)
