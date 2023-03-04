from django.contrib import admin

from .models import Category, Course, CourseItem, CourseItemFile, Archive, Order


admin.site.register(Category)
admin.site.register(CourseItem)
admin.site.register(CourseItemFile)
admin.site.register(Archive)
admin.site.register(Order)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "language", "price")
    list_editable = ("price",)
    search_fields = ("title", "language", "category", "user")
    list_filter = ("title", "language", "category")
