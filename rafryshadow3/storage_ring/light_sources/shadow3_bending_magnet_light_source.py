from rafryshadow3.storage_ring.shadow3_light_source import Shadow3LightSource
from rafryshadow3.util.shadow3_util import check_file_name, init_file_name
from syned.storage_ring.magnetic_structures.bending_magnet import BendingMagnet
from syned.storage_ring.electron_beam import ElectronBeam


from Shadow import Source

class Shadow3BendingMagnetParameters():
    def __init__(self,
                 NPOINT=5000,
                 ISTAR1=6775431,
                 PH1=5000.0,
                 PH2=100000.0,
                 F_POL=3,
                 EPSI_DX=0.0,
                 EPSI_DZ=0.0,
                 HDIV1=0.0005,
                 HDIV2=0.0005,
                 VDIV1=1.0,
                 VDIV2=1.0,
                 FDISTR=4,
                 F_BOUND_SOUR=0,
                 FILE_BOUND="NONE SPECIFIED",
                 NTOTALPOINT=10000000):
        self.NPOINT = NPOINT
        self.ISTAR1 = ISTAR1
        self.PH1 = PH1
        self.PH2 = PH2
        self.F_POL = F_POL
        self.EPSI_DX = EPSI_DX
        self.EPSI_DZ = EPSI_DZ
        self.HDIV1 = HDIV1
        self.HDIV2 = HDIV2
        self.VDIV1  = VDIV1
        self.VDIV2 = VDIV2
        self.FDISTR = FDISTR
        self.F_BOUND_SOUR = F_BOUND_SOUR
        self.FILE_BOUND = FILE_BOUND
        self.NTOTALPOINT = NTOTALPOINT

class Shadow3BendingMagnetLightSource(Shadow3LightSource):

    def __init__(self,
                 name="Undefined",
                 electron_beam=ElectronBeam(),
                 bending_magnet_magnetic_structure=BendingMagnet(0,0,0),
                 bending_magnet_parameters = Shadow3BendingMagnetParameters()):
        super().__init__(name,
                         electron_beam=electron_beam,
                         magnetic_structure=bending_magnet_magnetic_structure,
                         additional_parameters=bending_magnet_parameters)

    def _build_shadow3_source(self, additional_parameters):
        shadow3_source = Source()

        shadow3_source.FSOURCE_DEPTH=4
        shadow3_source.F_COLOR=3
        shadow3_source.F_PHOT=0
        shadow3_source.F_POLAR=1
        shadow3_source.NCOL=0
        shadow3_source.N_COLOR=0
        shadow3_source.POL_DEG=0.0
        shadow3_source.SIGDIX=0.0
        shadow3_source.SIGDIZ=0.0
        shadow3_source.SIGMAY=0.0
        shadow3_source.WXSOU=0.0
        shadow3_source.WYSOU=0.0
        shadow3_source.WZSOU=0.0
        shadow3_source.OE_NUMBER=0
        shadow3_source.FILE_TRAJ=init_file_name()
        shadow3_source.FILE_SOURCE=init_file_name()
        shadow3_source.F_OPD = 1
        shadow3_source.F_SR_TYPE = 0
        shadow3_source.F_WIGGLER = 0

        # FROM SYNED #############################################
        #
        sigma_x, sigma_xp, sigma_z, sigma_zp = self._electron_beam.get_sigmas_all()

        shadow3_source.DUMMY = 100
        shadow3_source.SIGMAX = sigma_x
        shadow3_source.SIGMAZ = sigma_z
        shadow3_source.EPSI_X = sigma_x * sigma_xp
        shadow3_source.EPSI_Z = sigma_z * sigma_zp
        shadow3_source.BENER = self._electron_beam._energy_in_GeV

        if self._magnetic_structure._radius > 0:
            shadow3_source.R_MAGNET=self._magnetic_structure._radius
        elif self._magnetic_structure._magnetic_field > 0:
            shadow3_source.R_MAGNET = self._magnetic_structure.get_magnetic_radius(self._electron_beam._energy_in_GeV)

        shadow3_source.R_ALADDIN = shadow3_source.R_MAGNET * 100

        ########################################################

        shadow3_source.NPOINT       = additional_parameters.NPOINT
        shadow3_source.ISTAR1       = additional_parameters.ISTAR1
        shadow3_source.PH1          = additional_parameters.PH1
        shadow3_source.PH2          = additional_parameters.PH2
        shadow3_source.F_POL        = additional_parameters.F_POL
        shadow3_source.EPSI_DX      = additional_parameters.EPSI_DX
        shadow3_source.EPSI_DZ      = additional_parameters.EPSI_DZ
        shadow3_source.HDIV1        = additional_parameters.HDIV1
        shadow3_source.HDIV2        = additional_parameters.HDIV2
        shadow3_source.VDIV1        = additional_parameters.VDIV1
        shadow3_source.VDIV2        = additional_parameters.VDIV2
        shadow3_source.FDISTR       = additional_parameters.FDISTR
        shadow3_source.F_BOUND_SOUR = additional_parameters.F_BOUND_SOUR
        shadow3_source.FILE_BOUND   = check_file_name(additional_parameters.FILE_BOUND)
        shadow3_source.NTOTALPOINT  = additional_parameters.NTOTALPOINT

        return shadow3_source