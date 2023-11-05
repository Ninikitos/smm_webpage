import os

from django.contrib import admin
from django.utils.text import slugify

from .models import AboutPageModel, ServicePageModel

class AboutPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_filenames = [os.path.basename(obj.about_image_one.name), os.path.basename(obj.about_image_two.name)]

        for i, image_filename in enumerate(image_filenames):
            image_filenames[i] = image_filename.replace("cfakepath", "").rsplit('.', 1)[0]

            if i == 0 and not obj.about_slug_one:
                obj.about_slug_one = slugify(image_filenames[i])
            elif i == 1 and not obj.about_slug_two:
                obj.about_slug_two = slugify(image_filenames[i])

        super().save_model(request, obj, form, change)


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

        for image_field, slug_field in zip(image_fields, slug_fields):
            image_filename = os.path.basename(getattr(obj, image_field).name)
            image_filename = image_filename.replace("cfakepath", "").rsplit('.', 1)[0]

            if not getattr(obj, slug_field):
                setattr(obj, slug_field, slugify(image_filename))

        super().save_model(request, obj, form, change)


admin.site.register(AboutPageModel, AboutPageAdmin)
admin.site.register(ServicePageModel, ServicePageAdmin)
