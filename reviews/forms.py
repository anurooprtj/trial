from django import forms
from .models import RestaurantReview,ReviewImages
class ReviewForm(forms.ModelForm):
	class Meta:
		model=RestaurantReview
		fields=['reviewText','reviewRating']
		widgets={'reviewText':forms.Textarea(attrs={'rows':4, 'cols':15}),}


class ImageUploadForm(forms.Form):
	ReviewImage=forms.ImageField()
	fields=['ReviewImage']

	

