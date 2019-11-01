from django.shortcuts import render
from portfolio import project_details

# Create your views here.

def index(request):
    context = {
        "name" : project_details.DATA["NAME"],
        "about_me": project_details.DATA["ABOUT_ME"],
        "resume_headline" : project_details.DATA["RESUME_HEADLINE"],
        "image_src" : project_details.DATA["IMAGE_SRC"],
        "profile_name_links" : project_details.DATA["PROFILE_NAME_LINKS"],
        "key_skills" : project_details.DATA["KEY_SKILLS"]
    }
    return render(request, 'main/index.html', context)
def projects(request):
    context = {
        "projects" : project_details.DATA["PROJECTS"]
    }
    return render(request,'main/projects.html', context)
def languages(request):
    context = {
        "languages" : project_details.DATA["LANGUAGES"]
    }
    return render(request, 'main/languages.html', context)
def resume(request):
    context = {}
    return render(request,'main/resume.html', context)

