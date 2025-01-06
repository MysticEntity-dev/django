from webGui.pythonCode.admin.models import UserWorld

def getAllAvailWorlds(user):
    UserWorld.objects.filter(userId=user.id)