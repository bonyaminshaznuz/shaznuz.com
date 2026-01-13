from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class HeroInfoForm(forms.ModelForm):
    class Meta:
        model = HeroInfo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'availability': forms.Select(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 bg-white cursor-pointer'}),
            'full_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'short_intro': forms.Textarea(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400 resize-y', 'rows': 3}),
            'company_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'hireme_link': forms.URLInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'download_cv_button': forms.URLInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'long_biography': forms.Textarea(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400 resize-y', 'rows': 5}),
        }

class EducationAndTrainingForm(forms.ModelForm):
    class Meta:
        model = EducationAndTraining
        fields = '__all__'
        widgets = {
            'training_type': forms.Select(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none text-gray-700 bg-white cursor-pointer'}),
            'institution_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'cgpa': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400', 'step': '0.01'}),
            'year': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
        }

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
        }

class MySkillForm(forms.ModelForm):
    class Meta:
        model = MySkill
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all duration-200 outline-none text-gray-700 bg-white cursor-pointer'}),
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'icon': forms.FileInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all duration-200 outline-none text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-green-50 file:text-green-700 hover:file:bg-green-100 file:cursor-pointer cursor-pointer'}),
        }

class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'difficulty_level': forms.Select(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 bg-white cursor-pointer'}),
            'project_type': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'logo': forms.FileInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100 file:cursor-pointer cursor-pointer'}),
            'status': forms.Select(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 bg-white cursor-pointer'}),
            'project_link': forms.URLInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'start_date': forms.DateInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all duration-200 outline-none text-gray-700 cursor-pointer', 'type': 'date'}),
        }

class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'small_talk': forms.Textarea(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400 resize-y', 'rows': 3}),
            'hire_me_link': forms.URLInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'copyright_text': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
        }

class SocialIconForm(forms.ModelForm):
    class Meta:
        model = SocialIcon
        fields = '__all__'
        widgets = {
            'icon': forms.FileInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-pink-500 focus:ring-2 focus:ring-pink-200 transition-all duration-200 outline-none text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-pink-50 file:text-pink-700 hover:file:bg-pink-100 file:cursor-pointer cursor-pointer'}),
            'icon_link': forms.URLInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-pink-500 focus:ring-2 focus:ring-pink-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
        }

class MailjetSettingsForm(forms.ModelForm):
    class Meta:
        model = MailjetSettings
        fields = '__all__'
        widgets = {
            'api_key': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400 font-mono text-sm'}),
            'api_secret': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400 font-mono text-sm'}),
            'admin_email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'sender_email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'sender_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
        }

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'favicon']  # Exclude profile_picture
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-teal-500 focus:ring-2 focus:ring-teal-200 transition-all duration-200 outline-none text-gray-700 placeholder-gray-400'}),
            'favicon': forms.FileInput(attrs={'class': 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-teal-500 focus:ring-2 focus:ring-teal-200 transition-all duration-200 outline-none text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100 file:cursor-pointer cursor-pointer'}),
        }

