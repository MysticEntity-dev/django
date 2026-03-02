from .models  import World

def getAllWorlds():
    return World.objects.all()