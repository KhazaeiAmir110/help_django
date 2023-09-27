from django.http import Http404
from django.shortcuts import get_object_or_404
from demand.models import Demand

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


"""
اضافه کردن پیش فرض user , status برای کاربران عادی
"""


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class UserAccessMixin():
    """
    Restrictions for editing demand
    """

    def dispatch(self, request, pk, *args, **kwargs):
        demand = get_object_or_404(Demand, pk=pk)
        if demand.user == request.user and demand.status == "d" or \
                request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return Http404("Error")
