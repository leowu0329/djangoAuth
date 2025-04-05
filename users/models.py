from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)  # 允許為空
    # 其他自訂欄位...

    def __str__(self):
        return self.username
