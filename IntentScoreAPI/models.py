from django.db import models

# Create your models here.

# Creating model for Product Offer
class ProductOffer(models.Model):
    name = models.CharField(max_length=255)
    value_props = models.JSONField(default=list)
    ideal_use_cases = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# Creating Lead model for saving csv data into db and later on populating csv from db data.
class Lead(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    linkedin_bio = models.CharField(max_length=255)
    intent = models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    reasoning = models.TextField(blank=True)
    created_at = models.DateTimeField
    
    def __str__(self):
        return f"{self.name} - {self.company}"
    
    def clean(self):
        if self.intent and self.intent not in ['High','Medium','Low']:
            from django.core.exceptions import ValidationError
            raise ValidationError({'intent':'Intent must be High, Medium, or Low'})