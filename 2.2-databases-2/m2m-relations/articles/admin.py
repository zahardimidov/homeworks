from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Tag



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count=0
        for form in self.forms:
            if not form.cleaned_data or form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data['is_main']:
                is_main_count+=1
        if is_main_count>1:
            print(is_main_count)
            raise ValidationError('Слишком много главных тегов')
        if is_main_count==0:
            print(is_main_count)
            raise ValidationError('Укажите главный тег')
        
        return super().clean()  # вызываем базовый код переопределяемого метода




class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra=0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id', 'title']
    inlines=[ScopeInline]
