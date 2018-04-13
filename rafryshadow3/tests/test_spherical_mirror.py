
from syned.storage_ring.electron_beam import ElectronBeam
from syned.storage_ring.magnetic_structures.bending_magnet import BendingMagnet
from syned.beamline.beamline_element import BeamlineElement
from syned.beamline.element_coordinates import ElementCoordinates
from syned.beamline.shape import SphericalCylinder, Rectangle, Convexity, Direction

from rafry.raytracer.raytracer import RaytracingElements, RaytracingManager, RaytracingParameters

from rafryshadow3.raytracer.shadow3_raytracer import Shadow3Raytracer
from rafryshadow3.storage_ring.light_sources.shadow3_bending_magnet_light_source import Shadow3BendingMagnetLightSource, Shadow3BendingMagnetParameters
from rafryshadow3.optical_elements.absorbers.shadow3_slit import Shadow3Slit, Shadow3SlitParameters
from rafryshadow3.optical_elements.mirrors.shadow3_mirror import Shadow3Mirror, Shadow3SphericalMirrorParameters


if __name__ == "__main__":

    raytracing_manager = RaytracingManager.Instance()
    raytracing_manager.add_raytracer(raytracer=Shadow3Raytracer())

    ##########################################

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


    slit = Shadow3Slit(name="first slit",
                       boundary_shape=Rectangle(x_left  =-0.001,
                                                x_right = 0.001,
                                                y_bottom=-0.005,
                                                y_top   = 0.005),
                       slit_parameters=Shadow3SlitParameters())

    slit_coordinates = ElementCoordinates(p=10.0, q=2.0)

    mirror = Shadow3Mirror(name="mirror 1",
                           surface_shape=SphericalCylinder(radius=0.0,
                                                           convexity=Convexity.UPWARD,
                                                           cylinder_direction=Direction.TANGENTIAL),
                           boundary_shape=Rectangle(x_left=-0.05,
                                                    x_right=0.05,
                                                    y_bottom=-0.5,
                                                    y_top=0.5),
                           mirror_parameters=Shadow3SphericalMirrorParameters(F_EXT=0,
                                                                              F_DEFAULT=0,
                                                                              SSOUR=14.0,
                                                                              SIMAG=1.0,
                                                                              THETA=88.0))

    mirror_coordinates = ElementCoordinates(p=2.0, q=1.0, angle_radial=88.0, angle_azimuthal=0.0)

    elements = RaytracingElements()
    elements.add_beamline_element(BeamlineElement(optical_element=slit, coordinates=slit_coordinates))
    elements.add_beamline_element(BeamlineElement(optical_element=mirror, coordinates=mirror_coordinates))

    raytracing_parameters = RaytracingParameters(beam=bm.generate_source(),
                                                 raytracing_elements=elements)

    beam = raytracing_manager.do_raytracing(raytracing_parameters=raytracing_parameters,
                                            handler_name=Shadow3Raytracer.HANDLER_NAME)


    import Shadow.ShadowTools as ST

    ST.plotxy(beam,1,3, nolost=True)
    # ST.histo1(beam,11)