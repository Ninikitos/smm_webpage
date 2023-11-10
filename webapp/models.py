from django.db import models
from PIL import Image
from django.db.models.signals import pre_delete
from django.dispatch import receiver


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
    about_image_one = models.ImageField(upload_to='about_page_images/', null=True)
    about_slug_one = models.SlugField(default="", blank=True)
    about_image_two = models.ImageField(upload_to='about_page_images/', null=True)
    about_slug_two = models.SlugField(default="", blank=True)

    def __str__(self):
        return self.about_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.coaching_image_one, 315, 368)
        resize_image(self.coaching_image_two, 252, 294)

    class Meta:
        verbose_name_plural = "About page"


class ServicePageModel(models.Model):
    service_image_one = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_one = models.SlugField(default="", blank=True)
    service_title_one = models.CharField(max_length=255)
    service_list_one = models.TextField()

    service_image_two = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_two = models.SlugField(default="", blank=True)
    service_title_two = models.CharField(max_length=255)
    service_list_two = models.TextField()

    service_image_three = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_three = models.SlugField(default="", blank=True)
    service_title_three = models.CharField(max_length=255)
    service_list_three = models.TextField()

    service_image_four = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_four = models.SlugField(default="", blank=True)
    service_title_four = models.CharField(max_length=255)
    service_list_four = models.TextField()

    def __str__(self):
        return "Service page"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.service_image_one, 660, 790)
        resize_image(self.service_image_two, 660, 790)
        resize_image(self.service_image_three, 660, 790)
        resize_image(self.service_image_four, 660, 790)

    class Meta:
        verbose_name_plural = "Service page"


class CoachingPageModel(models.Model):
    coaching_title = models.CharField(max_length=100)
    coaching_description = models.TextField()
    coaching_image_one = models.ImageField(upload_to='coaching_page_images/', null=True)
    coaching_slug_one = models.SlugField(default="", blank=True)
    coaching_image_two = models.ImageField(upload_to='coaching_page_images/', null=True)
    coaching_slug_two = models.SlugField(default="", blank=True)

    def __str__(self):
        return self.coaching_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.coaching_image_one, 315, 368)
        resize_image(self.coaching_image_two, 252, 294)

    class Meta:
        verbose_name_plural = "Coaching page"



def resize_image(image_field, new_width, new_height):
    if image_field:
        img = Image.open(image_field.path)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image_field.path)


@receiver(pre_delete, sender=AboutPageModel)
def delete_images(sender, instance, **kwargs):
    instance.about_image_one.delete(False)
    instance.about_image_two.delete(False)

@receiver(pre_delete, sender=CoachingPageModel)
def delete_images(sender, instance, **kwargs):
    instance.coaching_image_one.delete(False)
    instance.coaching_image_two.delete(False)

@receiver(pre_delete, sender=ServicePageModel)
def delete_images(sender, instance, **kwargs):
    instance.service_image_one.delete(False)
    instance.service_image_two.delete(False)
    instance.service_image_three.delete(False)
    instance.service_image_four.delete(False)