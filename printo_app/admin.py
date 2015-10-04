from django.contrib import admin
from .models import Organization, Shop, Publisher, Tag, Topic, University, College, Course, Branch, DocType, Document, UserProfile, Service
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
	list_display = ('name','organization','private_user','doc_type', 'pages', 'price', 'is_public','display')
	
class ServiceAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class PublisherAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class TopicAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class UniversityAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class CollegeAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}



admin.site.register(Organization)
admin.site.register(Shop)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(University,UniversityAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Branch)
admin.site.register(DocType)
admin.site.register(Document,DocumentAdmin)
admin.site.register(UserProfile)
