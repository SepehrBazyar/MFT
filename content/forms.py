from django import forms

from content.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "text",
        )

    def clean_text(self):
        text: str = self.cleaned_data["text"]
        if "bad" in text.lower():
            raise forms.ValidationError("Bad Words")

        return text
