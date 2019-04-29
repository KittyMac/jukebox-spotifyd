from mycroft import MycroftSkill, intent_file_handler


class Jukebox(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jukebox.intent')
    def handle_jukebox(self, message):
        self.speak_dialog('jukebox')


def create_skill():
    return Jukebox()

