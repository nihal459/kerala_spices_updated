from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False, verbose_name='Is Customer')
    name = models.CharField(max_length=100, default='User')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    landmark = models.CharField(max_length=250, blank=True, null=True)

    verified = models.BooleanField(default=False, verbose_name='Is Verified')
    gender = models.BooleanField(default=False, verbose_name='Gender')

    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    pincode = models.CharField(max_length=10, blank=True, null=True, verbose_name='Pincode')
    mobile_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Mobile Number')

    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images', blank=True, null=True)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    description = models.TextField()
    product_code = models.CharField(max_length=20)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.product_name
    


class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} added by {self.user.username} on {self.date_added}"



class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Checkout by {self.user.username} on {self.checkout_date}"


class OrderedProduct(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='ordered_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} - ${self.price}"



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name