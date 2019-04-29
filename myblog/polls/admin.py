from django.contrib import admin
from .models import Question, Choice

"""TabularInline关联对象以一种表格式的方式展示，显得更加紧凑"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


"""自定义后台表单;fieldsets定义字段集的标题,可以将多个并为一个字段集"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]  #添加关联对象
    list_display = ('question_text', 'pub_date', 'was_published_recently') #更改列表页中以列的形式展示这个对象
    list_filter = ['pub_date']  #以 pub_date 字段来过滤列表
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
