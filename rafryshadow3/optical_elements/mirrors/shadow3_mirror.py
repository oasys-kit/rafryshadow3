import numpy


from rafryshadow3.optical_elements.shadow3_optical_element_decorator import Shadow3OpticalElementDecorator
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name

from syned.beamline.optical_elements.mirrors.mirror import Mirror
from syned.beamline.shape import BoundaryShape, Rectangle, Ellipse
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

class Shadow3Mirror(Mirror, Shadow3OpticalElementDecorator):
    def __init__(self,
                 name="Undefined",
                 boundary_shape=None,
                 mirror_parameters=None):
        Mirror.__init__(self,
                        name=name,
                        surface_shape=self._get_surface_shape(mirror_parameters),
                        boundary_shape=boundary_shape)
        Shadow3OpticalElementDecorator.__init__(self, mirror_parameters)

    def _get_surface_shape(self, mirror_parameters):
        raise NotImplementedError()

    def _build_shadow3_oe(self, additional_parameters):
        shadow3_oe=OE()
        shadow3_oe.DUMMY=100
        
        shadow3_oe.F_CRYSTAL=0
        shadow3_oe.F_REFRAC=2
        shadow3_oe.F_SCREEN=0
        shadow3_oe.N_SCREEN=0

        # SURFACE SHAPE

        self._set_shadow3_mirror_shape_parameters(shadow3_oe, additional_parameters)
        
        # REFLECTIVITY
        
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

        # DIMENSIONS

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
            shadow3_oe.RLEN2  = z_min
            shadow3_oe.RWIDX1 = x_max
            shadow3_oe.RWIDX2 = x_min

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
        raise NotImplementedError()

    def _set_coordinates(self, element_coordinates=ElementCoordinates()):
        super()._set_coordinates(element_coordinates)
        
        self._shadow3_oe.T_REFLECTION = element_coordinates.angle_radial()





