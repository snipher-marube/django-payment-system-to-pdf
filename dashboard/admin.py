from django.contrib import admin

from .models import Grade, Staff


class GradeAdmin(admin.ModelAdmin):
    list_display = ('position', 'basic_salary')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade_status', 'gross_salary')

    list_display_links = ('first_name',)

admin.site.register(Staff, StaffAdmin)
admin.site.register(Grade, GradeAdmin)
