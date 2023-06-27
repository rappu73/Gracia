from django.contrib import admin
from .models import Complex
from .models import Task
from .models import Massage
from .models import Apparat

admin.site.register(Task)
admin.site.register(Complex)
admin.site.register(Massage)
admin.site.register(Apparat)

# Register your models here.
