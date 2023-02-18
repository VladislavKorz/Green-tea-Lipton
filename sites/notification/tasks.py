import datetime
from users.models import Profile 

def absence(Profile_Pk):
    profile=Profile.objects.get(pk=Profile_Pk)
    now = datetime.datetime.now()
    last_occurrence = profile.user.last_login()
    absence_time = now - last_occurrence
    return absence_time
