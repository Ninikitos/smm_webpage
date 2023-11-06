import os

from django.contrib import admin
from django.utils.text import slugify

from .models import AboutPageModel, ServicePageModel, CoachingPageModel

def update_slug_from_image(obj, image_fields, slug_fields):
    for i, image_field in enumerate(image_fields):
        image = getattr(obj, image_field)
        slug = getattr(obj, slug_fields[i])

        if image and hasattr(image, 'file') and hasattr(image.file, 'name'):
            image_filename = os.path.basename(image.file.name)
            image_filename = image_filename.replace("cfakepath", "").rsplit('.', 1)[0]

            if not slug or slug != slugify(image_filename):
                setattr(obj, slug_fields[i], slugify(image_filename))

    obj.save()

class AboutPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_fields = ['about_image_one', 'about_image_two']
        slug_fields = ['about_slug_one', 'about_slug_two']

        update_slug_from_image(obj, image_fields, slug_fields)

class ServicePageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_fields = [
            'service_image_one',
            'service_image_two',
            'service_image_three',
            'service_image_four',
        ]

        slug_fields = [
            'service_slug_one',
            'service_slug_two',
            'service_slug_three',
            'service_slug_four',
        ]

        update_slug_from_image(obj, image_fields, slug_fields)

class CoachingPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_filenames = [os.path.basename(obj.coaching_image_one.name), os.path.basename(obj.coaching_image_two.name)]

        for i, image_filename in enumerate(image_filenames):
            image_filenames[i] = image_filename.replace("cfakepath", "").rsplit('.', 1)[0]

            if i == 0 and not obj.coaching_slug_one:
                obj.coaching_slug_one = slugify(image_filenames[i])
            elif i == 1 and not obj.coaching_slug_two:
                obj.coaching_slug_two = slugify(image_filenames[i])

        super().save_model(request, obj, form, change)



admin.site.register(AboutPageModel, AboutPageAdmin)
admin.site.register(ServicePageModel, ServicePageAdmin)
admin.site.register(CoachingPageModel, CoachingPageAdmin)
