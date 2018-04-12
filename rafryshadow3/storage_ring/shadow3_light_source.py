

from syned.storage_ring.light_source import LightSource
from syned.storage_ring.electron_beam import ElectronBeam
from syned.storage_ring.magnetic_structure import MagneticStructure

from rafry.beamline.decorators import LightSourceDecorator
from rafryshadow3.raytracer.shadow3_beam import Shadow3Beam

class Shadow3LightSource(LightSource, LightSourceDecorator):

    def __init__(self,
                 name="Undefined",
                 electron_beam=ElectronBeam(),
                 magnetic_structure=MagneticStructure(),
                 additional_parameters=None):
        LightSource.__init__(self, name, electron_beam, magnetic_structure)

        self._shadow3_source = self._build_shadow3_source(additional_parameters)

    def _build_shadow3_source(self, additional_parameters=None):
        raise NotImplementedError("This method should be specialized by specific implementors")

    def generate_source(self, source_parameters=None):
        shadow3_beam = Shadow3Beam()
        shadow3_beam.genSource(self._shadow3_source)

        return shadow3_beam