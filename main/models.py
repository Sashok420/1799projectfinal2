from django.db import models
from django.contrib.auth.models import User

User.add_to_class('test_score', models.IntegerField(default=None, null=True, blank=True))
User.add_to_class('test_completed', models.BooleanField(default=False))
User.add_to_class('avatar', models.ImageField(upload_to='avatars/', default=None, blank=True))
