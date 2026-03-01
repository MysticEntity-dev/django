from pythonCode.admin.models import UserWorld

def getAllAvailWorlds(user):
    UserWorld.objects.filter(userid=user.id)