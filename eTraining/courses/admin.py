from django.contrib import admin # type: ignore
from .models import Course,Lesson ,Ressource,Module,Stripe


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Ressource)
admin.site.register(Stripe)