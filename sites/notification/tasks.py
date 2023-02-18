from datetime import datetime
from users.models import Profile 
from loguru import logger

def absence(Profile_Pk):
    profile=Profile.objects.get(pk=Profile_Pk)
    now = datetime.now().date()
    print(profile)
    last_occurrence = profile.user.last_login.date()
    logger.debug(profile.user.last_login)
    absence_time = now - last_occurrence
    return absence_time
