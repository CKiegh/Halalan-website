from django.contrib import admin

# Register your models here.
from .models import User, Position, Candidates, Vote

admin.site.register(User)
admin.site.register(Position)
admin.site.register(Candidates)
admin.site.register(Vote)


# USERNAME = admin
# PASSWORD = admin123