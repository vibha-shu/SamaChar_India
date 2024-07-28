from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')

admin.site.register(contact,contactAdmin)

class hnewsAdmin(admin.ModelAdmin):
    list_display = ('id','spick','sheadlines','subject','newsdes','ndate','city')

admin.site.register(hnews,hnewsAdmin)

class bnewsAdmin(admin.ModelAdmin):
    list_display = ('id','bn','city','subject','newsdes','newspic','ndate')

admin.site.register(bnews,bnewsAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpick','cdate')

admin.site.register(category,categoryAdmin)

class newcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','ncategory','fheadlines','sheadlines','theadlines','foheadlines','fiheadlines')

admin.site.register(newcategory,newcategoryAdmin)

class trendingAdmin(admin.ModelAdmin):
    list_display = ('id','ft','city','subject','newsdes','newspic','ndate','ncategory')

admin.site.register(trending,trendingAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','passwd','ppick','address')

admin.site.register(profile,profileAdmin)

class newsAdmin(admin.ModelAdmin):
    list_display = ('id','city','headlines','subject','newsdes','newspic','ndate','ncategory')

admin.site.register(news,newsAdmin)

class tnewsAdmin(admin.ModelAdmin):
    list_display = ('id','tnpick','tnheadlines','subject','newsdes','city','ndate','ncategory')

admin.site.register(tnews,tnewsAdmin)

class tsnewsAdmin(admin.ModelAdmin):
    list_display = ('id','tspick','tsheadlines','subject','newsdes','city','ndate','ncategory')

admin.site.register(tsnews,tsnewsAdmin)

class videosAdmin(admin.ModelAdmin):
    list_display = ('id','vheadlines','vlink','vdate','city','vcategory')

admin.site.register(videos,videosAdmin)

