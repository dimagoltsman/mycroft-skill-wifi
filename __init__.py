from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class WifiHotspotSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('WifiHotspot'))
    def handle_wifi_hotspot(self, message):
        self.speak_dialog('wifi.hotspot')


def create_skill():
    return WifiHotspotSkill()

