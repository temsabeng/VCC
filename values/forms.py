from django import forms
from .models import ProjectEvaluation

class ProjectEvaluation(forms.ModelForm):
    project_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = ProjectEvaluation
        fields = ["project_name", "category" , "score"]
