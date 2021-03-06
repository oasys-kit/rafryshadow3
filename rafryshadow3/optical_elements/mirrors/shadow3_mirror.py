

from rafryshadow3.optical_elements.shadow3_optical_element_decorator import Shadow3OpticalElementDecorator
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name

from syned.beamline.shape import SurfaceShape, BoundaryShape, Plane, Cylinder, Sphere, SphericalCylinder, \
    Ellipsoid, EllipticalCylinder, ParabolicCylinder, Paraboloid, HyperbolicCylinder, Hyperboloid, Toroidal, Conic
from syned.beamline.shape import Ellipse, Rectangle, Direction
from syned.beamline.optical_elements.mirrors.mirror import Mirror
from syned.beamline.element_coordinates import ElementCoordinates

from Shadow import OE

class Shadow3MirrorParameters():
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0):

        self.F_REFLEC=F_REFLEC
        self.F_REFL=F_REFL
        self.FILE_REFL=FILE_REFL
        self.ALFA=ALFA
        self.GAMMA=GAMMA
        self.F_THICK=F_THICK

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

class Shadow3CurvedMirrorParameters(Shadow3MirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0):
        Shadow3MirrorParameters.__init__(self,
                                         F_REFLEC,
                                         F_REFL,
                                         FILE_REFL,
                                         ALFA,
                                         GAMMA,
                                         F_THICK)
        self.F_EXT=F_EXT
        self.F_DEFAULT=F_DEFAULT
        self.SSOUR=SSOUR
        self.SIMAG=SIMAG
        self.THETA=THETA

class Shadow3SphericalMirrorParameters(Shadow3CurvedMirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0,
                 RMIRR=0.0):
        Shadow3CurvedMirrorParameters.__init__(self,
                                               F_REFLEC,
                                               F_REFL,
                                               FILE_REFL,
                                               ALFA,
                                               GAMMA,
                                               F_THICK,
                                               F_EXT,
                                               F_DEFAULT,
                                               SSOUR,
                                               SIMAG,
                                               THETA)
        self.RMIRR=RMIRR

class Shadow3EllipticalMirrorParameters(Shadow3CurvedMirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0,
                 AXMAJ=0.0,
                 AXMIN=0.0):
        Shadow3CurvedMirrorParameters.__init__(self,
                                               F_REFLEC,
                                               F_REFL,
                                               FILE_REFL,
                                               ALFA,
                                               GAMMA,
                                               F_THICK,
                                               F_EXT,
                                               F_DEFAULT,
                                               SSOUR,
                                               SIMAG,
                                               THETA)
        self.AXMAJ=AXMAJ
        self.AXMIN=AXMIN

class Shadow3ParabolicMirrorParameters(Shadow3CurvedMirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0,
                 F_SIDE=0.0,
                 PARAM =0.0):
        Shadow3CurvedMirrorParameters.__init__(self,
                                               F_REFLEC,
                                               F_REFL,
                                               FILE_REFL,
                                               ALFA,
                                               GAMMA,
                                               F_THICK,
                                               F_EXT,
                                               F_DEFAULT,
                                               SSOUR,
                                               SIMAG,
                                               THETA)
        self.F_SIDE=F_SIDE
        self.PARAM =PARAM

class Shadow3ToroidalMirrorParameters(Shadow3CurvedMirrorParameters):
    def __init__(self,
                 F_REFLEC=0,
                 F_REFL=0,
                 FILE_REFL=init_file_name(),
                 ALFA=0.0,
                 GAMMA=0.0,
                 F_THICK=0.0,
                 F_EXT=1,
                 F_DEFAULT=0,
                 SSOUR=0.0,
                 SIMAG=0.0,
                 THETA=0.0,
                 R_MAJ=0.0,
                 R_MIN=0.0):
        Shadow3CurvedMirrorParameters.__init__(self,
                                               F_REFLEC,
                                               F_REFL,
                                               FILE_REFL,
                                               ALFA,
                                               GAMMA,
                                               F_THICK,
                                               F_EXT,
                                               F_DEFAULT,
                                               SSOUR,
                                               SIMAG,
                                               THETA)
        self.R_MAJ=R_MAJ
        self.R_MIN=R_MIN

