from django import forms
from .models import Post
from django.utils.safestring import mark_safe

# form for creating new Post object
class new_post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]
        labels = {
            "content": "",
        }

        widgets = {
            "content": forms.TextInput(attrs={"placeholder": "Bir şeyler yaz"}),
        }

        helper = """
        <p class="mb-0 mt-1" style="color: #b7b7b7">( Maksimum 300 karakter )</p>
        <ul class="mt-1" style="color: #b7b7b7">
            <li>Paylaşımınızı sonradan silemeyeceksiniz.</li>
            <li>Kişisel bilgilerinizi paylaşmayınız.</li>
            <li>Küfür veya hakaret etmeyiniz.</li>
            <li>Düşünceli olunuz &#128519;</li>
        </ul>
        """
        help_texts = {
            "content": mark_safe(helper),
        }
