from django.http import Http404

"""
برای نمایش فیلد های اضافه کردن یک مطالبه 
یک mixin تعریف کرده و شرط میگذاریم گه اگر کاربر عادی بود دو بخش user , status رو برای ا نمایش ندهد
"""


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'slug', 'category', 'description', 'short_description',
                           'image', 'video', 'user', 'status'
                           ]
        elif request.user.is_active:
            self.fields = ['title', 'slug', 'category', 'description', 'short_description',
                           'image', 'video'
                           ]
        else:
            return Http404
        return super().dispatch(request, *args, **kwargs)
