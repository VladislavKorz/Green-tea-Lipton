import hashlib
from datetime import datetime
from users.models import Profile 
from loguru import logger
import random 
import string


def absence(Profile_Pk):
    profile=Profile.objects.get(pk=Profile_Pk)
    now = datetime.now().date()
    print(profile)
    last_occurrence = profile.user.last_login.date()
    logger.debug(last_occurrence)
    absence_time = now - last_occurrence
    return absence_time


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))



