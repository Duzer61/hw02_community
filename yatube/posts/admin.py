from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    # Поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'
    # Позволяет изменять поле group в любом посте прямо из списка постов
    list_editable = ('group',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    emty_value_display = '-пусто-'
    list_editable = ('description',)

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
