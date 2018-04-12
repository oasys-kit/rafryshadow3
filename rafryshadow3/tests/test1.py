
from syned.storage_ring.electron_beam import ElectronBeam
from syned.storage_ring.magnetic_structures.bending_magnet import BendingMagnet

from rafryshadow3.storage_ring.light_sources.shadow3_bending_magnet_light_source import Shadow3BendingMagnetLightSource, Shadow3BendingMagnetParameters

if __name__ == "__main__":

    electron_beam = ElectronBeam(energy_in_GeV=2.0,
                                 energy_spread=0.80e-03,
                                 current=0.32)

    electron_beam.set_sigmas_all(sigma_x=0.2529e-3,
                                 sigma_xp=0.02881e-3,
                                 sigma_y=0.01844e-3,
                                 sigma_yp=5.235e-6)

    bm = Shadow3BendingMagnetLightSource(electron_beam=electron_beam,
                                         bending_magnet_magnetic_structure=BendingMagnet(radius=0.0,
                                                                                         magnetic_field=1.2,
                                                                                         length=0.0),
                                         bending_magnet_parameters=Shadow3BendingMagnetParameters(NPOINT=50000))


    beam = bm.generate_source()

    import Shadow.ShadowTools as ST

    ST.plotxy(beam,1,3)
    ST.histo1(beam,11)