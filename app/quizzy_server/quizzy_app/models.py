from django.db import models
from django.utils.encoding import python_2_unicode_compatible


'''
relate session cookie to userID in database


def function:
    get user from databse
    
def function:
    put user in database
'''


class Cookie(models.Model):
    cookie_text = models.CharField(max_length=400)
    cookies = models.CharField(max_length=20)
    def __str__(self):
        return self.cookie_test
    
    
class UserIDs(models.Model):
    user_cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    userIDs_text = models.CharField(max_length=400)
    users = models.EmailField(max_length=50)
    def __str__(self):
        return self.userIDs_text