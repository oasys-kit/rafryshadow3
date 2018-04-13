from syned.beamline.shape import Plane

from rafryshadow3.optical_elements.mirrors.shadow3_mirror import Shadow3Mirror, Shadow3MirrorParameters
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name

class Shadow3PlaneMirrorParameters(Shadow3MirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0):
        Shadow3MirrorParameters.__init__(self,
                                         F_REFLEC,
                                         F_REFL,
                                         FILE_REFL,
                                         ALFA,
                                         GAMMA,
                                         F_THICK)

class Shadow3PlaneMirror(Shadow3Mirror):

    def __init__(self,
                 name="Undefined",
                 boundary_shape=None,
                 mirror_parameters=Shadow3PlaneMirrorParameters()):
        Shadow3Mirror.__init__(self,
                               name=name,
                               boundary_shape=boundary_shape,
                               mirror_parameters=mirror_parameters)

    def _get_surface_shape(self, mirror_parameters):
        return Plane()

    def _set_shadow3_mirror_shape_parameters(self, shadow3_oe, additional_parameters):
        shadow3_oe.FMIRR = 5
        shadow3_oe.FCYL  = 0