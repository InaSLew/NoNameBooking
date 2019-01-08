from django.contrib import admin

from .models import Question, Choice

# Below are the initial way to register
# admin.site.register(Question)
# admin.site.register(Choice)

#Register the Question model using a decorator, exactly the same as the `admin.site.register()` syntax
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'display_choices_and_votes')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
