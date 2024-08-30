from django.contrib import admin
from .models import *


# Register your models here.
'''
Explanation:
@admin.register(Student): This decorator registers the Student model with the admin site and associates 
it with the StudentAdmin class.
list_display: Specifies the fields to display in the admin list view of Student instances.
list_filter: Enables filtering by age and date_of_birth in the admin panel sidebar.
search_fields: Enables searching by first_name and last_name using a search box.
fields: Specifies the order and which fields appear in the add/change form for Student.
fieldsets: Allows you to group fields in sections in the add/change form, providing a more organized layout.
'''
# admin.site.register(Student)
admin.site.register(ModelName)
# admin.site.register(AllFieldType)
