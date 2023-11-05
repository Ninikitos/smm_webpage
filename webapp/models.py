from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

# class ProjectsModel(models.Model):
#     title = models.CharField(max_length=255)
#     cover_image = models.ImageField(upload_to='home_page_images/')
#     description = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'Case for {self.home_page.section_three_title}'
#
#
# class HomePageModel(models.Model):
#     # Section One
#     section_one_page_name = models.CharField(max_length=255)
#     section_one_title = models.CharField(max_length=255)
#     section_one_text = models.TextField()
#     section_one_img_1 = models.ImageField(upload_to='home_page_images/')
#     section_one_img_1_alt = models.CharField(max_length=255)
#     section_one_img_2 = models.ImageField(upload_to='home_page_images/')
#     section_one_img_2_alt = models.CharField(max_length=255)
#     section_one_cta = models.CharField(max_length=255)
#
#     # Section Two
#     section_two_title = models.CharField(max_length=255)
#     section_two_text = models.TextField()
#     section_two_img = models.ImageField(upload_to='home_page_images/')
#     section_two_img_alt = models.CharField(max_length=255)
#     section_two_cta = models.CharField(max_length=255)
#
#     # Section Three
#     section_three_title = models.CharField(max_length=255)
#     section_three_projects = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
#
#     # Section Four
#     section_four_title = models.CharField(max_length=255)
#     section_four_cta = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.section_one_page_name
#

class AboutPageModel(models.Model):

    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    about_image_one = models.ImageField(upload_to='about_page_images/')
    about_slug_one = models.SlugField(default="")
    about_image_two = models.ImageField(upload_to='about_page_images/')
    about_slug_two = models.SlugField(default="")

    def __str__(self):
        return self.about_title

    def safe_about_text(self):
        return mark_safe(self.about_description)

    class Meta:
        verbose_name_plural = "About page"