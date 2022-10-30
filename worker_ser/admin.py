from django.contrib import admin

from worker_ser.models import Worker, Open_to_guest, Close_current_guest

admin.site.register(Worker)
admin.site.register(Open_to_guest)
admin.site.register(Close_current_guest)
