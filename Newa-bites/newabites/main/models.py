from django.db import models

# Create your models here.
class Contribution(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    recipename=models.CharField(max_length=50)
    recipe=models.TextField()
    history=models.TextField()


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)  # Recipe name
    description = models.TextField(blank=True, null=True)  # Brief recipe description
    historical_essence = models.TextField(blank=True, null=True)  # Cultural/historical significance
    carbohydrate = models.TextField(blank=True, null=True)  # Nutritional information (JSON-friendly, e.g., calories, protein, etc.)
    protein = models.TextField(blank=True, null=True)  # Nutritional information (JSON-friendly, e.g., calories, protein, etc.)
    fat = models.TextField(blank=True, null=True)  # Nutritional information (JSON-friendly, e.g., calories, protein, etc.)
    calories = models.TextField(blank=True, null=True)  # Nutritional information (JSON-friendly, e.g., calories, protein, etc.)
    tutorial_video_url = models.URLField(blank=True, null=True)  # YouTube or external video URL
    ingredient_list = models.ManyToManyField(Ingredient, related_name="recipes")  # List of ingredients
    image1=models.ImageField(upload_to='img', blank=True, null=True)
    image2=models.ImageField(upload_to='img', blank=True, null=True)
    image3=models.ImageField(upload_to='img', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)  # Physical address in text
    maps_link = models.URLField(blank=True, null=True)  # Google Maps link for the shop
    contact = models.CharField(max_length=20, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="shops")
    promocode=models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
class OnlineShop(models.Model):
    name = models.CharField(max_length=100)  # Name of the online shop/platform
    product_url = models.URLField(blank=True, null=True)  # Direct link to the product
    ingredient = models.ForeignKey(Ingredient, related_name="online_shops", on_delete=models.CASCADE)  # Ingredient associated with the online link

    def __str__(self):
        return f"{self.name} - {self.ingredient.name}"



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)  # Physical address in text
    maps_link = models.URLField(blank=True, null=True)  # Google Maps link for the restaurant
    contact = models.CharField(max_length=20, blank=True, null=True)
    recipes = models.ManyToManyField(Recipe, related_name="restaurants")

    def __str__(self):
        return self.name