class Shadow3Mirror(Mirror, Shadow3OpticalElementDecorator):
    def __init__(self,
                 name="Undefined",
                 surface_shape = SurfaceShape(),
                 boundary_shape= BoundaryShape(),
                 mirror_parameters=None):
        Mirror.__init__(self,
                        name=name,
                        surface_shape=surface_shape,
                        boundary_shape=boundary_shape)
        Shadow3OpticalElementDecorator.__init__(self, mirror_parameters)

    def _build_shadow3_oe(self, additional_parameters):
        shadow3_oe=OE()
        shadow3_oe.DUMMY=100
        
        shadow3_oe.F_CRYSTAL=0
        shadow3_oe.F_REFRAC=0
        shadow3_oe.F_SCREEN=0
        shadow3_oe.N_SCREEN=0

        # SURFACE SHAPE

        self._set_shadow3_mirror_shape_parameters(shadow3_oe, additional_parameters)
        
        # REFLECTIVITY
        
        self._set_shadow3_reflectivity(shadow3_oe, additional_parameters)
        
        # DIMENSIONS

        self._set_shadow3_dimensions(shadow3_oe)

        # TEMPORARY NO ERRORS:

        shadow3_oe.F_RIPPLE = 0
        shadow3_oe.F_FACET  = 0
        shadow3_oe.F_ROUGHNESS = 0
        shadow3_oe.F_KOMA = 0
        shadow3_oe.F_SEGMENT = 0

        '''
        if self.modified_surface == 1:
             if self.ms_type_of_defect == 0:
                 shadow_oe._oe.F_RIPPLE = 1
                 shadow_oe._oe.F_G_S = 0
                 shadow_oe._oe.X_RIP_AMP = self.ms_ripple_ampli_x
                 shadow_oe._oe.X_RIP_WAV = self.ms_ripple_wavel_x
                 shadow_oe._oe.X_PHASE   = self.ms_ripple_phase_x
                 shadow_oe._oe.Y_RIP_AMP = self.ms_ripple_ampli_y
                 shadow_oe._oe.Y_RIP_WAV = self.ms_ripple_wavel_y
                 shadow_oe._oe.Y_PHASE   = self.ms_ripple_phase_y
                 shadow_oe._oe.FILE_RIP  = b''
             else:
                 shadow_oe._oe.F_RIPPLE = 1
                 shadow_oe._oe.F_G_S = self.ms_type_of_defect
                 shadow_oe._oe.X_RIP_AMP = 0.0
                 shadow_oe._oe.X_RIP_WAV = 0.0
                 shadow_oe._oe.X_PHASE   = 0.0
                 shadow_oe._oe.Y_RIP_AMP = 0.0
                 shadow_oe._oe.Y_RIP_WAV = 0.0
                 shadow_oe._oe.Y_PHASE   = 0.0
                 shadow_oe._oe.FILE_RIP  = bytes(congruence.checkFileName(self.ms_defect_file_name), 'utf-8')

        elif self.modified_surface == 2:
            shadow_oe._oe.F_FACET = 1
            shadow_oe._oe.FILE_FAC=bytes(congruence.checkFileName(self.ms_file_facet_descr), 'utf-8')
            shadow_oe._oe.F_FAC_LATT=self.ms_lattice_type
            shadow_oe._oe.F_FAC_ORIENT=self.ms_orientation
            shadow_oe._oe.F_POLSEL=self.ms_lattice_type+1
            shadow_oe._oe.RFAC_LENX=self.ms_facet_width_x
            shadow_oe._oe.RFAC_PHAX=self.ms_facet_phase_x
            shadow_oe._oe.RFAC_DELX1=self.ms_dead_width_x_minus
            shadow_oe._oe.RFAC_DELX2=self.ms_dead_width_x_plus
            shadow_oe._oe.RFAC_LENY=self.ms_facet_width_y
            shadow_oe._oe.RFAC_PHAY=self.ms_facet_phase_y
            shadow_oe._oe.RFAC_DELY1=self.ms_dead_width_y_minus
            shadow_oe._oe.RFAC_DELY2=self.ms_dead_width_y_plus
        elif self.modified_surface == 3:
            shadow_oe._oe.F_ROUGHNESS = 1
            shadow_oe._oe.FILE_ROUGH=bytes(congruence.checkFileName(self.ms_file_surf_roughness), 'utf-8')
            shadow_oe._oe.ROUGH_X=self.ms_roughness_rms_x
            shadow_oe._oe.ROUGH_Y=self.ms_roughness_rms_y
        elif self.modified_surface == 4:
            shadow_oe._oe.F_KOMA = 1
            shadow_oe._oe.F_KOMA_CA=self.ms_specify_rz2
            shadow_oe._oe.FILE_KOMA=bytes(congruence.checkFileName(self.ms_file_with_parameters_rz), 'utf-8')
            shadow_oe._oe.FILE_KOMA_CA=bytes(congruence.checkFileName(self.ms_file_with_parameters_rz2), 'utf-8')
            shadow_oe._oe.F_KOMA_BOUNCE=self.ms_save_intercept_bounces
        elif self.modified_surface == 5:
            shadow_oe._oe.F_SEGMENT = 1
            shadow_oe._oe.ISEG_XNUM=self.ms_number_of_segments_x
            shadow_oe._oe.ISEG_YNUM=self.ms_number_of_segments_y
            shadow_oe._oe.SEG_LENX=self.ms_length_of_segments_x
            shadow_oe._oe.SEG_LENY=self.ms_length_of_segments_y
            shadow_oe._oe.FILE_SEGMENT=bytes(congruence.checkFileName(self.ms_file_orientations), 'utf-8')
            shadow_oe._oe.FILE_SEGP=bytes(congruence.checkFileName(self.ms_file_polynomial), 'utf-8')
        '''

        shadow3_oe.FWRITE = 0
        shadow3_oe.F_ANGLE = 0

        return shadow3_oe

    def _set_shadow3_mirror_shape_parameters(self, shadow3_oe, additional_parameters):
        if isinstance(self._surface_shape, Plane):
            shadow3_oe.FMIRR = 5
            shadow3_oe.FCYL  = 0
        else:


            if isinstance(self._surface_shape, Ellipsoid) or isinstance(self._surface_shape, EllipticalCylinder):
                shadow3_oe.FMIRR = 2
            elif isinstance(self._surface_shape, Sphere) or isinstance(self._surface_shape, SphericalCylinder):
                shadow3_oe.FMIRR = 1
            elif isinstance(self._surface_shape, Paraboloid) or isinstance(self._surface_shape,ParabolicCylinder ):
                shadow3_oe.FMIRR = 4
            elif isinstance(self._surface_shape, Hyperboloid) or isinstance(self._surface_shape, HyperbolicCylinder):
                shadow3_oe.FMIRR = 7
            elif isinstance(self._surface_shape, Toroidal):
                shadow3_oe.FMIRR = 3
            elif isinstance(self._surface_shape, Conic):
                shadow3_oe.FMIRR = 10



            shadow3_oe.F_CONVEX = self._surface_shape._convexity

            if isinstance(self._surface_shape, Cylinder):
                shadow3_oe.FCYL = 1
                shadow3_oe.CIL_ANG = 90*self._surface_shape._cylinder_direction
            else:
                shadow3_oe.FCYL  = 0

            shadow3_oe.F_EXT=additional_parameters.F_EXT
            if (not isinstance(self._surface_shape, Conic)) and shadow3_oe.F_EXT == 0: # AUTOMATIC CALCULATION
                shadow3_oe.F_DEFAULT=additional_parameters.F_DEFAULT

                if shadow3_oe.F_DEFAULT == 0:
                    shadow3_oe.SSOUR=additional_parameters.SSOUR
                    shadow3_oe.SIMAG=additional_parameters.SIMAG
                    shadow3_oe.THETA=additional_parameters.THETA

                if isinstance(self._surface_shape, Paraboloid): shadow3_oe.F_SIDE=additional_parameters.F_SIDE
            else:
                if isinstance(self._surface_shape, Ellipsoid) or isinstance(self._surface_shape, Hyperboloid) \
                         or isinstance(self._surface_shape, EllipticalCylinder)  or isinstance(self._surface_shape, HyperbolicCylinder):
                    shadow3_oe.AXMAJ  = round(self._surface_shape._maj_axis/2, 4)
                    shadow3_oe.AXMIN  = round(self._surface_shape._min_axis/2, 4)
                    shadow3_oe.ELL_THE= 0.0 # defined later!
                elif isinstance(self._surface_shape, Sphere) or isinstance(self._surface_shape, SphericalCylinder):
                    shadow3_oe.RMIRR = round(self._surface_shape.get_radius(), 4)
                elif isinstance(self._surface_shape, Paraboloid) or isinstance(self._surface_shape, ParabolicCylinder):
                    shadow3_oe.PARAM = round(self._surface_shape._parabola_parameter, 4)
                elif isinstance(self._surface_shape, Toroidal):
                    shadow3_oe.R_MAJ = round(self._surface_shape._maj_radius, 4)
                    shadow3_oe.R_MIN = round(self._surface_shape._min_radius, 4)
                elif isinstance(self._surface_shape, Conic):
                    conic_coefficients = [self._surface_shape._conic_coefficients[0],
                                          self._surface_shape._conic_coefficients[1],
                                          self._surface_shape._conic_coefficients[2],
                                          self._surface_shape._conic_coefficients[3],
                                          self._surface_shape._conic_coefficients[4],
                                          self._surface_shape._conic_coefficients[5],
                                          self._surface_shape._conic_coefficients[6],
                                          self._surface_shape._conic_coefficients[7],
                                          self._surface_shape._conic_coefficients[8],
                                          self._surface_shape._conic_coefficients[9]]

                    shadow3_oe.CCC[:] = conic_coefficients[:]

    def _set_shadow3_reflectivity(self, shadow3_oe, additional_parameters):
        shadow3_oe.F_REFLEC = additional_parameters.F_REFLEC
        shadow3_oe.F_REFL   = additional_parameters.F_REFL
        
        if shadow3_oe.F_REFLEC == 1:
            if shadow3_oe.F_REFL == 0:
                shadow3_oe.FILE_REFL = check_file_name(additional_parameters.FILE_REFL) 
                shadow3_oe.ALFA = 0.0
                shadow3_oe.GAMMA = 0.0
                shadow3_oe.F_THICK = 0
            elif shadow3_oe.F_REFL == 1:
                shadow3_oe.FILE_REFL = 'GAAS.SHA'
                shadow3_oe.ALFA  = additional_parameters.ALFA
                shadow3_oe.GAMMA = additional_parameters.GAMMA
                shadow3_oe.F_THICK = 0
            elif shadow3_oe.F_REFL == 2:
                shadow3_oe.FILE_REFL = check_file_name(additional_parameters.FILE_REFL) 
                shadow3_oe.ALFA = 0.0
                shadow3_oe.GAMMA = 0.0
                shadow3_oe.F_THICK = additional_parameters.F_THICK
        elif shadow3_oe.F_REFLEC == 2:
            if shadow3_oe.F_REFL == 0:
                shadow3_oe.FILE_REFL = check_file_name(additional_parameters.FILE_REFL) 
                shadow3_oe.ALFA = 0.0
                shadow3_oe.GAMMA = 0.0
                shadow3_oe.F_THICK = 0
            elif shadow3_oe.F_REFL == 1:
                shadow3_oe.FILE_REFL = 'GAAS.SHA'
                shadow3_oe.ALFA  = additional_parameters.ALFA
                shadow3_oe.GAMMA = additional_parameters.GAMMA
                shadow3_oe.F_THICK = 0
            elif shadow3_oe.F_REFL == 2:
                shadow3_oe.FILE_REFL = check_file_name(additional_parameters.FILE_REFL) 
                shadow3_oe.ALFA = 0.0
                shadow3_oe.GAMMA = 0.0
                shadow3_oe.F_THICK = additional_parameters.F_THICK
        
    def _set_shadow3_dimensions(self, shadow3_oe):
        if self._boundary_shape is None:
            shadow3_oe.FHIT_C = 0
        else:
            shadow3_oe.FHIT_C = 1

            if isinstance(self._boundary_shape, Ellipse):
                shadow3_oe.FSHAPE = 2
            elif isinstance(self._boundary_shape, Rectangle):
                shadow3_oe.FSHAPE = 1

            x_min, x_max, z_min, z_max = self._boundary_shape.get_boundaries()

            shadow3_oe.RLEN1  = z_max
            shadow3_oe.RLEN2  = -z_min
            shadow3_oe.RWIDX1 = x_max
            shadow3_oe.RWIDX2 = -x_min


    def _set_coordinates(self, element_coordinates=ElementCoordinates()):
        super()._set_coordinates(element_coordinates)
        
        self._shadow3_oe.T_REFLECTION = element_coordinates.angle_radial()

        if isinstance(self._surface_shape, Ellipsoid):
            self._set_angle_of_majax_and_pole(element_coordinates)

        #IMPLEMENTATION OF THE AUTOMATIC CALCULATION OF THE SAGITTAL FOCUSING FOR SPHERICAL CYLINDERS
        elif isinstance(self._surface_shape, SphericalCylinder) and \
                        self._shadow3_oe.F_EXT==0 and \
                        self._surface_shape._cylinder_direction==Direction.SAGITTAL:
            self._set_spherical_cylinder_sagittal_radius()

    def _set_spherical_cylinder_sagittal_radius(self):
        self._shadow3_oe.F_EXT=1

        # RADIUS = (2 F1 F2 sin (theta)) /( F1+F2)
        if self._shadow3_oe.F_DEFAULT == 0:
          incidence_angle, reflection_angle = self._grazing_angles_in_rad()

          spherical_radius = ((2*self._shadow3_oe.T_SOURCE*self._shadow3_oe.T_IMAGE)/(self._shadow3_oe.T_SOURCE+self._shadow3_oe.T_IMAGE))*numpy.sin(reflection_angle)
        else:
          spherical_radius = ((2*self._shadow3_oe.SSOUR*self._shadow3_oe.SIMAG)/(self._shadow3_oe.SSOUR+self._shadow3_oe.SIMAG))*numpy.sin(numpy.radians(90-self._shadow3_oe.THETA))

        self._shadow3_oe.RMIRR = spherical_radius

    def _grazing_angles_in_rad(self):
        return round((numpy.pi*0.5-self._shadow3_oe.T_INCIDENCE), 2), round((numpy.pi*0.5-self._shadow3_oe.T_REFLECTION), 2)

    def _set_angle_of_majax_and_pole(self, coordinates):
        grazing_angle = 0.5 * numpy.pi - coordinates.angle_radial()
        p, q = self._surface_shape.get_p_q(grazing_angle)
        zp, xp = self._get_shadow_pole_coordinates_from_p_q(p, q, grazing_angle)

        self._shadow3_oe.ELL_THE = round(self._get_shadow_angle_of_majax_and_pole(xp, zp), 4)

    @classmethod
    def _get_shadow_pole_coordinates_from_p_q(cls, p=2.0, q=1.0, grazing_angle=0.003):
        min_ax, maj_ax = Ellipsoid.get_axis_from_p_q(p, q, grazing_angle)
        c = 0.5*numpy.sqrt(p**2 + q**2 - 2*p*q*numpy.cos(numpy.pi - 2*grazing_angle))

        a = maj_ax/2
        b = min_ax/2
        eccentricity = c/a

        # see calculation of ellipse center in shadow_kernel.f90 row 3621
        xp = 0.5*(p-q)/eccentricity
        yp = -numpy.sqrt(1-(xp**2)/(a**2))*b

        return xp, yp

    @classmethod
    def _get_shadow_angle_of_majax_and_pole(cls, xp, zp):
        return numpy.degrees(abs(numpy.arctan(zp/xp)))
