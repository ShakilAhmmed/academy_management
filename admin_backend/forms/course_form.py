from django import forms

from admin_backend.models import Courses, Category , SubCategory


class CourseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(category_status=True),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.none(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))



    class Meta:
        model = Courses
        fields = "__all__"
        LEVEL_CHOICE = (('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert'))
        LANGUAGE_CHOICE = (('English', 'English'), ('Bengali', 'Bengali'))
        widgets = {
            'course_title': forms.TextInput(attrs={'class': 'form-control'}),
            'course_short_description': forms.Textarea(attrs={'class': 'form-control', 'cols': '4', 'rows': '2'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control', 'cols': '4', 'rows': '2'}),
            'level': forms.Select(choices=LEVEL_CHOICE, attrs={'class': 'form-control'}),
            'course_language': forms.Select(choices=LANGUAGE_CHOICE, attrs={'class': 'form-control'}),
            'is_top': forms.CheckboxInput(),
        }
