from django import forms
from django.contrib import admin
from homepage.models import *


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"

    def clean(self):
        age_min = self.cleaned_data.get('playing_age_min')
        age_max = self.cleaned_data.get('playing_age_max')
        if age_min < 0:
            raise forms.ValidationError("Playing age cannot be negative. (?!)")
        elif age_min > age_max:
            raise forms.ValidationError("Maximum playing age must be greater than minimum playing age.")
        return self.cleaned_data


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = "__all__"


class ActorAdmin(admin.ModelAdmin):
    form = ActorForm
    list_display = ('full_name', 'location',)

    def has_add_permission(self, request):
        return allow_up_to(self.model, 1)


class ContactDetailAdmin(admin.ModelAdmin):
    form = ContactDetailForm

    def has_add_permission(self, request):
        return allow_up_to(self.model, 1)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"

    def clean_category(self):
        category = self.cleaned_data['category']
        if category is None:
            category = "Other"
        return category


def allow_up_to(model, num):
    """
    If 'num' instances of 'model' exist, return False. Else return True.
    :param model: django.db.models.Model
    :param num: int
    :return: bool
    """
    num_objects = model.objects.count()
    if num_objects >= num:
        return False
    else:
        return True

admin.site.register(Actor, ActorAdmin)
admin.site.register(TheatreCredit)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(ContactDetail)
