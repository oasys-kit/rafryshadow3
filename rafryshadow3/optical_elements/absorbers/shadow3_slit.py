
from syned.beamline.optical_elements.absorbers.slit import Slit
from syned.beamline.shape import BoundaryShape

from rafryshadow3.optical_elements.absorbers.shadow3_absorber import Shadow3Absorber
from rafryshadow3.util.shadow3_util import init_file_name

class Shadow3SlitParameters():
    def __init__(self, FILE_SCR_EXT=init_file_name()):
        self.I_ABS  = 0 # HAS ABSORPTION NO (0), YES (1)
        self.I_SLIT = 1 # IS APERTURE/STOP NO (0), YES (1)
        self.I_STOP = 1 # IS APERTURE (1), STOP (0)
        self.FILE_SCR_EXT = FILE_SCR_EXT
        self.THICK = 0.0
        self.FILE_ABS = init_file_name()

class Shadow3Slit(Slit, Shadow3Absorber):
    def __init__(self, name="Undefined", boundary_shape=BoundaryShape(), slit_parameters=Shadow3SlitParameters()):
        Slit.__init__(self, name=name, boundary_shape=boundary_shape)
        Shadow3Absorber.__init__(self, slit_parameters)
