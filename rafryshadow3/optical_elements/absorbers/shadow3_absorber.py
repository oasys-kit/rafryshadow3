import numpy

from rafryshadow3.optical_elements.shadow3_optical_element_decorator import Shadow3OpticalElementDecorator
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name
from syned.beamline.shape import BoundaryShape, Rectangle, Ellipse
from syned.beamline.element_coordinates import ElementCoordinates

from Shadow import OE

class Shadow3Absorber(Shadow3OpticalElementDecorator):

    def __init__(self, absorber_parameters):
        Shadow3OpticalElementDecorator.__init__(self, absorber_parameters)

    def _build_shadow3_oe(self, additional_parameters):
        shadow3_oe=OE()

        shadow3_oe.DUMMY=100

        shadow3_oe.FMIRR=5
        shadow3_oe.F_CRYSTAL=0
        shadow3_oe.F_REFRAC=2
        shadow3_oe.F_SCREEN=1
        shadow3_oe.N_SCREEN=1

        i_screen = numpy.zeros(10)  # after
        i_abs = numpy.zeros(10)
        i_slit = numpy.zeros(10)
        i_stop = numpy.zeros(10)
        k_slit = numpy.zeros(10)
        thick = numpy.zeros(10)
        file_abs = ['', '', '', '', '', '', '', '', '', '']
        rx_slit = numpy.zeros(10)
        rz_slit = numpy.zeros(10)
        sl_dis = numpy.zeros(10)
        file_scr_ext = ['', '', '', '', '', '', '', '', '', '']
        cx_slit = numpy.zeros(10)
        cz_slit = numpy.zeros(10)

        i_abs[0] = additional_parameters.I_ABS
        i_slit[0] = additional_parameters.I_SLIT

        if additional_parameters.I_SLIT == 1:
            i_stop[0] = additional_parameters.I_STOP

            if self._boundary_shape is None:
                k_slit[0] = 2
                file_scr_ext[0] = check_file_name(additional_parameters.FILE_SCR_EXT)
            else:
                if isinstance(self._boundary_shape, Rectangle):
                    k_slit[0] = 0
                elif isinstance(self._boundary_shape, Ellipse):
                    k_slit[0] = 1

                x_min, x_max, z_min, z_max = self._boundary_shape.get_boundaries()

                rx_slit[0] = abs(x_max - x_min)
                rz_slit[0] = abs(z_max - z_min)
                cx_slit[0] = 0.5*(x_max + x_min)
                cz_slit[0] = 0.5*(z_max + z_min)

        if additional_parameters.I_ABS == 1:
            thick[0] = additional_parameters.THICK
            file_abs[0] = check_file_name(additional_parameters.FILE_ABS)

        shadow3_oe.set_screens(1,
                               i_screen,
                               i_abs,
                               sl_dis,
                               i_slit,
                               i_stop,
                               k_slit,
                               thick,
                               numpy.array(file_abs),
                               rx_slit,
                               rz_slit,
                               cx_slit,
                               cz_slit,
                               numpy.array(file_scr_ext))

        return shadow3_oe

    def _set_coordinates(self, element_coordinates=ElementCoordinates()):
        self._shadow3_oe.T_SOURCE = element_coordinates.p()
        self._shadow3_oe.T_IMAGE = element_coordinates.q()
        self._shadow3_oe.T_INCIDENCE = 0.0
        self._shadow3_oe.T_REFLECTION = 180.0
        self._shadow3_oe.ALPHA = 0.0