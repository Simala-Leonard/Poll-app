from django.contrib import admin

from .models import Choice, Question

#admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
