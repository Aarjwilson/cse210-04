from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    def __init__(self):
        super().__init__()
        #self._message = "" #Set default message string

    """def set_message(self,message): #Takes argurment "message" and set it as the message used by self
        self._message = message

    def get_message(self): #Returns the "message" stored in self
        return self._message"""

    def calculate_points(self):
        points = 0

        if (self.get_text() == "*"):
            points = 1
        else:
            points = -1
        
        return points