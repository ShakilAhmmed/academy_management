from django import forms

from admin_backend.models import SubCategory, Category


class SubCategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(category_status=True),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = SubCategory
        fields = "__all__"
        CHOICES = (('1', 'Active'), ('0', 'Inactive'))
        widgets = {
            'sub_category_code': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_category_title': forms.TextInput(attrs={'class': 'form-control', '@keyup': 'ConvertSlug($event)'}),
            'sub_category_slug': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sub_category_status': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),
        }
