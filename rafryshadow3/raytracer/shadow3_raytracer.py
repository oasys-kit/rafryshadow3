
from rafry.raytracer.raytracer import Raytracer

class Shadow3Raytracer(Raytracer):

    HANDLER_NAME = "SHADOW3"

    def __init__(self):
        Raytracer.__init__(self)

    def get_handler_name(self):
        return self.HANDLER_NAME
