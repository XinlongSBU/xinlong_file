import _StarKillerMicrophysics
import f90wrap.runtime
import logging

class Actual_Burner_Module(f90wrap.runtime.FortranModule):
    """
    Module actual_burner_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 1-55
    
    """
    @staticmethod
    def actual_burner_init():
        """
        actual_burner_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 9-24
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_burner_init()
    
    @staticmethod
    def actual_burner_finalize():
        """
        actual_burner_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 26-36
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_burner_finalize()
    
    @staticmethod
    def actual_burner(state_in, state_out, dt, time):
        """
        actual_burner(state_in, state_out, dt, time)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 38-55
        
        Parameters
        ----------
        state_in : Burn_T
        state_out : Burn_T
        dt : float
        time : float
        
        """
        _StarKillerMicrophysics.f90wrap_actual_burner(state_in=state_in._handle, \
            state_out=state_out._handle, dt=dt, time=time)
    
    _dt_array_initialisers = []
    

actual_burner_module = Actual_Burner_Module()

class Actual_Network(f90wrap.runtime.FortranModule):
    """
    Module actual_network
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 1-257
    
    """
    @staticmethod
    def actual_network_init():
        """
        actual_network_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 101-205
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_network_init()
    
    @staticmethod
    def actual_network_finalize():
        """
        actual_network_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 207-236
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_network_finalize()
    
    @staticmethod
    def ener_gener_rate(dydt, enuc):
        """
        ener_gener_rate(dydt, enuc)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 238-257
        
        Parameters
        ----------
        dydt : float array
        enuc : float
        
        """
        _StarKillerMicrophysics.f90wrap_ener_gener_rate(dydt=dydt, enuc=enuc)
    
    @property
    def avo(self):
        """
        Element avo ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 10
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__avo()
    
    @property
    def c_light(self):
        """
        Element c_light ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 11
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__c_light()
    
    @property
    def enuc_conv2(self):
        """
        Element enuc_conv2 ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 12
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__enuc_conv2()
    
    @property
    def ev2erg(self):
        """
        Element ev2erg ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 14
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ev2erg()
    
    @property
    def mev2erg(self):
        """
        Element mev2erg ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 15
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mev2erg()
    
    @property
    def mev2gr(self):
        """
        Element mev2gr ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 16
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mev2gr()
    
    @property
    def mass_neutron(self):
        """
        Element mass_neutron ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 18
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mass_neutron()
    
    @property
    def mass_proton(self):
        """
        Element mass_proton ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 19
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mass_proton()
    
    @property
    def mass_electron(self):
        """
        Element mass_electron ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 20
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mass_electron()
    
    @property
    def nrates(self):
        """
        Element nrates ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 22
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nrates()
    
    @property
    def num_rate_groups(self):
        """
        Element num_rate_groups ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 23
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__num_rate_groups()
    
    @property
    def nspec_evolve(self):
        """
        Element nspec_evolve ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nspec_evolve()
    
    @property
    def naux(self):
        """
        Element naux ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 27
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__naux()
    
    @property
    def nspec(self):
        """
        Element nspec ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nspec()
    
    @property
    def nrat_reaclib(self):
        """
        Element nrat_reaclib ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 33
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nrat_reaclib()
    
    @property
    def number_reaclib_sets(self):
        """
        Element number_reaclib_sets ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 34
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_actual_network__get__number_reaclib_sets()
    
    @property
    def nrat_tabular(self):
        """
        Element nrat_tabular ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 37
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nrat_tabular()
    
    @property
    def ebind_per_nucleon(self):
        """
        Element ebind_per_nucleon ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 40
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__ebind_per_nucleon(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ebind_per_nucleon = self._arrays[array_handle]
        else:
            ebind_per_nucleon = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__ebind_per_nucleon)
            self._arrays[array_handle] = ebind_per_nucleon
        return ebind_per_nucleon
    
    @ebind_per_nucleon.setter
    def ebind_per_nucleon(self, ebind_per_nucleon):
        self.ebind_per_nucleon[...] = ebind_per_nucleon
    
    @property
    def jp(self):
        """
        Element jp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 48
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jp()
    
    @property
    def jhe4(self):
        """
        Element jhe4 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 49
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jhe4()
    
    @property
    def jo16(self):
        """
        Element jo16 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 50
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jo16()
    
    @property
    def jo20(self):
        """
        Element jo20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 51
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jo20()
    
    @property
    def jf20(self):
        """
        Element jf20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 52
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jf20()
    
    @property
    def jne20(self):
        """
        Element jne20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 53
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jne20()
    
    @property
    def jmg24(self):
        """
        Element jmg24 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 54
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jmg24()
    
    @property
    def jal27(self):
        """
        Element jal27 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 55
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jal27()
    
    @property
    def jsi28(self):
        """
        Element jsi28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 56
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jsi28()
    
    @property
    def jp31(self):
        """
        Element jp31 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 57
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__jp31()
    
    @property
    def js32(self):
        """
        Element js32 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 58
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__js32()
    
    @property
    def k_ne20__he4_o16(self):
        """
        Element k_ne20__he4_o16 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 61
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_ne20__he4_o16()
    
    @property
    def k_he4_o16__ne20(self):
        """
        Element k_he4_o16__ne20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 62
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_o16__ne20()
    
    @property
    def k_he4_ne20__mg24(self):
        """
        Element k_he4_ne20__mg24 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 63
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_ne20__mg24()
    
    @property
    def k_he4_mg24__si28(self):
        """
        Element k_he4_mg24__si28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 64
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_mg24__si28()
    
    @property
    def k_p_al27__si28(self):
        """
        Element k_p_al27__si28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 65
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_p_al27__si28()
    
    @property
    def k_he4_al27__p31(self):
        """
        Element k_he4_al27__p31 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 66
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_al27__p31()
    
    @property
    def k_he4_si28__s32(self):
        """
        Element k_he4_si28__s32 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 67
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_si28__s32()
    
    @property
    def k_p_p31__s32(self):
        """
        Element k_p_p31__s32 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 68
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_p_p31__s32()
    
    @property
    def k_o16_o16__p_p31(self):
        """
        Element k_o16_o16__p_p31 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 69
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_o16_o16__p_p31()
    
    @property
    def k_o16_o16__he4_si28(self):
        """
        Element k_o16_o16__he4_si28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 70
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_actual_network__get__k_o16_o16__he4_si28()
    
    @property
    def k_he4_mg24__p_al27(self):
        """
        Element k_he4_mg24__p_al27 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 71
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_mg24__p_al27()
    
    @property
    def k_p_al27__he4_mg24(self):
        """
        Element k_p_al27__he4_mg24 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 72
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_p_al27__he4_mg24()
    
    @property
    def k_he4_si28__p_p31(self):
        """
        Element k_he4_si28__p_p31 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 73
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_he4_si28__p_p31()
    
    @property
    def k_p_p31__he4_si28(self):
        """
        Element k_p_p31__he4_si28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 74
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_p_p31__he4_si28()
    
    @property
    def k_f20__o20(self):
        """
        Element k_f20__o20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 75
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_f20__o20()
    
    @property
    def k_ne20__f20(self):
        """
        Element k_ne20__f20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 76
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_ne20__f20()
    
    @property
    def k_o20__f20(self):
        """
        Element k_o20__f20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 77
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_o20__f20()
    
    @property
    def k_f20__ne20(self):
        """
        Element k_f20__ne20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 78
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__k_f20__ne20()
    
    @property
    def i_rate(self):
        """
        Element i_rate ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 81
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_rate()
    
    @property
    def i_drate_dt(self):
        """
        Element i_drate_dt ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 82
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_drate_dt()
    
    @property
    def i_scor(self):
        """
        Element i_scor ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 83
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_scor()
    
    @property
    def i_dscor_dt(self):
        """
        Element i_dscor_dt ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 84
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_dscor_dt()
    
    @property
    def i_dqweak(self):
        """
        Element i_dqweak ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 85
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_dqweak()
    
    @property
    def i_epart(self):
        """
        Element i_epart ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 86
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__i_epart()
    
    @property
    def spec_names(self):
        """
        Element spec_names ftype=character (len=16) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 88
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__spec_names(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            spec_names = self._arrays[array_handle]
        else:
            spec_names = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__spec_names)
            self._arrays[array_handle] = spec_names
        return spec_names
    
    @spec_names.setter
    def spec_names(self, spec_names):
        self.spec_names[...] = spec_names
    
    @property
    def short_spec_names(self):
        """
        Element short_spec_names ftype=character (len= 5) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 89
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__short_spec_names(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            short_spec_names = self._arrays[array_handle]
        else:
            short_spec_names = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__short_spec_names)
            self._arrays[array_handle] = short_spec_names
        return short_spec_names
    
    @short_spec_names.setter
    def short_spec_names(self, short_spec_names):
        self.short_spec_names[...] = short_spec_names
    
    @property
    def short_aux_names(self):
        """
        Element short_aux_names ftype=character (len= 5) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 90
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__short_aux_names(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            short_aux_names = self._arrays[array_handle]
        else:
            short_aux_names = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__short_aux_names)
            self._arrays[array_handle] = short_aux_names
        return short_aux_names
    
    @short_aux_names.setter
    def short_aux_names(self, short_aux_names):
        self.short_aux_names[...] = short_aux_names
    
    @property
    def aion(self):
        """
        Element aion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 92
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__aion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            aion = self._arrays[array_handle]
        else:
            aion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__aion)
            self._arrays[array_handle] = aion
        return aion
    
    @aion.setter
    def aion(self, aion):
        self.aion[...] = aion
    
    @property
    def zion(self):
        """
        Element zion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 92
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__zion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            zion = self._arrays[array_handle]
        else:
            zion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__zion)
            self._arrays[array_handle] = zion
        return zion
    
    @zion.setter
    def zion(self, zion):
        self.zion[...] = zion
    
    @property
    def bion(self):
        """
        Element bion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 92
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__bion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bion = self._arrays[array_handle]
        else:
            bion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__bion)
            self._arrays[array_handle] = bion
        return bion
    
    @bion.setter
    def bion(self, bion):
        self.bion[...] = bion
    
    @property
    def nion(self):
        """
        Element nion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 93
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__nion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            nion = self._arrays[array_handle]
        else:
            nion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__nion)
            self._arrays[array_handle] = nion
        return nion
    
    @nion.setter
    def nion(self, nion):
        self.nion[...] = nion
    
    @property
    def mion(self):
        """
        Element mion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 93
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__mion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            mion = self._arrays[array_handle]
        else:
            mion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__mion)
            self._arrays[array_handle] = mion
        return mion
    
    @mion.setter
    def mion(self, mion):
        self.mion[...] = mion
    
    @property
    def wion(self):
        """
        Element wion ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 93
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__wion(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            wion = self._arrays[array_handle]
        else:
            wion = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__wion)
            self._arrays[array_handle] = wion
        return wion
    
    @wion.setter
    def wion(self, wion):
        self.wion[...] = wion
    
    def __str__(self):
        ret = ['<actual_network>{\n']
        ret.append('    avo : ')
        ret.append(repr(self.avo))
        ret.append(',\n    c_light : ')
        ret.append(repr(self.c_light))
        ret.append(',\n    enuc_conv2 : ')
        ret.append(repr(self.enuc_conv2))
        ret.append(',\n    ev2erg : ')
        ret.append(repr(self.ev2erg))
        ret.append(',\n    mev2erg : ')
        ret.append(repr(self.mev2erg))
        ret.append(',\n    mev2gr : ')
        ret.append(repr(self.mev2gr))
        ret.append(',\n    mass_neutron : ')
        ret.append(repr(self.mass_neutron))
        ret.append(',\n    mass_proton : ')
        ret.append(repr(self.mass_proton))
        ret.append(',\n    mass_electron : ')
        ret.append(repr(self.mass_electron))
        ret.append(',\n    nrates : ')
        ret.append(repr(self.nrates))
        ret.append(',\n    num_rate_groups : ')
        ret.append(repr(self.num_rate_groups))
        ret.append(',\n    nspec_evolve : ')
        ret.append(repr(self.nspec_evolve))
        ret.append(',\n    naux : ')
        ret.append(repr(self.naux))
        ret.append(',\n    nspec : ')
        ret.append(repr(self.nspec))
        ret.append(',\n    nrat_reaclib : ')
        ret.append(repr(self.nrat_reaclib))
        ret.append(',\n    number_reaclib_sets : ')
        ret.append(repr(self.number_reaclib_sets))
        ret.append(',\n    nrat_tabular : ')
        ret.append(repr(self.nrat_tabular))
        ret.append(',\n    ebind_per_nucleon : ')
        ret.append(repr(self.ebind_per_nucleon))
        ret.append(',\n    jp : ')
        ret.append(repr(self.jp))
        ret.append(',\n    jhe4 : ')
        ret.append(repr(self.jhe4))
        ret.append(',\n    jo16 : ')
        ret.append(repr(self.jo16))
        ret.append(',\n    jo20 : ')
        ret.append(repr(self.jo20))
        ret.append(',\n    jf20 : ')
        ret.append(repr(self.jf20))
        ret.append(',\n    jne20 : ')
        ret.append(repr(self.jne20))
        ret.append(',\n    jmg24 : ')
        ret.append(repr(self.jmg24))
        ret.append(',\n    jal27 : ')
        ret.append(repr(self.jal27))
        ret.append(',\n    jsi28 : ')
        ret.append(repr(self.jsi28))
        ret.append(',\n    jp31 : ')
        ret.append(repr(self.jp31))
        ret.append(',\n    js32 : ')
        ret.append(repr(self.js32))
        ret.append(',\n    k_ne20__he4_o16 : ')
        ret.append(repr(self.k_ne20__he4_o16))
        ret.append(',\n    k_he4_o16__ne20 : ')
        ret.append(repr(self.k_he4_o16__ne20))
        ret.append(',\n    k_he4_ne20__mg24 : ')
        ret.append(repr(self.k_he4_ne20__mg24))
        ret.append(',\n    k_he4_mg24__si28 : ')
        ret.append(repr(self.k_he4_mg24__si28))
        ret.append(',\n    k_p_al27__si28 : ')
        ret.append(repr(self.k_p_al27__si28))
        ret.append(',\n    k_he4_al27__p31 : ')
        ret.append(repr(self.k_he4_al27__p31))
        ret.append(',\n    k_he4_si28__s32 : ')
        ret.append(repr(self.k_he4_si28__s32))
        ret.append(',\n    k_p_p31__s32 : ')
        ret.append(repr(self.k_p_p31__s32))
        ret.append(',\n    k_o16_o16__p_p31 : ')
        ret.append(repr(self.k_o16_o16__p_p31))
        ret.append(',\n    k_o16_o16__he4_si28 : ')
        ret.append(repr(self.k_o16_o16__he4_si28))
        ret.append(',\n    k_he4_mg24__p_al27 : ')
        ret.append(repr(self.k_he4_mg24__p_al27))
        ret.append(',\n    k_p_al27__he4_mg24 : ')
        ret.append(repr(self.k_p_al27__he4_mg24))
        ret.append(',\n    k_he4_si28__p_p31 : ')
        ret.append(repr(self.k_he4_si28__p_p31))
        ret.append(',\n    k_p_p31__he4_si28 : ')
        ret.append(repr(self.k_p_p31__he4_si28))
        ret.append(',\n    k_f20__o20 : ')
        ret.append(repr(self.k_f20__o20))
        ret.append(',\n    k_ne20__f20 : ')
        ret.append(repr(self.k_ne20__f20))
        ret.append(',\n    k_o20__f20 : ')
        ret.append(repr(self.k_o20__f20))
        ret.append(',\n    k_f20__ne20 : ')
        ret.append(repr(self.k_f20__ne20))
        ret.append(',\n    i_rate : ')
        ret.append(repr(self.i_rate))
        ret.append(',\n    i_drate_dt : ')
        ret.append(repr(self.i_drate_dt))
        ret.append(',\n    i_scor : ')
        ret.append(repr(self.i_scor))
        ret.append(',\n    i_dscor_dt : ')
        ret.append(repr(self.i_dscor_dt))
        ret.append(',\n    i_dqweak : ')
        ret.append(repr(self.i_dqweak))
        ret.append(',\n    i_epart : ')
        ret.append(repr(self.i_epart))
        ret.append(',\n    spec_names : ')
        ret.append(repr(self.spec_names))
        ret.append(',\n    short_spec_names : ')
        ret.append(repr(self.short_spec_names))
        ret.append(',\n    short_aux_names : ')
        ret.append(repr(self.short_aux_names))
        ret.append(',\n    aion : ')
        ret.append(repr(self.aion))
        ret.append(',\n    zion : ')
        ret.append(repr(self.zion))
        ret.append(',\n    bion : ')
        ret.append(repr(self.bion))
        ret.append(',\n    nion : ')
        ret.append(repr(self.nion))
        ret.append(',\n    mion : ')
        ret.append(repr(self.mion))
        ret.append(',\n    wion : ')
        ret.append(repr(self.wion))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

