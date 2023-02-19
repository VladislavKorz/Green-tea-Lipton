from django import template
from loguru import logger
from roadMaps.models import UserguideAction
register = template.Library()

@register.filter
def check_user_userguide(user, obj):
  uga = UserguideAction.objects.filter(user = user, guideAction = obj).first()
  if uga:
    return uga.date_earned
  else:
    return False