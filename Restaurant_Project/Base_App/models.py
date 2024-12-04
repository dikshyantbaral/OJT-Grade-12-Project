from django.db import models

class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='items', on_delete=models.CASCADE)  # Correct ForeignKey reference
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Item_name

class AboutUS(models.Model):
    description = models.TextField(blank=False)

class Feedback(models.Model):
    user_name = models.CharField(max_length=15)
    feedback = models.TextField(blank=False)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank= True)

    def __str__(self):
        return self.user_name

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_Person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
