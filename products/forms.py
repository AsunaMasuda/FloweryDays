from django import forms
from .models import Product, ProductReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('rating',)


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('rating_score', 'review_title', 'review_comment')
