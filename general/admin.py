from django.contrib import admin

from general.models import Company, Specialization, Worker

admin.site.register(Company)
admin.site.register(Specialization)
#admin.site.register(Worker)



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_shift', 'finish_shift', 'current_time']