
from rafry.beamline.decorators import OpticalElementDecorator
from rafryshadow3.raytracer.shadow3_beam import Shadow3Beam

from syned.beamline.element_coordinates import ElementCoordinates

from Shadow import OE

class Shadow3OpticalElementDecorator(OpticalElementDecorator):

    def __init__(self, additional_parameters):
        self._shadow3_oe = self._build_shadow3_oe(additional_parameters)

    def _build_shadow3_oe(self, additional_parameters):
        raise NotImplementedError("This method should be specialized by specific implementors" +
                                  "\n\nreturns " + OE.__module__ + "." + OE.__name__)

    def trace_optical_element(self, beam=Shadow3Beam(), element_coordinates=ElementCoordinates()):
        self._set_coordinates(element_coordinates)

        beam.traceOE(self._shadow3_oe, 1)

        return beam

    def _set_coordinates(self, element_coordinates=ElementCoordinates()):
        self._shadow3_oe.T_SOURCE = element_coordinates.p()
        self._shadow3_oe.T_IMAGE = element_coordinates.q()
        self._shadow3_oe.T_INCIDENCE = element_coordinates.angle_radial()
        self._shadow3_oe.ALPHA = element_coordinates.angle_azimuthal()