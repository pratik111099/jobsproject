from django.contrib import admin
from testApp.models import HydJobs,PuneJobs,BalJobs,MumJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BalJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class MumJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber'] 



admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(BalJobs,BalJobsAdmin)
admin.site.register(MumJobs,MumJobsAdmin)