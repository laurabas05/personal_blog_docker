from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write what are you thinking...', "class": "w-3/5 dark:bg-[#575757] mb-[10px] p-2 rounded-[4px] bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none resize-none overflow-y-auto"}),
        }