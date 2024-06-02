from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    github = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_date = models.DateField()

class Skill(models.Model):
    name = models.CharField(max_length=100)

class Certification(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    date_obtained = models.DateField()

class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100)
    results = models.TextField()
    url = models.URLField(blank=True, null=True)
    foto1 = models.ImageField(upload_to='proyectos/',default='path/to/default/image.jpg')
    foto2 = models.ImageField(upload_to='proyectos/',default='path/to/default/image.jpg')
    


class Photo(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)

class Photo_about(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, related_name='photos_about', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos_about/')
    caption = models.CharField(max_length=200, blank=True)

