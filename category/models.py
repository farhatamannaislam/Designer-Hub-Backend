from django.db import models

class Categories(models.TextChoices):
    FORMAL = 'formal', 'Formal'
    CASUAL = 'casual', 'Casual'
    PARTY = 'party', 'Party'

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        choices=Categories.choices,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.get_name_display()
