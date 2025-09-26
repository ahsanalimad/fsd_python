import django.db.models as model
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Products(model.Model):
    # ID field is auto-created by Django as primary key
    name = model.CharField(max_length=250)
    description = model.TextField()
    price = model.DecimalField(max_digits=10, decimal_places=2)
    stock = model.IntegerField()

    def __str__(self):
        return self.name

# Signal to create auth token when a new user is created
@receiver(post_save, sender='website.AuthUser')
def create_auth_user_token(sender, instance, created, **kwargs):
    if created:
        from rest_framework.authtoken.models import Token
        Token.objects.create(user=instance)

class AuthUser(AbstractUser):
    # Inherits all fields from AbstractUser
    email = model.EmailField(unique=True)
    username = model.CharField(max_length=150, unique=True)
    user_permissions = None  # Disable permissions for simplicity
    groups = None  # Disable groups for simplicity
    first_name = None
    last_name = None

    def __str__(self):
        return self.email
    
    