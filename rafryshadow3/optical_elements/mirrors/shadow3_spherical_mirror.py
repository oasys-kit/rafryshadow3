from syned.beamline.shape import Sphere, SphericalCylinder, Convexity, Direction

from rafryshadow3.optical_elements.mirrors.shadow3_mirror import Shadow3Mirror, Shadow3MirrorParameters
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name

class Shadow3SphericalMirrorParameters(Shadow3MirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 FCYL=0,
                 CIL_ANG=0.0,
                 F_CONVEX=0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0,
                 RMIRR=0.0):
        Shadow3MirrorParameters.__init__(self,
                                         F_REFLEC,
                                         F_REFL,
                                         FILE_REFL,
                                         ALFA,
                                         GAMMA,
                                         F_THICK)
        self.FCYL=FCYL
        self.CIL_ANG=CIL_ANG
        self.F_EXT=F_EXT
        self.F_CONVEX=F_CONVEX
        self.F_DEFAULT=F_DEFAULT
        self.SSOUR=SSOUR
        self.SIMAG=SIMAG
        self.THETA=THETA
        self.RMIRR=RMIRR

class Shadow3SpericalMirror(Shadow3Mirror):

    def __init__(self,
                 name="Undefined",
                 boundary_shape=None,
                 mirror_parameters=Shadow3SphericalMirrorParameters()):
        Shadow3Mirror.__init__(self,
                               name=name,
                               boundary_shape=boundary_shape,
                               mirror_parameters=mirror_parameters)

    def _get_surface_shape(self, mirror_parameters):
        if mirror_parameters.FCYL == 0:
            return Sphere(radius=mirror_parameters.RMIRR,
                          convexity=(Convexity.UPWARD if mirror_parameters.F_CONVEX == 0 else Convexity.DOWNWARD))
        else:
            return SphericalCylinder(radius=mirror_parameters.RMIRR,
                                     convexity=(Convexity.UPWARD if mirror_parameters.F_CONVEX == 0 else Convexity.DOWNWARD),
                                     cylinder_direction=Direction.TANGENTIAL if mirror_parameters.CIL_ANG == 0 else Direction.SAGITTAL)

    def _set_shadow3_mirror_shape_parameters(self, shadow3_oe, additional_parameters):
        shadow3_oe.FMIRR = 1

        shadow3_oe.FCYL=additional_parameters.FCYL
        shadow3_oe.CIL_ANG=additional_parameters.CIL_ANG
        shadow3_oe.F_EXT=additional_parameters.F_EXT
        shadow3_oe.F_CONVEX=additional_parameters.F_CONVEX
        shadow3_oe.F_DEFAULT=additional_parameters.F_DEFAULT
        shadow3_oe.SSOUR=additional_parameters.SSOUR
        shadow3_oe.SIMAG=additional_parameters.SIMAG
        shadow3_oe.THETA=additional_parameters.THETA
        shadow3_oe.RMIRR=additional_parameters.RMIRR