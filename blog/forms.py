from django import forms
from .models import Post, Comentario

class formComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)

class formPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('texto', 'data_publicacao', 'titulo',)
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'class': 'datetimepicker'})
        }