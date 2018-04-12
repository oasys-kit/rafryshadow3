import copy, numpy

from Shadow import Beam

from rafry.raytracer.beam import Beam as RafryBeam

class Shadow3Beam(Beam, RafryBeam):

    def __init__(self, N=None):
        Beam.__init__(self, N)

    def get_number_of_rays(self):
        return self.nrays()

    def get_rays(self):
        return self.rays

    def get_ray(self, ray_index):
        return self.rays[ray_index]

    def duplicate(self):
        new_beam = Shadow3Beam()
        new_beam.rays = copy.deepcopy(self.rays)

        return new_beam

    def merge(self, other_beam):
        if other_beam:
            rays = None

            if len(getattr(other_beam, "rays", numpy.zeros(0))) > 0:
                rays = copy.deepcopy(other_beam.rays)

            if not rays is None:
                self.rays = numpy.append(self.rays, rays, axis=0)
                self.rays[:, 11] = numpy.arange(1, len(self.rays) + 1, 1) # ray_index
