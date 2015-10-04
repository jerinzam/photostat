from django.contrib.auth.models import User


import re

def validateEmail(email):

    if len(email) > 6:
	if re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email) != None:
	    return 1
    return 0

class BasicBackend:
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailBackend(BasicBackend):
    def authenticate(self, username=None, password=None):
        #If username is an email address, then try to pull it up
        if  validateEmail(username):
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        else:
            #We have a non-email address username we should try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
