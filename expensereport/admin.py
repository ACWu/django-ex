from django.contrib import admin
from .models import ExpenseReport, ExpenseItem

# Register your models here.
class ExpenseItemInline(admin.TabularInline):
    model = ExpenseItem
    extra = 3
    
class ExpenseReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['generate_date']}),
        ('Ending mileage', {'fields': ['ending_mileage']}),
        ('Comment', {'fields': ['title'], 'classes': ['collapse']}),
    ]
    inlines = [ExpenseItemInline]
    list_display = ('title', 'generate_date', 'was_generated_recently')
    list_filter = ['generate_date']
    search_fields = ['generate_date']
    
admin.site.register(ExpenseReport, ExpenseReportAdmin)
admin.site.register(ExpenseItem)