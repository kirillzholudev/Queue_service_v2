from django.contrib import admin

from worker_ser.models import Process




@admin.register(Process)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['time_in_service', 'guest_id']
