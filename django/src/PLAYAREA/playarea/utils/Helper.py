from main.models import App

from typing import List


class Helper():
    @staticmethod
    def getAllApps(serialized=False) -> List[App]:
        apps: List[App] = App.objects.all()

        if serialized:
            apps = list(map(lambda x: x.serialize(), apps))

        return apps

    @staticmethod
    def setLanguageCookie(response):
        pass
