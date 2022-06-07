from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Model for all products within the users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="WishlistItem",
                                      related_name='product_wishlist')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their wishlist.
    """
    product = models.ForeignKey(Product, null=True, blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name