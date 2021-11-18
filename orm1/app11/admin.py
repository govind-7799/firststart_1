from django.contrib import admin
from.models import Employeedata

class empyoeeadmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_phno','emp_cmpname','emp_status','emp_address']
    
admin.site.register(Employeedata,empyoeeadmin)
