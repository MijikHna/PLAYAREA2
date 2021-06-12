from main.models import App

from typing import  List 

class Helper():
    @staticmethod
    def getAllApps() -> List[App]:
        apps: List[App] = App.objects.all()
        return apps
    