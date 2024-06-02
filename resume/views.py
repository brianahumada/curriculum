from django.shortcuts import render
from .models import PersonalInfo, WorkExperience, Education, Skill, Certification, Language, Project, Photo_about

def index_view(request):
    personal_info = {'personal_info':PersonalInfo.objects.first()}
    return render(request, 'resume/index.html',personal_info)



def about_view(request):
    personal_info = PersonalInfo.objects.first()
    photos_about = Photo_about.objects.filter(personal_info=personal_info)
    context = {'personal_info': personal_info, 'photos_about': photos_about}
    return render(request, 'resume/about.html', context)


def resume_view(request):
    personal_info = PersonalInfo.objects.first()
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    languages = Language.objects.all()
    projects = Project.objects.all()
    
    context = {
        'personal_info': personal_info,
        'work_experiences': work_experiences,
        'educations': educations,
        'skills': skills,
        'certifications': certifications,
        'languages': languages,
        'projects': projects,
    }
    
    return render(request, 'resume/resume.html', context)
