from django.contrib import admin

from grades import models
admin.site.register(models.Course)


class ClassAdmin(admin.ModelAdmin):
    list_display = ['course', 'week_day', 'start_time', 'end_time']
admin.site.register(models.Class, ClassAdmin)


class ClassEvaluationAdmin(admin.ModelAdmin):
    list_display = ['related_class', 'grade', 'student']

    def save_model(self, request, obj, form, change):
        obj.student = request.user
        obj.save()

    def queryset(self, request):
        qs = super(ClassEvaluationAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(student=request.user)


admin.site.register(models.ClassEvaluation, ClassEvaluationAdmin)