actual_network = Actual_Network()

class Actual_Rhs_Module(f90wrap.runtime.FortranModule):
    """
    Module actual_rhs_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 1-831
    
    """
    class Rate_Eval_T(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=rate_eval_t)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 12-17
        
        """
        def __init__(self, handle=None):
            """
            self = Rate_Eval_T()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 12-17
            
            
            Returns
            -------
            this : Rate_Eval_T
            	Object to be constructed
            
            
            Automatically generated constructor for rate_eval_t
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _StarKillerMicrophysics.f90wrap_rate_eval_t_initialise()
        
        def __del__(self):
            """
            Destructor for class Rate_Eval_T
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 12-17
            
            Parameters
            ----------
            this : Rate_Eval_T
            	Object to be destructed
            
            
            Automatically generated destructor for rate_eval_t
            """
            if self._alloc:
                _StarKillerMicrophysics.f90wrap_rate_eval_t_finalise(this=self._handle)
        
        @property
        def unscreened_rates(self):
            """
            Element unscreened_rates ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 13
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_rate_eval_t__array__unscreened_rates(self._handle)
            if array_handle in self._arrays:
                unscreened_rates = self._arrays[array_handle]
            else:
                unscreened_rates = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_rate_eval_t__array__unscreened_rates)
                self._arrays[array_handle] = unscreened_rates
            return unscreened_rates
        
        @unscreened_rates.setter
        def unscreened_rates(self, unscreened_rates):
            self.unscreened_rates[...] = unscreened_rates
        
        @property
        def screened_rates(self):
            """
            Element screened_rates ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 14
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_rate_eval_t__array__screened_rates(self._handle)
            if array_handle in self._arrays:
                screened_rates = self._arrays[array_handle]
            else:
                screened_rates = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_rate_eval_t__array__screened_rates)
                self._arrays[array_handle] = screened_rates
            return screened_rates
        
        @screened_rates.setter
        def screened_rates(self, screened_rates):
            self.screened_rates[...] = screened_rates
        
        @property
        def add_energy(self):
            """
            Element add_energy ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 15
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_rate_eval_t__array__add_energy(self._handle)
            if array_handle in self._arrays:
                add_energy = self._arrays[array_handle]
            else:
                add_energy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_rate_eval_t__array__add_energy)
                self._arrays[array_handle] = add_energy
            return add_energy
        
        @add_energy.setter
        def add_energy(self, add_energy):
            self.add_energy[...] = add_energy
        
        @property
        def add_energy_rate(self):
            """
            Element add_energy_rate ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 16
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_rate_eval_t__array__add_energy_rate(self._handle)
            if array_handle in self._arrays:
                add_energy_rate = self._arrays[array_handle]
            else:
                add_energy_rate = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_rate_eval_t__array__add_energy_rate)
                self._arrays[array_handle] = add_energy_rate
            return add_energy_rate
        
        @add_energy_rate.setter
        def add_energy_rate(self, add_energy_rate):
            self.add_energy_rate[...] = add_energy_rate
        
        def __str__(self):
            ret = ['<rate_eval_t>{\n']
            ret.append('    unscreened_rates : ')
            ret.append(repr(self.unscreened_rates))
            ret.append(',\n    screened_rates : ')
            ret.append(repr(self.screened_rates))
            ret.append(',\n    add_energy : ')
            ret.append(repr(self.add_energy))
            ret.append(',\n    add_energy_rate : ')
            ret.append(repr(self.add_energy_rate))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    @staticmethod
    def actual_rhs_init():
        """
        actual_rhs_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 21-25
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_rhs_init()
    
    @staticmethod
    def update_unevolved_species(self):
        """
        update_unevolved_species(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 27-35
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_update_unevolved_species(state=self._handle)
    
    @staticmethod
    def zero_rate_eval(self):
        """
        zero_rate_eval(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 37-54
        
        Parameters
        ----------
        rate_eval : Rate_Eval_T
        
        """
        _StarKillerMicrophysics.f90wrap_zero_rate_eval(rate_eval=self._handle)
    
    @staticmethod
    def evaluate_rates(self):
        """
        rate_eval = evaluate_rates(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 56-177
        
        Parameters
        ----------
        state : Burn_T
        
        Returns
        -------
        rate_eval : Rate_Eval_T
        
        """
        rate_eval = _StarKillerMicrophysics.f90wrap_evaluate_rates(state=self._handle)
        rate_eval = actual_rhs_module.Rate_Eval_T.from_handle(rate_eval)
        return rate_eval
    
    @staticmethod
    def actual_rhs(self):
        """
        actual_rhs(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 179-244
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_actual_rhs(state=self._handle)
    
    @staticmethod
    def rhs_nuc(state, ydot_nuc, y, screened_rates):
        """
        rhs_nuc(state, ydot_nuc, y, screened_rates)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 246-372
        
        Parameters
        ----------
        state : Burn_T
        ydot_nuc : float array
        y : float array
        screened_rates : float array
        
        """
        _StarKillerMicrophysics.f90wrap_rhs_nuc(state=state._handle, ydot_nuc=ydot_nuc, \
            y=y, screened_rates=screened_rates)
    
    @staticmethod
    def actual_jac(self):
        """
        actual_jac(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 374-451
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_actual_jac(state=self._handle)
    
    @staticmethod
    def jac_nuc(self, y, screened_rates):
        """
        jac_nuc(self, y, screened_rates)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 453-831
        
        Parameters
        ----------
        state : Burn_T
        y : float array
        screened_rates : float array
        
        """
        _StarKillerMicrophysics.f90wrap_jac_nuc(state=self._handle, y=y, \
            screened_rates=screened_rates)
    
    _dt_array_initialisers = []
    

actual_rhs_module = Actual_Rhs_Module()

class Burn_Type_Module(f90wrap.runtime.FortranModule):
    """
    Module burn_type_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 1-212
    
    """
    class Burn_T(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=burn_t)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 22-77
        
        """
        def __init__(self, handle=None):
            """
            self = Burn_T()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 22-77
            
            
            Returns
            -------
            this : Burn_T
            	Object to be constructed
            
            
            Automatically generated constructor for burn_t
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _StarKillerMicrophysics.f90wrap_burn_t_initialise()
        
        def __del__(self):
            """
            Destructor for class Burn_T
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 22-77
            
            Parameters
            ----------
            this : Burn_T
            	Object to be destructed
            
            
            Automatically generated destructor for burn_t
            """
            if self._alloc:
                _StarKillerMicrophysics.f90wrap_burn_t_finalise(this=self._handle)
        
        @property
        def rho(self):
            """
            Element rho ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 24
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__rho(self._handle)
        
        @rho.setter
        def rho(self, rho):
            _StarKillerMicrophysics.f90wrap_burn_t__set__rho(self._handle, rho)
        
        @property
        def t(self):
            """
            Element t ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 25
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__t(self._handle)
        
        @t.setter
        def t(self, t):
            _StarKillerMicrophysics.f90wrap_burn_t__set__t(self._handle, t)
        
        @property
        def e(self):
            """
            Element e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 26
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__e(self._handle)
        
        @e.setter
        def e(self, e):
            _StarKillerMicrophysics.f90wrap_burn_t__set__e(self._handle, e)
        
        @property
        def xn(self):
            """
            Element xn ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 27
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_burn_t__array__xn(self._handle)
            if array_handle in self._arrays:
                xn = self._arrays[array_handle]
            else:
                xn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_burn_t__array__xn)
                self._arrays[array_handle] = xn
            return xn
        
        @xn.setter
        def xn(self, xn):
            self.xn[...] = xn
        
        @property
        def cv(self):
            """
            Element cv ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 29
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cv(self._handle)
        
        @cv.setter
        def cv(self, cv):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cv(self._handle, cv)
        
        @property
        def cp(self):
            """
            Element cp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 30
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cp(self._handle)
        
        @cp.setter
        def cp(self, cp):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cp(self._handle, cp)
        
        @property
        def y_e(self):
            """
            Element y_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 31
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__y_e(self._handle)
        
        @y_e.setter
        def y_e(self, y_e):
            _StarKillerMicrophysics.f90wrap_burn_t__set__y_e(self._handle, y_e)
        
        @property
        def eta(self):
            """
            Element eta ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 32
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__eta(self._handle)
        
        @eta.setter
        def eta(self, eta):
            _StarKillerMicrophysics.f90wrap_burn_t__set__eta(self._handle, eta)
        
        @property
        def cs(self):
            """
            Element cs ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 33
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cs(self._handle)
        
        @cs.setter
        def cs(self, cs):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cs(self._handle, cs)
        
        @property
        def dx(self):
            """
            Element dx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 34
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dx(self._handle)
        
        @dx.setter
        def dx(self, dx):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dx(self._handle, dx)
        
        @property
        def abar(self):
            """
            Element abar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 35
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__abar(self._handle)
        
        @abar.setter
        def abar(self, abar):
            _StarKillerMicrophysics.f90wrap_burn_t__set__abar(self._handle, abar)
        
        @property
        def zbar(self):
            """
            Element zbar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 36
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__zbar(self._handle)
        
        @zbar.setter
        def zbar(self, zbar):
            _StarKillerMicrophysics.f90wrap_burn_t__set__zbar(self._handle, zbar)
        
        @property
        def t_old(self):
            """
            Element t_old ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 39
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__t_old(self._handle)
        
        @t_old.setter
        def t_old(self, t_old):
            _StarKillerMicrophysics.f90wrap_burn_t__set__t_old(self._handle, t_old)
        
        @property
        def dcvdt(self):
            """
            Element dcvdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 42
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dcvdt(self._handle)
        
        @dcvdt.setter
        def dcvdt(self, dcvdt):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dcvdt(self._handle, dcvdt)
        
        @property
        def dcpdt(self):
            """
            Element dcpdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 43
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dcpdt(self._handle)
        
        @dcpdt.setter
        def dcpdt(self, dcpdt):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dcpdt(self._handle, dcpdt)
        
        @property
        def ydot(self):
            """
            Element ydot ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 51
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_burn_t__array__ydot(self._handle)
            if array_handle in self._arrays:
                ydot = self._arrays[array_handle]
            else:
                ydot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_burn_t__array__ydot)
                self._arrays[array_handle] = ydot
            return ydot
        
        @ydot.setter
        def ydot(self, ydot):
            self.ydot[...] = ydot
        
        @property
        def jac(self):
            """
            Element jac ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 53
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_burn_t__array__jac(self._handle)
            if array_handle in self._arrays:
                jac = self._arrays[array_handle]
            else:
                jac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_burn_t__array__jac)
                self._arrays[array_handle] = jac
            return jac
        
        @jac.setter
        def jac(self, jac):
            self.jac[...] = jac
        
        @property
        def self_heat(self):
            """
            Element self_heat ftype=logical pytype=bool
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 57
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__self_heat(self._handle)
        
        @self_heat.setter
        def self_heat(self, self_heat):
            _StarKillerMicrophysics.f90wrap_burn_t__set__self_heat(self._handle, self_heat)
        
        @property
        def i(self):
            """
            Element i ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 61
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__i(self._handle)
        
        @i.setter
        def i(self, i):
            _StarKillerMicrophysics.f90wrap_burn_t__set__i(self._handle, i)
        
        @property
        def j(self):
            """
            Element j ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 62
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__j(self._handle)
        
        @j.setter
        def j(self, j):
            _StarKillerMicrophysics.f90wrap_burn_t__set__j(self._handle, j)
        
        @property
        def k(self):
            """
            Element k ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 63
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__k(self._handle)
        
        @k.setter
        def k(self, k):
            _StarKillerMicrophysics.f90wrap_burn_t__set__k(self._handle, k)
        
        @property
        def n_rhs(self):
            """
            Element n_rhs ftype=integer  pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 66
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__n_rhs(self._handle)
        
        @n_rhs.setter
        def n_rhs(self, n_rhs):
            _StarKillerMicrophysics.f90wrap_burn_t__set__n_rhs(self._handle, n_rhs)
        
        @property
        def n_jac(self):
            """
            Element n_jac ftype=integer  pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 67
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__n_jac(self._handle)
        
        @n_jac.setter
        def n_jac(self, n_jac):
            _StarKillerMicrophysics.f90wrap_burn_t__set__n_jac(self._handle, n_jac)
        
        @property
        def time(self):
            """
            Element time ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 71
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__time(self._handle)
        
        @time.setter
        def time(self, time):
            _StarKillerMicrophysics.f90wrap_burn_t__set__time(self._handle, time)
        
        @property
        def success(self):
            """
            Element success ftype=logical pytype=bool
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 75
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__success(self._handle)
        
        @success.setter
        def success(self, success):
            _StarKillerMicrophysics.f90wrap_burn_t__set__success(self._handle, success)
        
        def __str__(self):
            ret = ['<burn_t>{\n']
            ret.append('    rho : ')
            ret.append(repr(self.rho))
            ret.append(',\n    t : ')
            ret.append(repr(self.t))
            ret.append(',\n    e : ')
            ret.append(repr(self.e))
            ret.append(',\n    xn : ')
            ret.append(repr(self.xn))
            ret.append(',\n    cv : ')
            ret.append(repr(self.cv))
            ret.append(',\n    cp : ')
            ret.append(repr(self.cp))
            ret.append(',\n    y_e : ')
            ret.append(repr(self.y_e))
            ret.append(',\n    eta : ')
            ret.append(repr(self.eta))
            ret.append(',\n    cs : ')
            ret.append(repr(self.cs))
            ret.append(',\n    dx : ')
            ret.append(repr(self.dx))
            ret.append(',\n    abar : ')
            ret.append(repr(self.abar))
            ret.append(',\n    zbar : ')
            ret.append(repr(self.zbar))
            ret.append(',\n    t_old : ')
            ret.append(repr(self.t_old))
            ret.append(',\n    dcvdt : ')
            ret.append(repr(self.dcvdt))
            ret.append(',\n    dcpdt : ')
            ret.append(repr(self.dcpdt))
            ret.append(',\n    ydot : ')
            ret.append(repr(self.ydot))
            ret.append(',\n    jac : ')
            ret.append(repr(self.jac))
            ret.append(',\n    self_heat : ')
            ret.append(repr(self.self_heat))
            ret.append(',\n    i : ')
            ret.append(repr(self.i))
            ret.append(',\n    j : ')
            ret.append(repr(self.j))
            ret.append(',\n    k : ')
            ret.append(repr(self.k))
            ret.append(',\n    n_rhs : ')
            ret.append(repr(self.n_rhs))
            ret.append(',\n    n_jac : ')
            ret.append(repr(self.n_jac))
            ret.append(',\n    time : ')
            ret.append(repr(self.time))
            ret.append(',\n    success : ')
            ret.append(repr(self.success))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    @staticmethod
    def copy_burn_t(to_state, from_state):
        """
        copy_burn_t(to_state, from_state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 83-133
        
        Parameters
        ----------
        to_state : Burn_T
        from_state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_copy_burn_t(to_state=to_state._handle, \
            from_state=from_state._handle)
    
    @staticmethod
    def eos_to_burn(eos_state, burn_state):
        """
        eos_to_burn(eos_state, burn_state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 137-164
        
        Parameters
        ----------
        eos_state : Eos_T
        burn_state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_eos_to_burn(eos_state=eos_state._handle, \
            burn_state=burn_state._handle)
    
    @staticmethod
    def burn_to_eos(burn_state, eos_state):
        """
        burn_to_eos(burn_state, eos_state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 168-194
        
        Parameters
        ----------
        burn_state : Burn_T
        eos_state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_burn_to_eos(burn_state=burn_state._handle, \
            eos_state=eos_state._handle)
    
    @staticmethod
    def normalize_abundances_burn(state):
        """
        normalize_abundances_burn(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 196-212
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_normalize_abundances_burn(state=state._handle)
    
    @property
    def neqs(self):
        """
        Element neqs ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 15
        
        """
        return _StarKillerMicrophysics.f90wrap_burn_type_module__get__neqs()
    
    @property
    def net_itemp(self):
        """
        Element net_itemp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 19
        
        """
        return _StarKillerMicrophysics.f90wrap_burn_type_module__get__net_itemp()
    
    @property
    def net_ienuc(self):
        """
        Element net_ienuc ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 20
        
        """
        return _StarKillerMicrophysics.f90wrap_burn_type_module__get__net_ienuc()
    
    def __str__(self):
        ret = ['<burn_type_module>{\n']
        ret.append('    neqs : ')
        ret.append(repr(self.neqs))
        ret.append(',\n    net_itemp : ')
        ret.append(repr(self.net_itemp))
        ret.append(',\n    net_ienuc : ')
        ret.append(repr(self.net_ienuc))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

burn_type_module = Burn_Type_Module()

class Eos_Type_Module(f90wrap.runtime.FortranModule):
    """
    Module eos_type_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 1-482
    
    """
    class Eos_T(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=eos_t)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 109-157
        
        """
        def __init__(self, handle=None):
            """
            self = Eos_T()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 109-157
            
            
            Returns
            -------
            this : Eos_T
            	Object to be constructed
            
            
            Automatically generated constructor for eos_t
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _StarKillerMicrophysics.f90wrap_eos_t_initialise()
        
        def __del__(self):
            """
            Destructor for class Eos_T
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 109-157
            
            Parameters
            ----------
            this : Eos_T
            	Object to be destructed
            
            
            Automatically generated destructor for eos_t
            """
            if self._alloc:
                _StarKillerMicrophysics.f90wrap_eos_t_finalise(this=self._handle)
        
        @property
        def rho(self):
            """
            Element rho ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 111
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__rho(self._handle)
        
        @rho.setter
        def rho(self, rho):
            _StarKillerMicrophysics.f90wrap_eos_t__set__rho(self._handle, rho)
        
        @property
        def t(self):
            """
            Element t ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 112
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__t(self._handle)
        
        @t.setter
        def t(self, t):
            _StarKillerMicrophysics.f90wrap_eos_t__set__t(self._handle, t)
        
        @property
        def p(self):
            """
            Element p ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 113
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__p(self._handle)
        
        @p.setter
        def p(self, p):
            _StarKillerMicrophysics.f90wrap_eos_t__set__p(self._handle, p)
        
        @property
        def e(self):
            """
            Element e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 114
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__e(self._handle)
        
        @e.setter
        def e(self, e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__e(self._handle, e)
        
        @property
        def h(self):
            """
            Element h ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 115
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__h(self._handle)
        
        @h.setter
        def h(self, h):
            _StarKillerMicrophysics.f90wrap_eos_t__set__h(self._handle, h)
        
        @property
        def s(self):
            """
            Element s ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 116
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__s(self._handle)
        
        @s.setter
        def s(self, s):
            _StarKillerMicrophysics.f90wrap_eos_t__set__s(self._handle, s)
        
        @property
        def xn(self):
            """
            Element xn ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 117
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_eos_t__array__xn(self._handle)
            if array_handle in self._arrays:
                xn = self._arrays[array_handle]
            else:
                xn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_eos_t__array__xn)
                self._arrays[array_handle] = xn
            return xn
        
        @xn.setter
        def xn(self, xn):
            self.xn[...] = xn
        
        @property
        def aux(self):
            """
            Element aux ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 118
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_eos_t__array__aux(self._handle)
            if array_handle in self._arrays:
                aux = self._arrays[array_handle]
            else:
                aux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_eos_t__array__aux)
                self._arrays[array_handle] = aux
            return aux
        
        @aux.setter
        def aux(self, aux):
            self.aux[...] = aux
        
        @property
        def dpdt(self):
            """
            Element dpdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 120
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdt(self._handle)
        
        @dpdt.setter
        def dpdt(self, dpdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdt(self._handle, dpdt)
        
        @property
        def dpdr(self):
            """
            Element dpdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 121
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdr(self._handle)
        
        @dpdr.setter
        def dpdr(self, dpdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdr(self._handle, dpdr)
        
        @property
        def dedt(self):
            """
            Element dedt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 122
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedt(self._handle)
        
        @dedt.setter
        def dedt(self, dedt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedt(self._handle, dedt)
        
        @property
        def dedr(self):
            """
            Element dedr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 123
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedr(self._handle)
        
        @dedr.setter
        def dedr(self, dedr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedr(self._handle, dedr)
        
        @property
        def dhdt(self):
            """
            Element dhdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 124
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dhdt(self._handle)
        
        @dhdt.setter
        def dhdt(self, dhdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dhdt(self._handle, dhdt)
        
        @property
        def dhdr(self):
            """
            Element dhdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 125
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dhdr(self._handle)
        
        @dhdr.setter
        def dhdr(self, dhdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dhdr(self._handle, dhdr)
        
        @property
        def dsdt(self):
            """
            Element dsdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 126
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dsdt(self._handle)
        
        @dsdt.setter
        def dsdt(self, dsdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dsdt(self._handle, dsdt)
        
        @property
        def dsdr(self):
            """
            Element dsdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 127
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dsdr(self._handle)
        
        @dsdr.setter
        def dsdr(self, dsdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dsdr(self._handle, dsdr)
        
        @property
        def dpde(self):
            """
            Element dpde ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 128
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpde(self._handle)
        
        @dpde.setter
        def dpde(self, dpde):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpde(self._handle, dpde)
        
        @property
        def dpdr_e(self):
            """
            Element dpdr_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 129
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdr_e(self._handle)
        
        @dpdr_e.setter
        def dpdr_e(self, dpdr_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdr_e(self._handle, dpdr_e)
        
        @property
        def cv(self):
            """
            Element cv ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 131
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cv(self._handle)
        
        @cv.setter
        def cv(self, cv):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cv(self._handle, cv)
        
        @property
        def cp(self):
            """
            Element cp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 132
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cp(self._handle)
        
        @cp.setter
        def cp(self, cp):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cp(self._handle, cp)
        
        @property
        def xne(self):
            """
            Element xne ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 133
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__xne(self._handle)
        
        @xne.setter
        def xne(self, xne):
            _StarKillerMicrophysics.f90wrap_eos_t__set__xne(self._handle, xne)
        
        @property
        def xnp(self):
            """
            Element xnp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 134
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__xnp(self._handle)
        
        @xnp.setter
        def xnp(self, xnp):
            _StarKillerMicrophysics.f90wrap_eos_t__set__xnp(self._handle, xnp)
        
        @property
        def eta(self):
            """
            Element eta ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 135
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__eta(self._handle)
        
        @eta.setter
        def eta(self, eta):
            _StarKillerMicrophysics.f90wrap_eos_t__set__eta(self._handle, eta)
        
        @property
        def pele(self):
            """
            Element pele ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 136
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__pele(self._handle)
        
        @pele.setter
        def pele(self, pele):
            _StarKillerMicrophysics.f90wrap_eos_t__set__pele(self._handle, pele)
        
        @property
        def ppos(self):
            """
            Element ppos ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 137
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__ppos(self._handle)
        
        @ppos.setter
        def ppos(self, ppos):
            _StarKillerMicrophysics.f90wrap_eos_t__set__ppos(self._handle, ppos)
        
        @property
        def mu(self):
            """
            Element mu ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 138
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__mu(self._handle)
        
        @mu.setter
        def mu(self, mu):
            _StarKillerMicrophysics.f90wrap_eos_t__set__mu(self._handle, mu)
        
        @property
        def mu_e(self):
            """
            Element mu_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 139
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__mu_e(self._handle)
        
        @mu_e.setter
        def mu_e(self, mu_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__mu_e(self._handle, mu_e)
        
        @property
        def y_e(self):
            """
            Element y_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 140
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__y_e(self._handle)
        
        @y_e.setter
        def y_e(self, y_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__y_e(self._handle, y_e)
        
        @property
        def dedx(self):
            """
            Element dedx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 141
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_eos_t__array__dedx(self._handle)
            if array_handle in self._arrays:
                dedx = self._arrays[array_handle]
            else:
                dedx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_eos_t__array__dedx)
                self._arrays[array_handle] = dedx
            return dedx
        
        @dedx.setter
        def dedx(self, dedx):
            self.dedx[...] = dedx
        
        @property
        def dpdx(self):
            """
            Element dpdx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 142
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_eos_t__array__dpdx(self._handle)
            if array_handle in self._arrays:
                dpdx = self._arrays[array_handle]
            else:
                dpdx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_eos_t__array__dpdx)
                self._arrays[array_handle] = dpdx
            return dpdx
        
        @dpdx.setter
        def dpdx(self, dpdx):
            self.dpdx[...] = dpdx
        
        @property
        def dhdx(self):
            """
            Element dhdx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 143
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _StarKillerMicrophysics.f90wrap_eos_t__array__dhdx(self._handle)
            if array_handle in self._arrays:
                dhdx = self._arrays[array_handle]
            else:
                dhdx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _StarKillerMicrophysics.f90wrap_eos_t__array__dhdx)
                self._arrays[array_handle] = dhdx
            return dhdx
        
        @dhdx.setter
        def dhdx(self, dhdx):
            self.dhdx[...] = dhdx
        
        @property
        def gam1(self):
            """
            Element gam1 ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 144
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__gam1(self._handle)
        
        @gam1.setter
        def gam1(self, gam1):
            _StarKillerMicrophysics.f90wrap_eos_t__set__gam1(self._handle, gam1)
        
        @property
        def cs(self):
            """
            Element cs ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 145
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cs(self._handle)
        
        @cs.setter
        def cs(self, cs):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cs(self._handle, cs)
        
        @property
        def abar(self):
            """
            Element abar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 147
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__abar(self._handle)
        
        @abar.setter
        def abar(self, abar):
            _StarKillerMicrophysics.f90wrap_eos_t__set__abar(self._handle, abar)
        
        @property
        def zbar(self):
            """
            Element zbar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 148
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__zbar(self._handle)
        
        @zbar.setter
        def zbar(self, zbar):
            _StarKillerMicrophysics.f90wrap_eos_t__set__zbar(self._handle, zbar)
        
        @property
        def dpda(self):
            """
            Element dpda ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 150
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpda(self._handle)
        
        @dpda.setter
        def dpda(self, dpda):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpda(self._handle, dpda)
        
        @property
        def dpdz(self):
            """
            Element dpdz ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 151
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdz(self._handle)
        
        @dpdz.setter
        def dpdz(self, dpdz):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdz(self._handle, dpdz)
        
        @property
        def deda(self):
            """
            Element deda ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 152
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__deda(self._handle)
        
        @deda.setter
        def deda(self, deda):
            _StarKillerMicrophysics.f90wrap_eos_t__set__deda(self._handle, deda)
        
        @property
        def dedz(self):
            """
            Element dedz ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 153
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedz(self._handle)
        
        @dedz.setter
        def dedz(self, dedz):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedz(self._handle, dedz)
        
        @property
        def conductivity(self):
            """
            Element conductivity ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 155
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__conductivity(self._handle)
        
        @conductivity.setter
        def conductivity(self, conductivity):
            _StarKillerMicrophysics.f90wrap_eos_t__set__conductivity(self._handle, \
                conductivity)
        
        def __str__(self):
            ret = ['<eos_t>{\n']
            ret.append('    rho : ')
            ret.append(repr(self.rho))
            ret.append(',\n    t : ')
            ret.append(repr(self.t))
            ret.append(',\n    p : ')
            ret.append(repr(self.p))
            ret.append(',\n    e : ')
            ret.append(repr(self.e))
            ret.append(',\n    h : ')
            ret.append(repr(self.h))
            ret.append(',\n    s : ')
            ret.append(repr(self.s))
            ret.append(',\n    xn : ')
            ret.append(repr(self.xn))
            ret.append(',\n    aux : ')
            ret.append(repr(self.aux))
            ret.append(',\n    dpdt : ')
            ret.append(repr(self.dpdt))
            ret.append(',\n    dpdr : ')
            ret.append(repr(self.dpdr))
            ret.append(',\n    dedt : ')
            ret.append(repr(self.dedt))
            ret.append(',\n    dedr : ')
            ret.append(repr(self.dedr))
            ret.append(',\n    dhdt : ')
            ret.append(repr(self.dhdt))
            ret.append(',\n    dhdr : ')
            ret.append(repr(self.dhdr))
            ret.append(',\n    dsdt : ')
            ret.append(repr(self.dsdt))
            ret.append(',\n    dsdr : ')
            ret.append(repr(self.dsdr))
            ret.append(',\n    dpde : ')
            ret.append(repr(self.dpde))
            ret.append(',\n    dpdr_e : ')
            ret.append(repr(self.dpdr_e))
            ret.append(',\n    cv : ')
            ret.append(repr(self.cv))
            ret.append(',\n    cp : ')
            ret.append(repr(self.cp))
            ret.append(',\n    xne : ')
            ret.append(repr(self.xne))
            ret.append(',\n    xnp : ')
            ret.append(repr(self.xnp))
            ret.append(',\n    eta : ')
            ret.append(repr(self.eta))
            ret.append(',\n    pele : ')
            ret.append(repr(self.pele))
            ret.append(',\n    ppos : ')
            ret.append(repr(self.ppos))
            ret.append(',\n    mu : ')
            ret.append(repr(self.mu))
            ret.append(',\n    mu_e : ')
            ret.append(repr(self.mu_e))
            ret.append(',\n    y_e : ')
            ret.append(repr(self.y_e))
            ret.append(',\n    dedx : ')
            ret.append(repr(self.dedx))
            ret.append(',\n    dpdx : ')
            ret.append(repr(self.dpdx))
            ret.append(',\n    dhdx : ')
            ret.append(repr(self.dhdx))
            ret.append(',\n    gam1 : ')
            ret.append(repr(self.gam1))
            ret.append(',\n    cs : ')
            ret.append(repr(self.cs))
            ret.append(',\n    abar : ')
            ret.append(repr(self.abar))
            ret.append(',\n    zbar : ')
            ret.append(repr(self.zbar))
            ret.append(',\n    dpda : ')
            ret.append(repr(self.dpda))
            ret.append(',\n    dpdz : ')
            ret.append(repr(self.dpdz))
            ret.append(',\n    deda : ')
            ret.append(repr(self.deda))
            ret.append(',\n    dedz : ')
            ret.append(repr(self.dedz))
            ret.append(',\n    conductivity : ')
            ret.append(repr(self.conductivity))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    @staticmethod
    def copy_eos_t(self, from_eos):
        """
        copy_eos_t(self, from_eos)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 163-220
        
        Parameters
        ----------
        to_eos : Eos_T
        from_eos : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_copy_eos_t(to_eos=self._handle, \
            from_eos=from_eos._handle)
    
    @staticmethod
    def composition(state):
        """
        composition(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 225-250
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_composition(state=state._handle)
    
    @staticmethod
    def composition_derivatives(state):
        """
        composition_derivatives(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 254-284
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_composition_derivatives(state=state._handle)
    
    @staticmethod
    def normalize_abundances(state):
        """
        normalize_abundances(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 289-305
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_normalize_abundances(state=state._handle)
    
    @staticmethod
    def clean_state(state):
        """
        clean_state(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 309-322
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_clean_state(state=state._handle)
    
    @staticmethod
    def print_state(state):
        """
        print_state(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 326-338
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_print_state(state=state._handle)
    
    @staticmethod
    def eos_get_small_temp():
        """
        small_temp_out = eos_get_small_temp()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 340-354
        
        
        Returns
        -------
        small_temp_out : float
        
        """
        small_temp_out = _StarKillerMicrophysics.f90wrap_eos_get_small_temp()
        return small_temp_out
    
    @staticmethod
    def eos_get_small_dens():
        """
        small_dens_out = eos_get_small_dens()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 356-370
        
        
        Returns
        -------
        small_dens_out : float
        
        """
        small_dens_out = _StarKillerMicrophysics.f90wrap_eos_get_small_dens()
        return small_dens_out
    
    @staticmethod
    def eos_get_max_temp():
        """
        max_temp_out = eos_get_max_temp()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 372-386
        
        
        Returns
        -------
        max_temp_out : float
        
        """
        max_temp_out = _StarKillerMicrophysics.f90wrap_eos_get_max_temp()
        return max_temp_out
    
    @staticmethod
    def eos_get_max_dens():
        """
        max_dens_out = eos_get_max_dens()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 388-401
        
        
        Returns
        -------
        max_dens_out : float
        
        """
        max_dens_out = _StarKillerMicrophysics.f90wrap_eos_get_max_dens()
        return max_dens_out
    
    @staticmethod
    def eos_input_has_var(input, ivar):
        """
        has = eos_input_has_var(input, ivar)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 405-482
        
        Parameters
        ----------
        input : int
        ivar : int
        
        Returns
        -------
        has : bool
        
        """
        has = _StarKillerMicrophysics.f90wrap_eos_input_has_var(input=input, ivar=ivar)
        return has
    
    @property
    def eos_input_rt(self):
        """
        Element eos_input_rt ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 11
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rt()
    
    @property
    def eos_input_rh(self):
        """
        Element eos_input_rh ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 12
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rh()
    
    @property
    def eos_input_tp(self):
        """
        Element eos_input_tp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 13
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_tp()
    
    @property
    def eos_input_rp(self):
        """
        Element eos_input_rp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 14
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rp()
    
    @property
    def eos_input_re(self):
        """
        Element eos_input_re ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 15
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_re()
    
    @property
    def eos_input_ps(self):
        """
        Element eos_input_ps ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 16
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_ps()
    
    @property
    def eos_input_ph(self):
        """
        Element eos_input_ph ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 17
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_ph()
    
    @property
    def eos_input_th(self):
        """
        Element eos_input_th ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 18
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_th()
    
    @property
    def itemp(self):
        """
        Element itemp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 22
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__itemp()
    
    @property
    def idens(self):
        """
        Element idens ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 23
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__idens()
    
    @property
    def iener(self):
        """
        Element iener ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 24
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__iener()
    
    @property
    def ienth(self):
        """
        Element ienth ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 25
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ienth()
    
    @property
    def ientr(self):
        """
        Element ientr ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ientr()
    
    @property
    def ipres(self):
        """
        Element ipres ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 27
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ipres()
    
    @property
    def ierr_general(self):
        """
        Element ierr_general ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_general()
    
    @property
    def ierr_input(self):
        """
        Element ierr_input ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 31
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_input()
    
    @property
    def ierr_iter_conv(self):
        """
        Element ierr_iter_conv ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 32
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_iter_conv()
    
    @property
    def ierr_neg_e(self):
        """
        Element ierr_neg_e ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 33
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_e()
    
    @property
    def ierr_neg_p(self):
        """
        Element ierr_neg_p ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 34
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_p()
    
    @property
    def ierr_neg_h(self):
        """
        Element ierr_neg_h ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 35
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_h()
    
    @property
    def ierr_neg_s(self):
        """
        Element ierr_neg_s ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 36
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_s()
    
    @property
    def ierr_iter_var(self):
        """
        Element ierr_iter_var ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 37
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_iter_var()
    
    @property
    def ierr_init(self):
        """
        Element ierr_init ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 38
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_init()
    
    @property
    def ierr_init_xn(self):
        """
        Element ierr_init_xn ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 39
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_init_xn()
    
    @property
    def ierr_out_of_bounds(self):
        """
        Element ierr_out_of_bounds ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 40
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_out_of_bounds()
    
    @property
    def ierr_not_implemented(self):
        """
        Element ierr_not_implemented ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 41
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_not_implemented()
    
    @property
    def mintemp(self):
        """
        Element mintemp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 45
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mintemp()
    
    @mintemp.setter
    def mintemp(self, mintemp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mintemp(mintemp)
    
    @property
    def maxtemp(self):
        """
        Element maxtemp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 46
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxtemp()
    
    @maxtemp.setter
    def maxtemp(self, maxtemp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxtemp(maxtemp)
    
    @property
    def mindens(self):
        """
        Element mindens ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 47
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mindens()
    
    @mindens.setter
    def mindens(self, mindens):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mindens(mindens)
    
    @property
    def maxdens(self):
        """
        Element maxdens ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 48
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxdens()
    
    @maxdens.setter
    def maxdens(self, maxdens):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxdens(maxdens)
    
    @property
    def minx(self):
        """
        Element minx ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 49
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minx()
    
    @minx.setter
    def minx(self, minx):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minx(minx)
    
    @property
    def maxx(self):
        """
        Element maxx ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 50
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxx()
    
    @maxx.setter
    def maxx(self, maxx):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxx(maxx)
    
    @property
    def minye(self):
        """
        Element minye ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 51
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minye()
    
    @minye.setter
    def minye(self, minye):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minye(minye)
    
    @property
    def maxye(self):
        """
        Element maxye ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 52
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxye()
    
    @maxye.setter
    def maxye(self, maxye):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxye(maxye)
    
    @property
    def mine(self):
        """
        Element mine ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 53
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mine()
    
    @mine.setter
    def mine(self, mine):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mine(mine)
    
    @property
    def maxe(self):
        """
        Element maxe ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 54
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxe()
    
    @maxe.setter
    def maxe(self, maxe):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxe(maxe)
    
    @property
    def minp(self):
        """
        Element minp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 55
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minp()
    
    @minp.setter
    def minp(self, minp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minp(minp)
    
    @property
    def maxp(self):
        """
        Element maxp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 56
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxp()
    
    @maxp.setter
    def maxp(self, maxp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxp(maxp)
    
    @property
    def mins(self):
        """
        Element mins ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 57
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mins()
    
    @mins.setter
    def mins(self, mins):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mins(mins)
    
    @property
    def maxs(self):
        """
        Element maxs ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 58
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxs()
    
    @maxs.setter
    def maxs(self, maxs):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxs(maxs)
    
    @property
    def minh(self):
        """
        Element minh ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 59
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minh()
    
    @minh.setter
    def minh(self, minh):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minh(minh)
    
    @property
    def maxh(self):
        """
        Element maxh ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 60
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxh()
    
    @maxh.setter
    def maxh(self, maxh):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxh(maxh)
    
    def __str__(self):
        ret = ['<eos_type_module>{\n']
        ret.append('    eos_input_rt : ')
        ret.append(repr(self.eos_input_rt))
        ret.append(',\n    eos_input_rh : ')
        ret.append(repr(self.eos_input_rh))
        ret.append(',\n    eos_input_tp : ')
        ret.append(repr(self.eos_input_tp))
        ret.append(',\n    eos_input_rp : ')
        ret.append(repr(self.eos_input_rp))
        ret.append(',\n    eos_input_re : ')
        ret.append(repr(self.eos_input_re))
        ret.append(',\n    eos_input_ps : ')
        ret.append(repr(self.eos_input_ps))
        ret.append(',\n    eos_input_ph : ')
        ret.append(repr(self.eos_input_ph))
        ret.append(',\n    eos_input_th : ')
        ret.append(repr(self.eos_input_th))
        ret.append(',\n    itemp : ')
        ret.append(repr(self.itemp))
        ret.append(',\n    idens : ')
        ret.append(repr(self.idens))
        ret.append(',\n    iener : ')
        ret.append(repr(self.iener))
        ret.append(',\n    ienth : ')
        ret.append(repr(self.ienth))
        ret.append(',\n    ientr : ')
        ret.append(repr(self.ientr))
        ret.append(',\n    ipres : ')
        ret.append(repr(self.ipres))
        ret.append(',\n    ierr_general : ')
        ret.append(repr(self.ierr_general))
        ret.append(',\n    ierr_input : ')
        ret.append(repr(self.ierr_input))
        ret.append(',\n    ierr_iter_conv : ')
        ret.append(repr(self.ierr_iter_conv))
        ret.append(',\n    ierr_neg_e : ')
        ret.append(repr(self.ierr_neg_e))
        ret.append(',\n    ierr_neg_p : ')
        ret.append(repr(self.ierr_neg_p))
        ret.append(',\n    ierr_neg_h : ')
        ret.append(repr(self.ierr_neg_h))
        ret.append(',\n    ierr_neg_s : ')
        ret.append(repr(self.ierr_neg_s))
        ret.append(',\n    ierr_iter_var : ')
        ret.append(repr(self.ierr_iter_var))
        ret.append(',\n    ierr_init : ')
        ret.append(repr(self.ierr_init))
        ret.append(',\n    ierr_init_xn : ')
        ret.append(repr(self.ierr_init_xn))
        ret.append(',\n    ierr_out_of_bounds : ')
        ret.append(repr(self.ierr_out_of_bounds))
        ret.append(',\n    ierr_not_implemented : ')
        ret.append(repr(self.ierr_not_implemented))
        ret.append(',\n    mintemp : ')
        ret.append(repr(self.mintemp))
        ret.append(',\n    maxtemp : ')
        ret.append(repr(self.maxtemp))
        ret.append(',\n    mindens : ')
        ret.append(repr(self.mindens))
        ret.append(',\n    maxdens : ')
        ret.append(repr(self.maxdens))
        ret.append(',\n    minx : ')
        ret.append(repr(self.minx))
        ret.append(',\n    maxx : ')
        ret.append(repr(self.maxx))
        ret.append(',\n    minye : ')
        ret.append(repr(self.minye))
        ret.append(',\n    maxye : ')
        ret.append(repr(self.maxye))
        ret.append(',\n    mine : ')
        ret.append(repr(self.mine))
        ret.append(',\n    maxe : ')
        ret.append(repr(self.maxe))
        ret.append(',\n    minp : ')
        ret.append(repr(self.minp))
        ret.append(',\n    maxp : ')
        ret.append(repr(self.maxp))
        ret.append(',\n    mins : ')
        ret.append(repr(self.mins))
        ret.append(',\n    maxs : ')
        ret.append(repr(self.maxs))
        ret.append(',\n    minh : ')
        ret.append(repr(self.minh))
        ret.append(',\n    maxh : ')
        ret.append(repr(self.maxh))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

eos_type_module = Eos_Type_Module()

class Eos_Module(f90wrap.runtime.FortranModule):
    """
    Module eos_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 1-596
    
    """
    @staticmethod
    def eos_init(small_temp=None, small_dens=None):
        """
        eos_init([small_temp, small_dens])
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 14-107
        
        Parameters
        ----------
        small_temp : float
        small_dens : float
        
        """
        _StarKillerMicrophysics.f90wrap_eos_init(small_temp=small_temp, \
            small_dens=small_dens)
    
    @staticmethod
    def eos_finalize():
        """
        eos_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 109-118
        
        
        """
        _StarKillerMicrophysics.f90wrap_eos_finalize()
    
    @staticmethod
    def eos(input, state):
        """
        eos(input, state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 120-172
        
        Parameters
        ----------
        input : int
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_eos(input=input, state=state._handle)
    
    @staticmethod
    def reset_inputs(input, state, has_been_reset):
        """
        reset_inputs(input, state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 174-237
        
        Parameters
        ----------
        input : int
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_inputs(input=input, state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_rho(state, has_been_reset):
        """
        reset_rho(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 241-258
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_rho(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_t(state, has_been_reset):
        """
        reset_t(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 262-279
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_t(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_e(state, has_been_reset):
        """
        reset_e(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 281-300
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_e(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_h(state, has_been_reset):
        """
        reset_h(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 302-321
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_h(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_s(state, has_been_reset):
        """
        reset_s(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 323-342
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_s(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def reset_p(state, has_been_reset):
        """
        reset_p(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 344-363
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_reset_p(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def eos_reset(state, has_been_reset):
        """
        eos_reset(state, has_been_reset)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 368-391
        
        Parameters
        ----------
        state : Eos_T
        has_been_reset : bool
        
        """
        _StarKillerMicrophysics.f90wrap_eos_reset(state=state._handle, \
            has_been_reset=has_been_reset)
    
    @staticmethod
    def check_inputs(input, state):
        """
        check_inputs(input, state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 393-472
        
        Parameters
        ----------
        input : int
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_inputs(input=input, state=state._handle)
    
    @staticmethod
    def check_rho(state):
        """
        check_rho(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 474-493
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_rho(state=state._handle)
    
    @staticmethod
    def check_t(state):
        """
        check_t(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 495-514
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_t(state=state._handle)
    
    @staticmethod
    def check_e(state):
        """
        check_e(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 516-535
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_e(state=state._handle)
    
    @staticmethod
    def check_h(state):
        """
        check_h(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 537-556
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_h(state=state._handle)
    
    @staticmethod
    def check_s(state):
        """
        check_s(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 558-577
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_s(state=state._handle)
    
    @staticmethod
    def check_p(state):
        """
        check_p(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 579-596
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_p(state=state._handle)
    
    @property
    def initialized(self):
        """
        Element initialized ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 line 7
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_module__get__initialized()
    
    @initialized.setter
    def initialized(self, initialized):
        _StarKillerMicrophysics.f90wrap_eos_module__set__initialized(initialized)
    
    def __str__(self):
        ret = ['<eos_module>{\n']
        ret.append('    initialized : ')
        ret.append(repr(self.initialized))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

eos_module = Eos_Module()

class Network(f90wrap.runtime.FortranModule):
    """
    Module network
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 22-129
    
    """
    @staticmethod
    def network_init():
        """
        network_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 39-73
        
        
        """
        _StarKillerMicrophysics.f90wrap_network_init()
    
    @staticmethod
    def network_species_index(name):
        """
        r = network_species_index(name)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 75-90
        
        Parameters
        ----------
        name : str
        
        Returns
        -------
        r : int
        
        """
        r = _StarKillerMicrophysics.f90wrap_network_species_index(name=name)
        return r
    
    @staticmethod
    def get_network_species_name(index_bn):
        """
        name = get_network_species_name(index_bn)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 92-104
        
        Parameters
        ----------
        index_bn : int
        
        Returns
        -------
        name : str
        
        """
        name = \
            _StarKillerMicrophysics.f90wrap_get_network_species_name(index_bn=index_bn)
        return name
    
    @staticmethod
    def get_network_short_species_name(index_bn):
        """
        name = get_network_short_species_name(index_bn)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 106-118
        
        Parameters
        ----------
        index_bn : int
        
        Returns
        -------
        name : str
        
        """
        name = \
            _StarKillerMicrophysics.f90wrap_get_network_short_species_name(index_bn=index_bn)
        return name
    
    @staticmethod
    def network_finalize():
        """
        network_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 120-129
        
        
        """
        _StarKillerMicrophysics.f90wrap_network_finalize()
    
    @property
    def network_initialized(self):
        """
        Element network_initialized ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 line 29
        
        """
        return _StarKillerMicrophysics.f90wrap_network__get__network_initialized()
    
    @network_initialized.setter
    def network_initialized(self, network_initialized):
        \
            _StarKillerMicrophysics.f90wrap_network__set__network_initialized(network_initialized)
    
    @property
    def aion_inv(self):
        """
        Element aion_inv ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 line 32
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_network__array__aion_inv(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            aion_inv = self._arrays[array_handle]
        else:
            aion_inv = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_network__array__aion_inv)
            self._arrays[array_handle] = aion_inv
        return aion_inv
    
    @aion_inv.setter
    def aion_inv(self, aion_inv):
        self.aion_inv[...] = aion_inv
    
    def __str__(self):
        ret = ['<network>{\n']
        ret.append('    network_initialized : ')
        ret.append(repr(self.network_initialized))
        ret.append(',\n    aion_inv : ')
        ret.append(repr(self.aion_inv))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

network = Network()

class Microphysics_Module(f90wrap.runtime.FortranModule):
    """
    Module microphysics_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 1-45
    
    """
    @staticmethod
    def microphysics_init(small_temp=None, small_dens=None):
        """
        microphysics_init([small_temp, small_dens])
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 15-37
        
        Parameters
        ----------
        small_temp : unknown
        small_dens : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_microphysics_init(small_temp=small_temp, \
            small_dens=small_dens)
    
    @staticmethod
    def microphysics_finalize():
        """
        microphysics_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 39-45
        
        
        """
        _StarKillerMicrophysics.f90wrap_microphysics_finalize()
    
    _dt_array_initialisers = []
    

microphysics_module = Microphysics_Module()

class Extern_Probin_Module(f90wrap.runtime.FortranModule):
    """
    Module extern_probin_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 lines 12-98
    
    """
    @property
    def small_temp(self):
        """
        Element small_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 20
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__small_temp()
    
    @small_temp.setter
    def small_temp(self, small_temp):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__small_temp(small_temp)
    
    @property
    def small_dens(self):
        """
        Element small_dens ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 22
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__small_dens()
    
    @small_dens.setter
    def small_dens(self, small_dens):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__small_dens(small_dens)
    
    @property
    def use_eos_coulomb(self):
        """
        Element use_eos_coulomb ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 24
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_eos_coulomb()
    
    @use_eos_coulomb.setter
    def use_eos_coulomb(self, use_eos_coulomb):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_eos_coulomb(use_eos_coulomb)
    
    @property
    def eos_input_is_constant(self):
        """
        Element eos_input_is_constant ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 26
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__eos_input_is_constant()
    
    @eos_input_is_constant.setter
    def eos_input_is_constant(self, eos_input_is_constant):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__eos_input_is_constant(eos_input_is_constant)
    
    @property
    def eos_ttol(self):
        """
        Element eos_ttol ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 28
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__eos_ttol()
    
    @eos_ttol.setter
    def eos_ttol(self, eos_ttol):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__eos_ttol(eos_ttol)
    
    @property
    def eos_dtol(self):
        """
        Element eos_dtol ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__eos_dtol()
    
    @eos_dtol.setter
    def eos_dtol(self, eos_dtol):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__eos_dtol(eos_dtol)
    
    @property
    def small_x(self):
        """
        Element small_x ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 32
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__small_x()
    
    @small_x.setter
    def small_x(self, small_x):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__small_x(small_x)
    
    @property
    def use_tables(self):
        """
        Element use_tables ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 34
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_tables()
    
    @use_tables.setter
    def use_tables(self, use_tables):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_tables(use_tables)
    
    @property
    def use_c12ag_deboer17(self):
        """
        Element use_c12ag_deboer17 ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 36
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_c12ag_deboer17()
    
    @use_c12ag_deboer17.setter
    def use_c12ag_deboer17(self, use_c12ag_deboer17):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_c12ag_deboer17(use_c12ag_deboer17)
    
    @property
    def disable_thermal_neutrinos(self):
        """
        Element disable_thermal_neutrinos ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 38
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__disable_thermal_neutrinos()
    
    @disable_thermal_neutrinos.setter
    def disable_thermal_neutrinos(self, disable_thermal_neutrinos):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__disable_thermal_neutrinos(disable_thermal_neutrinos)
    
    @property
    def use_jacobian_caching(self):
        """
        Element use_jacobian_caching ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 40
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_jacobian_caching()
    
    @use_jacobian_caching.setter
    def use_jacobian_caching(self, use_jacobian_caching):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_jacobian_caching(use_jacobian_caching)
    
    @property
    def do_constant_volume_burn(self):
        """
        Element do_constant_volume_burn ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 42
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__do_constant_volume_burn()
    
    @do_constant_volume_burn.setter
    def do_constant_volume_burn(self, do_constant_volume_burn):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__do_constant_volume_burn(do_constant_volume_burn)
    
    @property
    def call_eos_in_rhs(self):
        """
        Element call_eos_in_rhs ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 44
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__call_eos_in_rhs()
    
    @call_eos_in_rhs.setter
    def call_eos_in_rhs(self, call_eos_in_rhs):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__call_eos_in_rhs(call_eos_in_rhs)
    
    @property
    def dt_crit(self):
        """
        Element dt_crit ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 46
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__dt_crit()
    
    @dt_crit.setter
    def dt_crit(self, dt_crit):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__dt_crit(dt_crit)
    
    @property
    def burning_mode(self):
        """
        Element burning_mode ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 48
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__burning_mode()
    
    @burning_mode.setter
    def burning_mode(self, burning_mode):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__burning_mode(burning_mode)
    
    @property
    def burning_mode_factor(self):
        """
        Element burning_mode_factor ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 50
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__burning_mode_factor()
    
    @burning_mode_factor.setter
    def burning_mode_factor(self, burning_mode_factor):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__burning_mode_factor(burning_mode_factor)
    
    @property
    def integrate_temperature(self):
        """
        Element integrate_temperature ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 52
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__integrate_temperature()
    
    @integrate_temperature.setter
    def integrate_temperature(self, integrate_temperature):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__integrate_temperature(integrate_temperature)
    
    @property
    def integrate_energy(self):
        """
        Element integrate_energy ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 54
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__integrate_energy()
    
    @integrate_energy.setter
    def integrate_energy(self, integrate_energy):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__integrate_energy(integrate_energy)
    
    @property
    def jacobian(self):
        """
        Element jacobian ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 56
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__jacobian()
    
    @jacobian.setter
    def jacobian(self, jacobian):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__jacobian(jacobian)
    
    @property
    def centered_diff_jac(self):
        """
        Element centered_diff_jac ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 58
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__centered_diff_jac()
    
    @centered_diff_jac.setter
    def centered_diff_jac(self, centered_diff_jac):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__centered_diff_jac(centered_diff_jac)
    
    @property
    def burner_verbose(self):
        """
        Element burner_verbose ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 60
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__burner_verbose()
    
    @burner_verbose.setter
    def burner_verbose(self, burner_verbose):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__burner_verbose(burner_verbose)
    
    @property
    def rtol_spec(self):
        """
        Element rtol_spec ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 62
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_spec()
    
    @rtol_spec.setter
    def rtol_spec(self, rtol_spec):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_spec(rtol_spec)
    
    @property
    def rtol_temp(self):
        """
        Element rtol_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 64
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_temp()
    
    @rtol_temp.setter
    def rtol_temp(self, rtol_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_temp(rtol_temp)
    
    @property
    def rtol_enuc(self):
        """
        Element rtol_enuc ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 66
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_enuc()
    
    @rtol_enuc.setter
    def rtol_enuc(self, rtol_enuc):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_enuc(rtol_enuc)
    
    @property
    def atol_spec(self):
        """
        Element atol_spec ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 68
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_spec()
    
    @atol_spec.setter
    def atol_spec(self, atol_spec):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_spec(atol_spec)
    
    @property
    def atol_temp(self):
        """
        Element atol_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 70
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_temp()
    
    @atol_temp.setter
    def atol_temp(self, atol_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_temp(atol_temp)
    
    @property
    def atol_enuc(self):
        """
        Element atol_enuc ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 72
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_enuc()
    
    @atol_enuc.setter
    def atol_enuc(self, atol_enuc):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_enuc(atol_enuc)
    
    @property
    def retry_burn(self):
        """
        Element retry_burn ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 74
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__retry_burn()
    
    @retry_burn.setter
    def retry_burn(self, retry_burn):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__retry_burn(retry_burn)
    
    @property
    def retry_burn_factor(self):
        """
        Element retry_burn_factor ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 76
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__retry_burn_factor()
    
    @retry_burn_factor.setter
    def retry_burn_factor(self, retry_burn_factor):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__retry_burn_factor(retry_burn_factor)
    
    @property
    def retry_burn_max_change(self):
        """
        Element retry_burn_max_change ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 78
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__retry_burn_max_change()
    
    @retry_burn_max_change.setter
    def retry_burn_max_change(self, retry_burn_max_change):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__retry_burn_max_change(retry_burn_max_change)
    
    @property
    def abort_on_failure(self):
        """
        Element abort_on_failure ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 80
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__abort_on_failure()
    
    @abort_on_failure.setter
    def abort_on_failure(self, abort_on_failure):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__abort_on_failure(abort_on_failure)
    
    @property
    def renormalize_abundances(self):
        """
        Element renormalize_abundances ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 82
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__renormalize_abundances()
    
    @renormalize_abundances.setter
    def renormalize_abundances(self, renormalize_abundances):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__renormalize_abundances(renormalize_abundances)
    
    @property
    def small_x_safe(self):
        """
        Element small_x_safe ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 84
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__small_x_safe()
    
    @small_x_safe.setter
    def small_x_safe(self, small_x_safe):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__small_x_safe(small_x_safe)
    
    @property
    def max_temp(self):
        """
        Element max_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 86
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__max_temp()
    
    @max_temp.setter
    def max_temp(self, max_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__max_temp(max_temp)
    
    @property
    def react_boost(self):
        """
        Element react_boost ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 88
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__react_boost()
    
    @react_boost.setter
    def react_boost(self, react_boost):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__react_boost(react_boost)
    
    @property
    def reactions_density_scale(self):
        """
        Element reactions_density_scale ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 90
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__reactions_density_scale()
    
    @reactions_density_scale.setter
    def reactions_density_scale(self, reactions_density_scale):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__reactions_density_scale(reactions_density_scale)
    
    @property
    def reactions_temperature_scale(self):
        """
        Element reactions_temperature_scale ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 92
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__reactions_temperature_scale()
    
    @reactions_temperature_scale.setter
    def reactions_temperature_scale(self, reactions_temperature_scale):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__reactions_temperature_scale(reactions_temperature_scale)
    
    @property
    def reactions_energy_scale(self):
        """
        Element reactions_energy_scale ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 94
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__reactions_energy_scale()
    
    @reactions_energy_scale.setter
    def reactions_energy_scale(self, reactions_energy_scale):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__reactions_energy_scale(reactions_energy_scale)
    
    def __str__(self):
        ret = ['<extern_probin_module>{\n']
        ret.append('    small_temp : ')
        ret.append(repr(self.small_temp))
        ret.append(',\n    small_dens : ')
        ret.append(repr(self.small_dens))
        ret.append(',\n    use_eos_coulomb : ')
        ret.append(repr(self.use_eos_coulomb))
        ret.append(',\n    eos_input_is_constant : ')
        ret.append(repr(self.eos_input_is_constant))
        ret.append(',\n    eos_ttol : ')
        ret.append(repr(self.eos_ttol))
        ret.append(',\n    eos_dtol : ')
        ret.append(repr(self.eos_dtol))
        ret.append(',\n    small_x : ')
        ret.append(repr(self.small_x))
        ret.append(',\n    use_tables : ')
        ret.append(repr(self.use_tables))
        ret.append(',\n    use_c12ag_deboer17 : ')
        ret.append(repr(self.use_c12ag_deboer17))
        ret.append(',\n    disable_thermal_neutrinos : ')
        ret.append(repr(self.disable_thermal_neutrinos))
        ret.append(',\n    use_jacobian_caching : ')
        ret.append(repr(self.use_jacobian_caching))
        ret.append(',\n    do_constant_volume_burn : ')
        ret.append(repr(self.do_constant_volume_burn))
        ret.append(',\n    call_eos_in_rhs : ')
        ret.append(repr(self.call_eos_in_rhs))
        ret.append(',\n    dt_crit : ')
        ret.append(repr(self.dt_crit))
        ret.append(',\n    burning_mode : ')
        ret.append(repr(self.burning_mode))
        ret.append(',\n    burning_mode_factor : ')
        ret.append(repr(self.burning_mode_factor))
        ret.append(',\n    integrate_temperature : ')
        ret.append(repr(self.integrate_temperature))
        ret.append(',\n    integrate_energy : ')
        ret.append(repr(self.integrate_energy))
        ret.append(',\n    jacobian : ')
        ret.append(repr(self.jacobian))
        ret.append(',\n    centered_diff_jac : ')
        ret.append(repr(self.centered_diff_jac))
        ret.append(',\n    burner_verbose : ')
        ret.append(repr(self.burner_verbose))
        ret.append(',\n    rtol_spec : ')
        ret.append(repr(self.rtol_spec))
        ret.append(',\n    rtol_temp : ')
        ret.append(repr(self.rtol_temp))
        ret.append(',\n    rtol_enuc : ')
        ret.append(repr(self.rtol_enuc))
        ret.append(',\n    atol_spec : ')
        ret.append(repr(self.atol_spec))
        ret.append(',\n    atol_temp : ')
        ret.append(repr(self.atol_temp))
        ret.append(',\n    atol_enuc : ')
        ret.append(repr(self.atol_enuc))
        ret.append(',\n    retry_burn : ')
        ret.append(repr(self.retry_burn))
        ret.append(',\n    retry_burn_factor : ')
        ret.append(repr(self.retry_burn_factor))
        ret.append(',\n    retry_burn_max_change : ')
        ret.append(repr(self.retry_burn_max_change))
        ret.append(',\n    abort_on_failure : ')
        ret.append(repr(self.abort_on_failure))
        ret.append(',\n    renormalize_abundances : ')
        ret.append(repr(self.renormalize_abundances))
        ret.append(',\n    small_x_safe : ')
        ret.append(repr(self.small_x_safe))
        ret.append(',\n    max_temp : ')
        ret.append(repr(self.max_temp))
        ret.append(',\n    react_boost : ')
        ret.append(repr(self.react_boost))
        ret.append(',\n    reactions_density_scale : ')
        ret.append(repr(self.reactions_density_scale))
        ret.append(',\n    reactions_temperature_scale : ')
        ret.append(repr(self.reactions_temperature_scale))
        ret.append(',\n    reactions_energy_scale : ')
        ret.append(repr(self.reactions_energy_scale))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

extern_probin_module = Extern_Probin_Module()

class Sneut_Module(f90wrap.runtime.FortranModule):
    """
    Module sneut_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 1-1356
    
    """
    @staticmethod
    def sneut5(temp, den, abar, zbar, snu, dsnudt, dsnudd, dsnuda, dsnudz):
        """
        sneut5(temp, den, abar, zbar, snu, dsnudt, dsnudd, dsnuda, dsnudz)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 8-1187
        
        Parameters
        ----------
        temp : unknown
        den : unknown
        abar : unknown
        zbar : unknown
        snu : unknown
        dsnudt : unknown
        dsnudd : unknown
        dsnuda : unknown
        dsnudz : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_sneut5(temp=temp, den=den, abar=abar, zbar=zbar, \
            snu=snu, dsnudt=dsnudt, dsnudd=dsnudd, dsnuda=dsnuda, dsnudz=dsnudz)
    
    @staticmethod
    def ifermi12(f):
        """
        ifermi12r = ifermi12(f)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 1189-1265
        
        Parameters
        ----------
        f : unknown
        
        Returns
        -------
        ifermi12r : unknown
        
        """
        ifermi12r = _StarKillerMicrophysics.f90wrap_ifermi12(f=f)
        return ifermi12r
    
    @staticmethod
    def zfermim12(x):
        """
        zfermim12r = zfermim12(x)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 1267-1356
        
        Parameters
        ----------
        x : unknown
        
        Returns
        -------
        zfermim12r : unknown
        
        """
        zfermim12r = _StarKillerMicrophysics.f90wrap_zfermim12(x=x)
        return zfermim12r
    
    _dt_array_initialisers = []
    

sneut_module = Sneut_Module()

class Screening_Module(f90wrap.runtime.FortranModule):
    """
    Module screening_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 1-679
    
    """
    class Plasma_State(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=plasma_state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 38-52
        
        """
        def __init__(self, handle=None):
            """
            self = Plasma_State()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 38-52
            
            
            Returns
            -------
            this : Plasma_State
            	Object to be constructed
            
            
            Automatically generated constructor for plasma_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _StarKillerMicrophysics.f90wrap_plasma_state_initialise()
        
        def __del__(self):
            """
            Destructor for class Plasma_State
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 38-52
            
            Parameters
            ----------
            this : Plasma_State
            	Object to be destructed
            
            
            Automatically generated destructor for plasma_state
            """
            if self._alloc:
                _StarKillerMicrophysics.f90wrap_plasma_state_finalise(this=self._handle)
        
        @property
        def qlam0z(self):
            """
            Element qlam0z ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 40
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__qlam0z(self._handle)
        
        @qlam0z.setter
        def qlam0z(self, qlam0z):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__qlam0z(self._handle, qlam0z)
        
        @property
        def qlam0zdt(self):
            """
            Element qlam0zdt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 41
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__qlam0zdt(self._handle)
        
        @qlam0zdt.setter
        def qlam0zdt(self, qlam0zdt):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__qlam0zdt(self._handle, \
                qlam0zdt)
        
        @property
        def qlam0zdd(self):
            """
            Element qlam0zdd ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 42
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__qlam0zdd(self._handle)
        
        @qlam0zdd.setter
        def qlam0zdd(self, qlam0zdd):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__qlam0zdd(self._handle, \
                qlam0zdd)
        
        @property
        def taufac(self):
            """
            Element taufac ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 44
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__taufac(self._handle)
        
        @taufac.setter
        def taufac(self, taufac):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__taufac(self._handle, taufac)
        
        @property
        def taufacdt(self):
            """
            Element taufacdt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 45
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__taufacdt(self._handle)
        
        @taufacdt.setter
        def taufacdt(self, taufacdt):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__taufacdt(self._handle, \
                taufacdt)
        
        @property
        def aa(self):
            """
            Element aa ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 47
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__aa(self._handle)
        
        @aa.setter
        def aa(self, aa):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__aa(self._handle, aa)
        
        @property
        def daadt(self):
            """
            Element daadt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 48
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__daadt(self._handle)
        
        @daadt.setter
        def daadt(self, daadt):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__daadt(self._handle, daadt)
        
        @property
        def daadd(self):
            """
            Element daadd ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 49
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__daadd(self._handle)
        
        @daadd.setter
        def daadd(self, daadd):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__daadd(self._handle, daadd)
        
        def __str__(self):
            ret = ['<plasma_state>{\n']
            ret.append('    qlam0z : ')
            ret.append(repr(self.qlam0z))
            ret.append(',\n    qlam0zdt : ')
            ret.append(repr(self.qlam0zdt))
            ret.append(',\n    qlam0zdd : ')
            ret.append(repr(self.qlam0zdd))
            ret.append(',\n    taufac : ')
            ret.append(repr(self.taufac))
            ret.append(',\n    taufacdt : ')
            ret.append(repr(self.taufacdt))
            ret.append(',\n    aa : ')
            ret.append(repr(self.aa))
            ret.append(',\n    daadt : ')
            ret.append(repr(self.daadt))
            ret.append(',\n    daadd : ')
            ret.append(repr(self.daadd))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    @staticmethod
    def screening_init():
        """
        screening_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 62-91
        
        
        """
        _StarKillerMicrophysics.f90wrap_screening_init()
    
    @staticmethod
    def screening_finalize():
        """
        screening_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 93-139
        
        
        """
        _StarKillerMicrophysics.f90wrap_screening_finalize()
    
    @staticmethod
    def add_screening_factor(z1, a1, z2, a2):
        """
        add_screening_factor(z1, a1, z2, a2)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 141-215
        
        Parameters
        ----------
        z1 : unknown
        a1 : unknown
        z2 : unknown
        a2 : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_add_screening_factor(z1=z1, a1=a1, z2=z2, a2=a2)
    
    @staticmethod
    def fill_plasma_state(state, temp, dens, y):
        """
        fill_plasma_state(state, temp, dens, y)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 217-268
        
        Parameters
        ----------
        state : Plasma_State
        temp : unknown
        dens : unknown
        y : unknown array
        
        """
        _StarKillerMicrophysics.f90wrap_fill_plasma_state(state=state._handle, \
            temp=temp, dens=dens, y=y)
    
    @staticmethod
    def screen5(state, jscreen, scor, scordt, scordd):
        """
        screen5(state, jscreen, scor, scordt, scordd)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 270-491
        
        Parameters
        ----------
        state : Plasma_State
        jscreen : int
        scor : unknown
        scordt : unknown
        scordd : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_screen5(state=state._handle, jscreen=jscreen, \
            scor=scor, scordt=scordt, scordd=scordd)
    
    @staticmethod
    def screenz(t, d, z1, z2, a1, a2, ymass, scfac, dscfacdt):
        """
        screenz(t, d, z1, z2, a1, a2, ymass, scfac, dscfacdt)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 493-679
        
        Parameters
        ----------
        t : unknown
        d : unknown
        z1 : unknown
        z2 : unknown
        a1 : unknown
        a2 : unknown
        ymass : unknown array
        scfac : unknown
        dscfacdt : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_screenz(t=t, d=d, z1=z1, z2=z2, a1=a1, a2=a2, \
            ymass=ymass, scfac=scfac, dscfacdt=dscfacdt)
    
    _dt_array_initialisers = []
    

screening_module = Screening_Module()

class Actual_Conductivity_Module(f90wrap.runtime.FortranModule):
    """
    Module actual_conductivity_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines 1-360
    
    """
    @staticmethod
    def actual_conductivity_init():
        """
        actual_conductivity_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines 9-14
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_conductivity_init()
    
    @staticmethod
    def actual_conductivity(self):
        """
        actual_conductivity(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines \
            16-360
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_actual_conductivity(state=self._handle)
    
    _dt_array_initialisers = []
    

actual_conductivity_module = Actual_Conductivity_Module()

class Starkiller_Initialization_Module(f90wrap.runtime.FortranModule):
    """
    Module starkiller_initialization_module
    
    
    Defined at starkiller_initialization.f90 lines 1-29
    
    """
    @staticmethod
    def starkiller_initialize(probin_file):
        """
        starkiller_initialize(probin_file)
        
        
        Defined at starkiller_initialization.f90 lines 9-29
        
        Parameters
        ----------
        probin_file : str
        
        """
        _StarKillerMicrophysics.f90wrap_starkiller_initialize(probin_file=probin_file)
    
    @property
    def initialized(self):
        """
        Element initialized ftype=logical pytype=bool
        
        
        Defined at starkiller_initialization.f90 line 5
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_starkiller_initialization_module__get__initialized()
    
    @initialized.setter
    def initialized(self, initialized):
        \
            _StarKillerMicrophysics.f90wrap_starkiller_initialization_module__set__initialized(initialized)
    
    def __str__(self):
        ret = ['<starkiller_initialization_module>{\n']
        ret.append('    initialized : ')
        ret.append(repr(self.initialized))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

starkiller_initialization_module = Starkiller_Initialization_Module()

def runtime_init(probin):
    """
    runtime_init(probin)
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 lines 100-223
    
    Parameters
    ----------
    probin : str
    
    """
    _StarKillerMicrophysics.f90wrap_runtime_init(probin=probin)

