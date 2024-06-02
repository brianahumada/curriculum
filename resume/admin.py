from django.contrib import admin
from .models import PersonalInfo, WorkExperience, Education, Skill, Certification, Language, Project, Photo, Photo_about

admin.site.register(PersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Photo)
admin.site.register(Photo_about)
