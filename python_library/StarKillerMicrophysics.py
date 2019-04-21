import _StarKillerMicrophysics
import f90wrap.runtime
import logging

class Actual_Burner_Module(f90wrap.runtime.FortranModule):
    """
    Module actual_burner_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 14-52
    
    """
    @staticmethod
    def actual_burner(state_in, state_out, dt, time):
        """
        actual_burner(state_in, state_out, dt, time)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 26-42
        
        Parameters
        ----------
        state_in : Burn_T
        state_out : Burn_T
        dt : unknown
        time : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_actual_burner(state_in=state_in._handle, \
            state_out=state_out._handle, dt=dt, time=time)
    
    @staticmethod
    def actual_burner_init():
        """
        actual_burner_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90 lines 44-52
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_burner_init()
    
    _dt_array_initialisers = []
    

actual_burner_module = Actual_Burner_Module()

class Actual_Network(f90wrap.runtime.FortranModule):
    """
    Module actual_network
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 14-339
    
    """
    @staticmethod
    def actual_network_init():
        """
        actual_network_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 145-314
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_network_init()
    
    @staticmethod
    def actual_network_finalize():
        """
        actual_network_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 lines 316-339
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_network_finalize()
    
    @property
    def nspec(self):
        """
        Element nspec ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 20
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nspec()
    
    @property
    def nspec_evolve(self):
        """
        Element nspec_evolve ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 21
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nspec_evolve()
    
    @property
    def naux(self):
        """
        Element naux ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 22
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__naux()
    
    @property
    def ihe4(self):
        """
        Element ihe4 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 24
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ihe4()
    
    @property
    def ic12(self):
        """
        Element ic12 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 25
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ic12()
    
    @property
    def io16(self):
        """
        Element io16 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__io16()
    
    @property
    def ine20(self):
        """
        Element ine20 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 27
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ine20()
    
    @property
    def img24(self):
        """
        Element img24 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 28
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__img24()
    
    @property
    def isi28(self):
        """
        Element isi28 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 29
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__isi28()
    
    @property
    def is32(self):
        """
        Element is32 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__is32()
    
    @property
    def iar36(self):
        """
        Element iar36 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 31
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iar36()
    
    @property
    def ica40(self):
        """
        Element ica40 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 32
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ica40()
    
    @property
    def iti44(self):
        """
        Element iti44 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 33
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iti44()
    
    @property
    def icr48(self):
        """
        Element icr48 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 34
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__icr48()
    
    @property
    def ife52(self):
        """
        Element ife52 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 35
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ife52()
    
    @property
    def ini56(self):
        """
        Element ini56 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 36
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ini56()
    
    @property
    def aion(self):
        """
        Element aion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 38
        
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
        Element zion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 38
        
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
    def nion(self):
        """
        Element nion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 38
        
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
    def bion(self):
        """
        Element bion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 39
        
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
    def mion(self):
        """
        Element mion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 39
        
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
        Element wion ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 39
        
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
    
    @property
    def spec_names(self):
        """
        Element spec_names ftype=character (len=16) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 42
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 43
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 44
        
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
    def network_name(self):
        """
        Element network_name ftype=character (len=32) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 46
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__network_name()
    
    @property
    def avo(self):
        """
        Element avo ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 50
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__avo()
    
    @property
    def c_light(self):
        """
        Element c_light ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 51
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__c_light()
    
    @property
    def ev2erg(self):
        """
        Element ev2erg ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 53
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ev2erg()
    
    @property
    def mev2erg(self):
        """
        Element mev2erg ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 54
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mev2erg()
    
    @property
    def mev2gr(self):
        """
        Element mev2gr ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 55
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mev2gr()
    
    @property
    def mn(self):
        """
        Element mn ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 57
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mn()
    
    @property
    def mp(self):
        """
        Element mp ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 58
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__mp()
    
    @property
    def me(self):
        """
        Element me ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 59
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__me()
    
    @property
    def enuc_conv2(self):
        """
        Element enuc_conv2 ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 63
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__enuc_conv2()
    
    @property
    def nrates(self):
        """
        Element nrates ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 69
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__nrates()
    
    @property
    def num_rate_groups(self):
        """
        Element num_rate_groups ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 70
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__num_rate_groups()
    
    @property
    def ir3a(self):
        """
        Element ir3a ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 72
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ir3a()
    
    @property
    def irg3a(self):
        """
        Element irg3a ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 73
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irg3a()
    
    @property
    def ircag(self):
        """
        Element ircag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 74
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircag()
    
    @property
    def iroga(self):
        """
        Element iroga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 75
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iroga()
    
    @property
    def ir1212(self):
        """
        Element ir1212 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 76
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ir1212()
    
    @property
    def ir1216(self):
        """
        Element ir1216 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 77
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ir1216()
    
    @property
    def ir1616(self):
        """
        Element ir1616 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 78
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ir1616()
    
    @property
    def iroag(self):
        """
        Element iroag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 79
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iroag()
    
    @property
    def irnega(self):
        """
        Element irnega ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 80
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irnega()
    
    @property
    def irneag(self):
        """
        Element irneag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 81
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irneag()
    
    @property
    def irmgga(self):
        """
        Element irmgga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 82
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irmgga()
    
    @property
    def irmgag(self):
        """
        Element irmgag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 83
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irmgag()
    
    @property
    def irsiga(self):
        """
        Element irsiga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 84
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsiga()
    
    @property
    def irmgap(self):
        """
        Element irmgap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 85
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irmgap()
    
    @property
    def iralpa(self):
        """
        Element iralpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 86
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iralpa()
    
    @property
    def iralpg(self):
        """
        Element iralpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 87
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iralpg()
    
    @property
    def irsigp(self):
        """
        Element irsigp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 88
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsigp()
    
    @property
    def irsiag(self):
        """
        Element irsiag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 89
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsiag()
    
    @property
    def irsga(self):
        """
        Element irsga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 90
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsga()
    
    @property
    def irsiap(self):
        """
        Element irsiap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 91
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsiap()
    
    @property
    def irppa(self):
        """
        Element irppa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 92
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irppa()
    
    @property
    def irppg(self):
        """
        Element irppg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 93
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irppg()
    
    @property
    def irsgp(self):
        """
        Element irsgp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 94
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsgp()
    
    @property
    def irsag(self):
        """
        Element irsag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 95
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsag()
    
    @property
    def irarga(self):
        """
        Element irarga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 96
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irarga()
    
    @property
    def irsap(self):
        """
        Element irsap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 97
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irsap()
    
    @property
    def irclpa(self):
        """
        Element irclpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 98
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irclpa()
    
    @property
    def irclpg(self):
        """
        Element irclpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 99
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irclpg()
    
    @property
    def irargp(self):
        """
        Element irargp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 100
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irargp()
    
    @property
    def irarag(self):
        """
        Element irarag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 101
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irarag()
    
    @property
    def ircaga(self):
        """
        Element ircaga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 102
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircaga()
    
    @property
    def irarap(self):
        """
        Element irarap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 103
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irarap()
    
    @property
    def irkpa(self):
        """
        Element irkpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 104
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irkpa()
    
    @property
    def irkpg(self):
        """
        Element irkpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 105
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irkpg()
    
    @property
    def ircagp(self):
        """
        Element ircagp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 106
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircagp()
    
    @property
    def ircaag(self):
        """
        Element ircaag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 107
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircaag()
    
    @property
    def irtiga(self):
        """
        Element irtiga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 108
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irtiga()
    
    @property
    def ircaap(self):
        """
        Element ircaap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 109
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircaap()
    
    @property
    def irscpa(self):
        """
        Element irscpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 110
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irscpa()
    
    @property
    def irscpg(self):
        """
        Element irscpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 111
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irscpg()
    
    @property
    def irtigp(self):
        """
        Element irtigp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 112
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irtigp()
    
    @property
    def irtiag(self):
        """
        Element irtiag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 113
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irtiag()
    
    @property
    def ircrga(self):
        """
        Element ircrga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 114
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircrga()
    
    @property
    def irtiap(self):
        """
        Element irtiap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 115
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irtiap()
    
    @property
    def irvpa(self):
        """
        Element irvpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 116
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irvpa()
    
    @property
    def irvpg(self):
        """
        Element irvpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 117
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irvpg()
    
    @property
    def ircrgp(self):
        """
        Element ircrgp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 118
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircrgp()
    
    @property
    def ircrag(self):
        """
        Element ircrag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 119
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircrag()
    
    @property
    def irfega(self):
        """
        Element irfega ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 120
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irfega()
    
    @property
    def ircrap(self):
        """
        Element ircrap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 121
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircrap()
    
    @property
    def irmnpa(self):
        """
        Element irmnpa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 122
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irmnpa()
    
    @property
    def irmnpg(self):
        """
        Element irmnpg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 123
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irmnpg()
    
    @property
    def irfegp(self):
        """
        Element irfegp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 124
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irfegp()
    
    @property
    def irfeag(self):
        """
        Element irfeag ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 125
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irfeag()
    
    @property
    def irniga(self):
        """
        Element irniga ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 126
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irniga()
    
    @property
    def irfeap(self):
        """
        Element irfeap ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 127
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irfeap()
    
    @property
    def ircopa(self):
        """
        Element ircopa ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 128
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircopa()
    
    @property
    def ircopg(self):
        """
        Element ircopg ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 129
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__ircopg()
    
    @property
    def irnigp(self):
        """
        Element irnigp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 130
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irnigp()
    
    @property
    def irr1(self):
        """
        Element irr1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 131
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irr1()
    
    @property
    def irs1(self):
        """
        Element irs1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 132
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irs1()
    
    @property
    def irt1(self):
        """
        Element irt1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 133
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irt1()
    
    @property
    def iru1(self):
        """
        Element iru1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 134
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iru1()
    
    @property
    def irv1(self):
        """
        Element irv1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 135
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irv1()
    
    @property
    def irw1(self):
        """
        Element irw1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 136
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irw1()
    
    @property
    def irx1(self):
        """
        Element irx1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 137
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__irx1()
    
    @property
    def iry1(self):
        """
        Element iry1 ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 138
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_network__get__iry1()
    
    @property
    def ratenames(self):
        """
        Element ratenames ftype=character (len=16) pytype=str
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_network.F90 line 140
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_network__array__ratenames(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratenames = self._arrays[array_handle]
        else:
            ratenames = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_network__array__ratenames)
            self._arrays[array_handle] = ratenames
        return ratenames
    
    @ratenames.setter
    def ratenames(self, ratenames):
        self.ratenames[...] = ratenames
    
    def __str__(self):
        ret = ['<actual_network>{\n']
        ret.append('    nspec : ')
        ret.append(repr(self.nspec))
        ret.append(',\n    nspec_evolve : ')
        ret.append(repr(self.nspec_evolve))
        ret.append(',\n    naux : ')
        ret.append(repr(self.naux))
        ret.append(',\n    ihe4 : ')
        ret.append(repr(self.ihe4))
        ret.append(',\n    ic12 : ')
        ret.append(repr(self.ic12))
        ret.append(',\n    io16 : ')
        ret.append(repr(self.io16))
        ret.append(',\n    ine20 : ')
        ret.append(repr(self.ine20))
        ret.append(',\n    img24 : ')
        ret.append(repr(self.img24))
        ret.append(',\n    isi28 : ')
        ret.append(repr(self.isi28))
        ret.append(',\n    is32 : ')
        ret.append(repr(self.is32))
        ret.append(',\n    iar36 : ')
        ret.append(repr(self.iar36))
        ret.append(',\n    ica40 : ')
        ret.append(repr(self.ica40))
        ret.append(',\n    iti44 : ')
        ret.append(repr(self.iti44))
        ret.append(',\n    icr48 : ')
        ret.append(repr(self.icr48))
        ret.append(',\n    ife52 : ')
        ret.append(repr(self.ife52))
        ret.append(',\n    ini56 : ')
        ret.append(repr(self.ini56))
        ret.append(',\n    aion : ')
        ret.append(repr(self.aion))
        ret.append(',\n    zion : ')
        ret.append(repr(self.zion))
        ret.append(',\n    nion : ')
        ret.append(repr(self.nion))
        ret.append(',\n    bion : ')
        ret.append(repr(self.bion))
        ret.append(',\n    mion : ')
        ret.append(repr(self.mion))
        ret.append(',\n    wion : ')
        ret.append(repr(self.wion))
        ret.append(',\n    spec_names : ')
        ret.append(repr(self.spec_names))
        ret.append(',\n    short_spec_names : ')
        ret.append(repr(self.short_spec_names))
        ret.append(',\n    short_aux_names : ')
        ret.append(repr(self.short_aux_names))
        ret.append(',\n    network_name : ')
        ret.append(repr(self.network_name))
        ret.append(',\n    avo : ')
        ret.append(repr(self.avo))
        ret.append(',\n    c_light : ')
        ret.append(repr(self.c_light))
        ret.append(',\n    ev2erg : ')
        ret.append(repr(self.ev2erg))
        ret.append(',\n    mev2erg : ')
        ret.append(repr(self.mev2erg))
        ret.append(',\n    mev2gr : ')
        ret.append(repr(self.mev2gr))
        ret.append(',\n    mn : ')
        ret.append(repr(self.mn))
        ret.append(',\n    mp : ')
        ret.append(repr(self.mp))
        ret.append(',\n    me : ')
        ret.append(repr(self.me))
        ret.append(',\n    enuc_conv2 : ')
        ret.append(repr(self.enuc_conv2))
        ret.append(',\n    nrates : ')
        ret.append(repr(self.nrates))
        ret.append(',\n    num_rate_groups : ')
        ret.append(repr(self.num_rate_groups))
        ret.append(',\n    ir3a : ')
        ret.append(repr(self.ir3a))
        ret.append(',\n    irg3a : ')
        ret.append(repr(self.irg3a))
        ret.append(',\n    ircag : ')
        ret.append(repr(self.ircag))
        ret.append(',\n    iroga : ')
        ret.append(repr(self.iroga))
        ret.append(',\n    ir1212 : ')
        ret.append(repr(self.ir1212))
        ret.append(',\n    ir1216 : ')
        ret.append(repr(self.ir1216))
        ret.append(',\n    ir1616 : ')
        ret.append(repr(self.ir1616))
        ret.append(',\n    iroag : ')
        ret.append(repr(self.iroag))
        ret.append(',\n    irnega : ')
        ret.append(repr(self.irnega))
        ret.append(',\n    irneag : ')
        ret.append(repr(self.irneag))
        ret.append(',\n    irmgga : ')
        ret.append(repr(self.irmgga))
        ret.append(',\n    irmgag : ')
        ret.append(repr(self.irmgag))
        ret.append(',\n    irsiga : ')
        ret.append(repr(self.irsiga))
        ret.append(',\n    irmgap : ')
        ret.append(repr(self.irmgap))
        ret.append(',\n    iralpa : ')
        ret.append(repr(self.iralpa))
        ret.append(',\n    iralpg : ')
        ret.append(repr(self.iralpg))
        ret.append(',\n    irsigp : ')
        ret.append(repr(self.irsigp))
        ret.append(',\n    irsiag : ')
        ret.append(repr(self.irsiag))
        ret.append(',\n    irsga : ')
        ret.append(repr(self.irsga))
        ret.append(',\n    irsiap : ')
        ret.append(repr(self.irsiap))
        ret.append(',\n    irppa : ')
        ret.append(repr(self.irppa))
        ret.append(',\n    irppg : ')
        ret.append(repr(self.irppg))
        ret.append(',\n    irsgp : ')
        ret.append(repr(self.irsgp))
        ret.append(',\n    irsag : ')
        ret.append(repr(self.irsag))
        ret.append(',\n    irarga : ')
        ret.append(repr(self.irarga))
        ret.append(',\n    irsap : ')
        ret.append(repr(self.irsap))
        ret.append(',\n    irclpa : ')
        ret.append(repr(self.irclpa))
        ret.append(',\n    irclpg : ')
        ret.append(repr(self.irclpg))
        ret.append(',\n    irargp : ')
        ret.append(repr(self.irargp))
        ret.append(',\n    irarag : ')
        ret.append(repr(self.irarag))
        ret.append(',\n    ircaga : ')
        ret.append(repr(self.ircaga))
        ret.append(',\n    irarap : ')
        ret.append(repr(self.irarap))
        ret.append(',\n    irkpa : ')
        ret.append(repr(self.irkpa))
        ret.append(',\n    irkpg : ')
        ret.append(repr(self.irkpg))
        ret.append(',\n    ircagp : ')
        ret.append(repr(self.ircagp))
        ret.append(',\n    ircaag : ')
        ret.append(repr(self.ircaag))
        ret.append(',\n    irtiga : ')
        ret.append(repr(self.irtiga))
        ret.append(',\n    ircaap : ')
        ret.append(repr(self.ircaap))
        ret.append(',\n    irscpa : ')
        ret.append(repr(self.irscpa))
        ret.append(',\n    irscpg : ')
        ret.append(repr(self.irscpg))
        ret.append(',\n    irtigp : ')
        ret.append(repr(self.irtigp))
        ret.append(',\n    irtiag : ')
        ret.append(repr(self.irtiag))
        ret.append(',\n    ircrga : ')
        ret.append(repr(self.ircrga))
        ret.append(',\n    irtiap : ')
        ret.append(repr(self.irtiap))
        ret.append(',\n    irvpa : ')
        ret.append(repr(self.irvpa))
        ret.append(',\n    irvpg : ')
        ret.append(repr(self.irvpg))
        ret.append(',\n    ircrgp : ')
        ret.append(repr(self.ircrgp))
        ret.append(',\n    ircrag : ')
        ret.append(repr(self.ircrag))
        ret.append(',\n    irfega : ')
        ret.append(repr(self.irfega))
        ret.append(',\n    ircrap : ')
        ret.append(repr(self.ircrap))
        ret.append(',\n    irmnpa : ')
        ret.append(repr(self.irmnpa))
        ret.append(',\n    irmnpg : ')
        ret.append(repr(self.irmnpg))
        ret.append(',\n    irfegp : ')
        ret.append(repr(self.irfegp))
        ret.append(',\n    irfeag : ')
        ret.append(repr(self.irfeag))
        ret.append(',\n    irniga : ')
        ret.append(repr(self.irniga))
        ret.append(',\n    irfeap : ')
        ret.append(repr(self.irfeap))
        ret.append(',\n    ircopa : ')
        ret.append(repr(self.ircopa))
        ret.append(',\n    ircopg : ')
        ret.append(repr(self.ircopg))
        ret.append(',\n    irnigp : ')
        ret.append(repr(self.irnigp))
        ret.append(',\n    irr1 : ')
        ret.append(repr(self.irr1))
        ret.append(',\n    irs1 : ')
        ret.append(repr(self.irs1))
        ret.append(',\n    irt1 : ')
        ret.append(repr(self.irt1))
        ret.append(',\n    iru1 : ')
        ret.append(repr(self.iru1))
        ret.append(',\n    irv1 : ')
        ret.append(repr(self.irv1))
        ret.append(',\n    irw1 : ')
        ret.append(repr(self.irw1))
        ret.append(',\n    irx1 : ')
        ret.append(repr(self.irx1))
        ret.append(',\n    iry1 : ')
        ret.append(repr(self.iry1))
        ret.append(',\n    ratenames : ')
        ret.append(repr(self.ratenames))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

actual_network = Actual_Network()

class Actual_Rhs_Module(f90wrap.runtime.FortranModule):
    """
    Module actual_rhs_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 14-2298
    
    """
    @staticmethod
    def actual_rhs_init():
        """
        actual_rhs_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 44-73
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_rhs_init()
    
    @staticmethod
    def actual_rhs(state):
        """
        actual_rhs(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 75-140
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_actual_rhs(state=state._handle)
    
    @staticmethod
    def actual_jac(state):
        """
        actual_jac(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 144-228
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_actual_jac(state=state._handle)
    
    @staticmethod
    def create_rates_table():
        """
        create_rates_table()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 409-426
        
        
        """
        _StarKillerMicrophysics.f90wrap_create_rates_table()
    
    @staticmethod
    def set_aprox13rat():
        """
        set_aprox13rat()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 428-455
        
        
        """
        _StarKillerMicrophysics.f90wrap_set_aprox13rat()
    
    @staticmethod
    def ener_gener_rate(dydt, enuc):
        """
        ener_gener_rate(dydt, enuc)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 2209-2225
        
        Parameters
        ----------
        dydt : unknown array
        enuc : unknown
        
        """
        _StarKillerMicrophysics.f90wrap_ener_gener_rate(dydt=dydt, enuc=enuc)
    
    @staticmethod
    def set_up_screening_factors():
        """
        set_up_screening_factors()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 2229-2288
        
        
        """
        _StarKillerMicrophysics.f90wrap_set_up_screening_factors()
    
    @staticmethod
    def update_unevolved_species(state):
        """
        update_unevolved_species(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 lines 2290-2298
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_update_unevolved_species(state=state._handle)
    
    @property
    def tab_tlo(self):
        """
        Element tab_tlo ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__tab_tlo()
    
    @property
    def tab_thi(self):
        """
        Element tab_thi ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__tab_thi()
    
    @property
    def tab_per_decade(self):
        """
        Element tab_per_decade ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 27
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__tab_per_decade()
    
    @property
    def nrattab(self):
        """
        Element nrattab ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 28
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__nrattab()
    
    @property
    def tab_imax(self):
        """
        Element tab_imax ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 29
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__tab_imax()
    
    @property
    def tab_tstp(self):
        """
        Element tab_tstp ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_actual_rhs_module__get__tab_tstp()
    
    @property
    def rattab(self):
        """
        Element rattab ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 32
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__rattab(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rattab = self._arrays[array_handle]
        else:
            rattab = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__rattab)
            self._arrays[array_handle] = rattab
        return rattab
    
    @rattab.setter
    def rattab(self, rattab):
        self.rattab[...] = rattab
    
    @property
    def drattabdt(self):
        """
        Element drattabdt ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 33
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__drattabdt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            drattabdt = self._arrays[array_handle]
        else:
            drattabdt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__drattabdt)
            self._arrays[array_handle] = drattabdt
        return drattabdt
    
    @drattabdt.setter
    def drattabdt(self, drattabdt):
        self.drattabdt[...] = drattabdt
    
    @property
    def ttab(self):
        """
        Element ttab ftype=double precision pytype=unknown
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_rhs.F90 line 35
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__ttab(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ttab = self._arrays[array_handle]
        else:
            ttab = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _StarKillerMicrophysics.f90wrap_actual_rhs_module__array__ttab)
            self._arrays[array_handle] = ttab
        return ttab
    
    @ttab.setter
    def ttab(self, ttab):
        self.ttab[...] = ttab
    
    def __str__(self):
        ret = ['<actual_rhs_module>{\n']
        ret.append('    tab_tlo : ')
        ret.append(repr(self.tab_tlo))
        ret.append(',\n    tab_thi : ')
        ret.append(repr(self.tab_thi))
        ret.append(',\n    tab_per_decade : ')
        ret.append(repr(self.tab_per_decade))
        ret.append(',\n    nrattab : ')
        ret.append(repr(self.nrattab))
        ret.append(',\n    tab_imax : ')
        ret.append(repr(self.tab_imax))
        ret.append(',\n    tab_tstp : ')
        ret.append(repr(self.tab_tstp))
        ret.append(',\n    rattab : ')
        ret.append(repr(self.rattab))
        ret.append(',\n    drattabdt : ')
        ret.append(repr(self.drattabdt))
        ret.append(',\n    ttab : ')
        ret.append(repr(self.ttab))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

actual_rhs_module = Actual_Rhs_Module()

class Burn_Type_Module(f90wrap.runtime.FortranModule):
    """
    Module burn_type_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 14-225
    
    """
    class Burn_T(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=burn_t)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 35-90
        
        """
        def __init__(self, handle=None):
            """
            self = Burn_T()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 35-90
            
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 35-90
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 37
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__rho(self._handle)
        
        @rho.setter
        def rho(self, rho):
            _StarKillerMicrophysics.f90wrap_burn_t__set__rho(self._handle, rho)
        
        @property
        def t(self):
            """
            Element t ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 38
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__t(self._handle)
        
        @t.setter
        def t(self, t):
            _StarKillerMicrophysics.f90wrap_burn_t__set__t(self._handle, t)
        
        @property
        def e(self):
            """
            Element e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 39
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__e(self._handle)
        
        @e.setter
        def e(self, e):
            _StarKillerMicrophysics.f90wrap_burn_t__set__e(self._handle, e)
        
        @property
        def xn(self):
            """
            Element xn ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 40
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 42
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cv(self._handle)
        
        @cv.setter
        def cv(self, cv):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cv(self._handle, cv)
        
        @property
        def cp(self):
            """
            Element cp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 43
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cp(self._handle)
        
        @cp.setter
        def cp(self, cp):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cp(self._handle, cp)
        
        @property
        def y_e(self):
            """
            Element y_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 44
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__y_e(self._handle)
        
        @y_e.setter
        def y_e(self, y_e):
            _StarKillerMicrophysics.f90wrap_burn_t__set__y_e(self._handle, y_e)
        
        @property
        def eta(self):
            """
            Element eta ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 45
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__eta(self._handle)
        
        @eta.setter
        def eta(self, eta):
            _StarKillerMicrophysics.f90wrap_burn_t__set__eta(self._handle, eta)
        
        @property
        def cs(self):
            """
            Element cs ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 46
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__cs(self._handle)
        
        @cs.setter
        def cs(self, cs):
            _StarKillerMicrophysics.f90wrap_burn_t__set__cs(self._handle, cs)
        
        @property
        def dx(self):
            """
            Element dx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 47
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dx(self._handle)
        
        @dx.setter
        def dx(self, dx):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dx(self._handle, dx)
        
        @property
        def abar(self):
            """
            Element abar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 48
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__abar(self._handle)
        
        @abar.setter
        def abar(self, abar):
            _StarKillerMicrophysics.f90wrap_burn_t__set__abar(self._handle, abar)
        
        @property
        def zbar(self):
            """
            Element zbar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 49
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__zbar(self._handle)
        
        @zbar.setter
        def zbar(self, zbar):
            _StarKillerMicrophysics.f90wrap_burn_t__set__zbar(self._handle, zbar)
        
        @property
        def t_old(self):
            """
            Element t_old ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 52
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__t_old(self._handle)
        
        @t_old.setter
        def t_old(self, t_old):
            _StarKillerMicrophysics.f90wrap_burn_t__set__t_old(self._handle, t_old)
        
        @property
        def dcvdt(self):
            """
            Element dcvdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 55
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dcvdt(self._handle)
        
        @dcvdt.setter
        def dcvdt(self, dcvdt):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dcvdt(self._handle, dcvdt)
        
        @property
        def dcpdt(self):
            """
            Element dcpdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 56
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__dcpdt(self._handle)
        
        @dcpdt.setter
        def dcpdt(self, dcpdt):
            _StarKillerMicrophysics.f90wrap_burn_t__set__dcpdt(self._handle, dcpdt)
        
        @property
        def ydot(self):
            """
            Element ydot ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 64
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 66
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 70
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__self_heat(self._handle)
        
        @self_heat.setter
        def self_heat(self, self_heat):
            _StarKillerMicrophysics.f90wrap_burn_t__set__self_heat(self._handle, self_heat)
        
        @property
        def i(self):
            """
            Element i ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 74
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__i(self._handle)
        
        @i.setter
        def i(self, i):
            _StarKillerMicrophysics.f90wrap_burn_t__set__i(self._handle, i)
        
        @property
        def j(self):
            """
            Element j ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 75
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__j(self._handle)
        
        @j.setter
        def j(self, j):
            _StarKillerMicrophysics.f90wrap_burn_t__set__j(self._handle, j)
        
        @property
        def k(self):
            """
            Element k ftype=integer           pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 76
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__k(self._handle)
        
        @k.setter
        def k(self, k):
            _StarKillerMicrophysics.f90wrap_burn_t__set__k(self._handle, k)
        
        @property
        def n_rhs(self):
            """
            Element n_rhs ftype=integer  pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 79
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__n_rhs(self._handle)
        
        @n_rhs.setter
        def n_rhs(self, n_rhs):
            _StarKillerMicrophysics.f90wrap_burn_t__set__n_rhs(self._handle, n_rhs)
        
        @property
        def n_jac(self):
            """
            Element n_jac ftype=integer  pytype=int
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 80
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__n_jac(self._handle)
        
        @n_jac.setter
        def n_jac(self, n_jac):
            _StarKillerMicrophysics.f90wrap_burn_t__set__n_jac(self._handle, n_jac)
        
        @property
        def time(self):
            """
            Element time ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 84
            
            """
            return _StarKillerMicrophysics.f90wrap_burn_t__get__time(self._handle)
        
        @time.setter
        def time(self, time):
            _StarKillerMicrophysics.f90wrap_burn_t__set__time(self._handle, time)
        
        @property
        def success(self):
            """
            Element success ftype=logical pytype=bool
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 88
            
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 96-146
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 150-177
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 181-207
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 lines 209-225
        
        Parameters
        ----------
        state : Burn_T
        
        """
        _StarKillerMicrophysics.f90wrap_normalize_abundances_burn(state=state._handle)
    
    @property
    def neqs(self):
        """
        Element neqs ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 28
        
        """
        return _StarKillerMicrophysics.f90wrap_burn_type_module__get__neqs()
    
    @property
    def net_itemp(self):
        """
        Element net_itemp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 32
        
        """
        return _StarKillerMicrophysics.f90wrap_burn_type_module__get__net_itemp()
    
    @property
    def net_ienuc(self):
        """
        Element net_ienuc ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-burn_type.F90 line 33
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 14-495
    
    """
    class Eos_T(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=eos_t)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 122-170
        
        """
        def __init__(self, handle=None):
            """
            self = Eos_T()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 122-170
            
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 122-170
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 124
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__rho(self._handle)
        
        @rho.setter
        def rho(self, rho):
            _StarKillerMicrophysics.f90wrap_eos_t__set__rho(self._handle, rho)
        
        @property
        def t(self):
            """
            Element t ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 125
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__t(self._handle)
        
        @t.setter
        def t(self, t):
            _StarKillerMicrophysics.f90wrap_eos_t__set__t(self._handle, t)
        
        @property
        def p(self):
            """
            Element p ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 126
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__p(self._handle)
        
        @p.setter
        def p(self, p):
            _StarKillerMicrophysics.f90wrap_eos_t__set__p(self._handle, p)
        
        @property
        def e(self):
            """
            Element e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 127
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__e(self._handle)
        
        @e.setter
        def e(self, e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__e(self._handle, e)
        
        @property
        def h(self):
            """
            Element h ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 128
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__h(self._handle)
        
        @h.setter
        def h(self, h):
            _StarKillerMicrophysics.f90wrap_eos_t__set__h(self._handle, h)
        
        @property
        def s(self):
            """
            Element s ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 129
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__s(self._handle)
        
        @s.setter
        def s(self, s):
            _StarKillerMicrophysics.f90wrap_eos_t__set__s(self._handle, s)
        
        @property
        def xn(self):
            """
            Element xn ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 130
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 131
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 133
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdt(self._handle)
        
        @dpdt.setter
        def dpdt(self, dpdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdt(self._handle, dpdt)
        
        @property
        def dpdr(self):
            """
            Element dpdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 134
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdr(self._handle)
        
        @dpdr.setter
        def dpdr(self, dpdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdr(self._handle, dpdr)
        
        @property
        def dedt(self):
            """
            Element dedt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 135
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedt(self._handle)
        
        @dedt.setter
        def dedt(self, dedt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedt(self._handle, dedt)
        
        @property
        def dedr(self):
            """
            Element dedr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 136
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedr(self._handle)
        
        @dedr.setter
        def dedr(self, dedr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedr(self._handle, dedr)
        
        @property
        def dhdt(self):
            """
            Element dhdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 137
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dhdt(self._handle)
        
        @dhdt.setter
        def dhdt(self, dhdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dhdt(self._handle, dhdt)
        
        @property
        def dhdr(self):
            """
            Element dhdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 138
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dhdr(self._handle)
        
        @dhdr.setter
        def dhdr(self, dhdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dhdr(self._handle, dhdr)
        
        @property
        def dsdt(self):
            """
            Element dsdt ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 139
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dsdt(self._handle)
        
        @dsdt.setter
        def dsdt(self, dsdt):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dsdt(self._handle, dsdt)
        
        @property
        def dsdr(self):
            """
            Element dsdr ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 140
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dsdr(self._handle)
        
        @dsdr.setter
        def dsdr(self, dsdr):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dsdr(self._handle, dsdr)
        
        @property
        def dpde(self):
            """
            Element dpde ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 141
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpde(self._handle)
        
        @dpde.setter
        def dpde(self, dpde):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpde(self._handle, dpde)
        
        @property
        def dpdr_e(self):
            """
            Element dpdr_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 142
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdr_e(self._handle)
        
        @dpdr_e.setter
        def dpdr_e(self, dpdr_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdr_e(self._handle, dpdr_e)
        
        @property
        def cv(self):
            """
            Element cv ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 144
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cv(self._handle)
        
        @cv.setter
        def cv(self, cv):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cv(self._handle, cv)
        
        @property
        def cp(self):
            """
            Element cp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 145
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cp(self._handle)
        
        @cp.setter
        def cp(self, cp):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cp(self._handle, cp)
        
        @property
        def xne(self):
            """
            Element xne ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 146
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__xne(self._handle)
        
        @xne.setter
        def xne(self, xne):
            _StarKillerMicrophysics.f90wrap_eos_t__set__xne(self._handle, xne)
        
        @property
        def xnp(self):
            """
            Element xnp ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 147
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__xnp(self._handle)
        
        @xnp.setter
        def xnp(self, xnp):
            _StarKillerMicrophysics.f90wrap_eos_t__set__xnp(self._handle, xnp)
        
        @property
        def eta(self):
            """
            Element eta ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 148
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__eta(self._handle)
        
        @eta.setter
        def eta(self, eta):
            _StarKillerMicrophysics.f90wrap_eos_t__set__eta(self._handle, eta)
        
        @property
        def pele(self):
            """
            Element pele ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 149
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__pele(self._handle)
        
        @pele.setter
        def pele(self, pele):
            _StarKillerMicrophysics.f90wrap_eos_t__set__pele(self._handle, pele)
        
        @property
        def ppos(self):
            """
            Element ppos ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 150
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__ppos(self._handle)
        
        @ppos.setter
        def ppos(self, ppos):
            _StarKillerMicrophysics.f90wrap_eos_t__set__ppos(self._handle, ppos)
        
        @property
        def mu(self):
            """
            Element mu ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 151
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__mu(self._handle)
        
        @mu.setter
        def mu(self, mu):
            _StarKillerMicrophysics.f90wrap_eos_t__set__mu(self._handle, mu)
        
        @property
        def mu_e(self):
            """
            Element mu_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 152
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__mu_e(self._handle)
        
        @mu_e.setter
        def mu_e(self, mu_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__mu_e(self._handle, mu_e)
        
        @property
        def y_e(self):
            """
            Element y_e ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 153
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__y_e(self._handle)
        
        @y_e.setter
        def y_e(self, y_e):
            _StarKillerMicrophysics.f90wrap_eos_t__set__y_e(self._handle, y_e)
        
        @property
        def dedx(self):
            """
            Element dedx ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 154
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 155
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 156
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 157
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__gam1(self._handle)
        
        @gam1.setter
        def gam1(self, gam1):
            _StarKillerMicrophysics.f90wrap_eos_t__set__gam1(self._handle, gam1)
        
        @property
        def cs(self):
            """
            Element cs ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 158
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__cs(self._handle)
        
        @cs.setter
        def cs(self, cs):
            _StarKillerMicrophysics.f90wrap_eos_t__set__cs(self._handle, cs)
        
        @property
        def abar(self):
            """
            Element abar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 160
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__abar(self._handle)
        
        @abar.setter
        def abar(self, abar):
            _StarKillerMicrophysics.f90wrap_eos_t__set__abar(self._handle, abar)
        
        @property
        def zbar(self):
            """
            Element zbar ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 161
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__zbar(self._handle)
        
        @zbar.setter
        def zbar(self, zbar):
            _StarKillerMicrophysics.f90wrap_eos_t__set__zbar(self._handle, zbar)
        
        @property
        def dpda(self):
            """
            Element dpda ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 163
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpda(self._handle)
        
        @dpda.setter
        def dpda(self, dpda):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpda(self._handle, dpda)
        
        @property
        def dpdz(self):
            """
            Element dpdz ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 164
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dpdz(self._handle)
        
        @dpdz.setter
        def dpdz(self, dpdz):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dpdz(self._handle, dpdz)
        
        @property
        def deda(self):
            """
            Element deda ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 165
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__deda(self._handle)
        
        @deda.setter
        def deda(self, deda):
            _StarKillerMicrophysics.f90wrap_eos_t__set__deda(self._handle, deda)
        
        @property
        def dedz(self):
            """
            Element dedz ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 166
            
            """
            return _StarKillerMicrophysics.f90wrap_eos_t__get__dedz(self._handle)
        
        @dedz.setter
        def dedz(self, dedz):
            _StarKillerMicrophysics.f90wrap_eos_t__set__dedz(self._handle, dedz)
        
        @property
        def conductivity(self):
            """
            Element conductivity ftype=real(rt) pytype=float
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 168
            
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 176-233
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 238-263
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_composition(state=state._handle)
    
    @staticmethod
    def composition_derivatives(state):
        """
        composition_derivatives(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 267-297
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_composition_derivatives(state=state._handle)
    
    @staticmethod
    def normalize_abundances(state):
        """
        normalize_abundances(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 302-318
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_normalize_abundances(state=state._handle)
    
    @staticmethod
    def clean_state(state):
        """
        clean_state(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 322-335
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_clean_state(state=state._handle)
    
    @staticmethod
    def print_state(state):
        """
        print_state(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 339-351
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_print_state(state=state._handle)
    
    @staticmethod
    def eos_get_small_temp():
        """
        small_temp_out = eos_get_small_temp()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 353-367
        
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 369-383
        
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 385-399
        
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 401-414
        
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 lines 418-495
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 24
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rt()
    
    @property
    def eos_input_rh(self):
        """
        Element eos_input_rh ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 25
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rh()
    
    @property
    def eos_input_tp(self):
        """
        Element eos_input_tp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 26
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_tp()
    
    @property
    def eos_input_rp(self):
        """
        Element eos_input_rp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 27
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_rp()
    
    @property
    def eos_input_re(self):
        """
        Element eos_input_re ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 28
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_re()
    
    @property
    def eos_input_ps(self):
        """
        Element eos_input_ps ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 29
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_ps()
    
    @property
    def eos_input_ph(self):
        """
        Element eos_input_ph ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 30
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_ph()
    
    @property
    def eos_input_th(self):
        """
        Element eos_input_th ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 31
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__eos_input_th()
    
    @property
    def itemp(self):
        """
        Element itemp ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 35
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__itemp()
    
    @property
    def idens(self):
        """
        Element idens ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 36
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__idens()
    
    @property
    def iener(self):
        """
        Element iener ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 37
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__iener()
    
    @property
    def ienth(self):
        """
        Element ienth ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 38
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ienth()
    
    @property
    def ientr(self):
        """
        Element ientr ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 39
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ientr()
    
    @property
    def ipres(self):
        """
        Element ipres ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 40
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ipres()
    
    @property
    def ierr_general(self):
        """
        Element ierr_general ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 43
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_general()
    
    @property
    def ierr_input(self):
        """
        Element ierr_input ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 44
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_input()
    
    @property
    def ierr_iter_conv(self):
        """
        Element ierr_iter_conv ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 45
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_iter_conv()
    
    @property
    def ierr_neg_e(self):
        """
        Element ierr_neg_e ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 46
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_e()
    
    @property
    def ierr_neg_p(self):
        """
        Element ierr_neg_p ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 47
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_p()
    
    @property
    def ierr_neg_h(self):
        """
        Element ierr_neg_h ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 48
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_h()
    
    @property
    def ierr_neg_s(self):
        """
        Element ierr_neg_s ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 49
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_neg_s()
    
    @property
    def ierr_iter_var(self):
        """
        Element ierr_iter_var ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 50
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_iter_var()
    
    @property
    def ierr_init(self):
        """
        Element ierr_init ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 51
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_init()
    
    @property
    def ierr_init_xn(self):
        """
        Element ierr_init_xn ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 52
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_init_xn()
    
    @property
    def ierr_out_of_bounds(self):
        """
        Element ierr_out_of_bounds ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 53
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_out_of_bounds()
    
    @property
    def ierr_not_implemented(self):
        """
        Element ierr_not_implemented ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 54
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_eos_type_module__get__ierr_not_implemented()
    
    @property
    def mintemp(self):
        """
        Element mintemp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 58
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mintemp()
    
    @mintemp.setter
    def mintemp(self, mintemp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mintemp(mintemp)
    
    @property
    def maxtemp(self):
        """
        Element maxtemp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 59
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxtemp()
    
    @maxtemp.setter
    def maxtemp(self, maxtemp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxtemp(maxtemp)
    
    @property
    def mindens(self):
        """
        Element mindens ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 60
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mindens()
    
    @mindens.setter
    def mindens(self, mindens):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mindens(mindens)
    
    @property
    def maxdens(self):
        """
        Element maxdens ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 61
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxdens()
    
    @maxdens.setter
    def maxdens(self, maxdens):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxdens(maxdens)
    
    @property
    def minx(self):
        """
        Element minx ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 62
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minx()
    
    @minx.setter
    def minx(self, minx):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minx(minx)
    
    @property
    def maxx(self):
        """
        Element maxx ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 63
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxx()
    
    @maxx.setter
    def maxx(self, maxx):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxx(maxx)
    
    @property
    def minye(self):
        """
        Element minye ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 64
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minye()
    
    @minye.setter
    def minye(self, minye):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minye(minye)
    
    @property
    def maxye(self):
        """
        Element maxye ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 65
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxye()
    
    @maxye.setter
    def maxye(self, maxye):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxye(maxye)
    
    @property
    def mine(self):
        """
        Element mine ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 66
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mine()
    
    @mine.setter
    def mine(self, mine):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mine(mine)
    
    @property
    def maxe(self):
        """
        Element maxe ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 67
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxe()
    
    @maxe.setter
    def maxe(self, maxe):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxe(maxe)
    
    @property
    def minp(self):
        """
        Element minp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 68
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minp()
    
    @minp.setter
    def minp(self, minp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minp(minp)
    
    @property
    def maxp(self):
        """
        Element maxp ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 69
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxp()
    
    @maxp.setter
    def maxp(self, maxp):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxp(maxp)
    
    @property
    def mins(self):
        """
        Element mins ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 70
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__mins()
    
    @mins.setter
    def mins(self, mins):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__mins(mins)
    
    @property
    def maxs(self):
        """
        Element maxs ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 71
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__maxs()
    
    @maxs.setter
    def maxs(self, maxs):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__maxs(maxs)
    
    @property
    def minh(self):
        """
        Element minh ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 72
        
        """
        return _StarKillerMicrophysics.f90wrap_eos_type_module__get__minh()
    
    @minh.setter
    def minh(self, minh):
        _StarKillerMicrophysics.f90wrap_eos_type_module__set__minh(minh)
    
    @property
    def maxh(self):
        """
        Element maxh ftype=real(rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos_type.F90 line 73
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 14-609
    
    """
    @staticmethod
    def eos_init(small_temp=None, small_dens=None):
        """
        eos_init([small_temp, small_dens])
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 27-120
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 122-131
        
        
        """
        _StarKillerMicrophysics.f90wrap_eos_finalize()
    
    @staticmethod
    def eos(input, state):
        """
        eos(input, state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 133-185
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 187-250
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 254-271
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 275-292
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 294-313
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 315-334
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 336-355
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 357-376
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 381-404
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 406-485
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 487-506
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_rho(state=state._handle)
    
    @staticmethod
    def check_t(state):
        """
        check_t(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 508-527
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_t(state=state._handle)
    
    @staticmethod
    def check_e(state):
        """
        check_e(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 529-548
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_e(state=state._handle)
    
    @staticmethod
    def check_h(state):
        """
        check_h(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 550-569
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_h(state=state._handle)
    
    @staticmethod
    def check_s(state):
        """
        check_s(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 571-590
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_s(state=state._handle)
    
    @staticmethod
    def check_p(state):
        """
        check_p(state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 lines 592-609
        
        Parameters
        ----------
        state : Eos_T
        
        """
        _StarKillerMicrophysics.f90wrap_check_p(state=state._handle)
    
    @property
    def initialized(self):
        """
        Element initialized ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-eos.F90 line 20
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 35-142
    
    """
    @staticmethod
    def network_init():
        """
        network_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 52-86
        
        
        """
        _StarKillerMicrophysics.f90wrap_network_init()
    
    @staticmethod
    def network_species_index(name):
        """
        r = network_species_index(name)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 88-103
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 105-117
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 119-131
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 lines 133-142
        
        
        """
        _StarKillerMicrophysics.f90wrap_network_finalize()
    
    @property
    def network_initialized(self):
        """
        Element network_initialized ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 line 42
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-network.F90 line 45
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 14-58
    
    """
    @staticmethod
    def microphysics_init(small_temp=None, small_dens=None):
        """
        microphysics_init([small_temp, small_dens])
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 28-50
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-microphysics.F90 lines 52-58
        
        
        """
        _StarKillerMicrophysics.f90wrap_microphysics_finalize()
    
    _dt_array_initialisers = []
    

microphysics_module = Microphysics_Module()

class Extern_Probin_Module(f90wrap.runtime.FortranModule):
    """
    Module extern_probin_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 lines 25-111
    
    """
    @property
    def small_temp(self):
        """
        Element small_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 33
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 35
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 37
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 39
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 41
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__eos_ttol()
    
    @eos_ttol.setter
    def eos_ttol(self, eos_ttol):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__eos_ttol(eos_ttol)
    
    @property
    def eos_dtol(self):
        """
        Element eos_dtol ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 43
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__eos_dtol()
    
    @eos_dtol.setter
    def eos_dtol(self, eos_dtol):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__eos_dtol(eos_dtol)
    
    @property
    def small_x(self):
        """
        Element small_x ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 45
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__small_x()
    
    @small_x.setter
    def small_x(self, small_x):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__small_x(small_x)
    
    @property
    def use_tables(self):
        """
        Element use_tables ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 47
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 49
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_c12ag_deboer17()
    
    @use_c12ag_deboer17.setter
    def use_c12ag_deboer17(self, use_c12ag_deboer17):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_c12ag_deboer17(use_c12ag_deboer17)
    
    @property
    def do_constant_volume_burn(self):
        """
        Element do_constant_volume_burn ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 51
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 53
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 55
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__dt_crit()
    
    @dt_crit.setter
    def dt_crit(self, dt_crit):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__dt_crit(dt_crit)
    
    @property
    def burning_mode(self):
        """
        Element burning_mode ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 57
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 59
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 61
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 63
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 65
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__jacobian()
    
    @jacobian.setter
    def jacobian(self, jacobian):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__jacobian(jacobian)
    
    @property
    def centered_diff_jac(self):
        """
        Element centered_diff_jac ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 67
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 69
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 71
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_spec()
    
    @rtol_spec.setter
    def rtol_spec(self, rtol_spec):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_spec(rtol_spec)
    
    @property
    def rtol_temp(self):
        """
        Element rtol_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 73
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_temp()
    
    @rtol_temp.setter
    def rtol_temp(self, rtol_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_temp(rtol_temp)
    
    @property
    def rtol_enuc(self):
        """
        Element rtol_enuc ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 75
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__rtol_enuc()
    
    @rtol_enuc.setter
    def rtol_enuc(self, rtol_enuc):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__rtol_enuc(rtol_enuc)
    
    @property
    def atol_spec(self):
        """
        Element atol_spec ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 77
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_spec()
    
    @atol_spec.setter
    def atol_spec(self, atol_spec):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_spec(atol_spec)
    
    @property
    def atol_temp(self):
        """
        Element atol_temp ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 79
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_temp()
    
    @atol_temp.setter
    def atol_temp(self, atol_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_temp(atol_temp)
    
    @property
    def atol_enuc(self):
        """
        Element atol_enuc ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 81
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__atol_enuc()
    
    @atol_enuc.setter
    def atol_enuc(self, atol_enuc):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__atol_enuc(atol_enuc)
    
    @property
    def retry_burn(self):
        """
        Element retry_burn ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 83
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 85
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 87
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 89
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 91
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 93
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 95
        
        """
        return _StarKillerMicrophysics.f90wrap_extern_probin_module__get__max_temp()
    
    @max_temp.setter
    def max_temp(self, max_temp):
        _StarKillerMicrophysics.f90wrap_extern_probin_module__set__max_temp(max_temp)
    
    @property
    def react_boost(self):
        """
        Element react_boost ftype=real (kind=rt) pytype=float
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 97
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 99
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 101
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 103
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__reactions_energy_scale()
    
    @reactions_energy_scale.setter
    def reactions_energy_scale(self, reactions_energy_scale):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__reactions_energy_scale(reactions_energy_scale)
    
    @property
    def ode_max_steps(self):
        """
        Element ode_max_steps ftype=integer pytype=int
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 105
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__ode_max_steps()
    
    @ode_max_steps.setter
    def ode_max_steps(self, ode_max_steps):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__ode_max_steps(ode_max_steps)
    
    @property
    def use_jacobian_caching(self):
        """
        Element use_jacobian_caching ftype=logical pytype=bool
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 line 107
        
        """
        return \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__get__use_jacobian_caching()
    
    @use_jacobian_caching.setter
    def use_jacobian_caching(self, use_jacobian_caching):
        \
            _StarKillerMicrophysics.f90wrap_extern_probin_module__set__use_jacobian_caching(use_jacobian_caching)
    
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
        ret.append(',\n    ode_max_steps : ')
        ret.append(repr(self.ode_max_steps))
        ret.append(',\n    use_jacobian_caching : ')
        ret.append(repr(self.use_jacobian_caching))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

extern_probin_module = Extern_Probin_Module()

class Sneut_Module(f90wrap.runtime.FortranModule):
    """
    Module sneut_module
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 14-1369
    
    """
    @staticmethod
    def sneut5(temp, den, abar, zbar, snu, dsnudt, dsnudd, dsnuda, dsnudz):
        """
        sneut5(temp, den, abar, zbar, snu, dsnudt, dsnudd, dsnuda, dsnudz)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 21-1200
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 1202-1278
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-sneut5.F90 lines 1280-1369
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 14-692
    
    """
    class Plasma_State(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=plasma_state)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 51-65
        
        """
        def __init__(self, handle=None):
            """
            self = Plasma_State()
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 51-65
            
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 51-65
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 53
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__qlam0z(self._handle)
        
        @qlam0z.setter
        def qlam0z(self, qlam0z):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__qlam0z(self._handle, qlam0z)
        
        @property
        def qlam0zdt(self):
            """
            Element qlam0zdt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 54
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 55
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 57
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__taufac(self._handle)
        
        @taufac.setter
        def taufac(self, taufac):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__taufac(self._handle, taufac)
        
        @property
        def taufacdt(self):
            """
            Element taufacdt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 58
            
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
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 60
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__aa(self._handle)
        
        @aa.setter
        def aa(self, aa):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__aa(self._handle, aa)
        
        @property
        def daadt(self):
            """
            Element daadt ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 61
            
            """
            return _StarKillerMicrophysics.f90wrap_plasma_state__get__daadt(self._handle)
        
        @daadt.setter
        def daadt(self, daadt):
            _StarKillerMicrophysics.f90wrap_plasma_state__set__daadt(self._handle, daadt)
        
        @property
        def daadd(self):
            """
            Element daadd ftype=double precision pytype=unknown
            
            
            Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 line 62
            
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 75-104
        
        
        """
        _StarKillerMicrophysics.f90wrap_screening_init()
    
    @staticmethod
    def screening_finalize():
        """
        screening_finalize()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 106-152
        
        
        """
        _StarKillerMicrophysics.f90wrap_screening_finalize()
    
    @staticmethod
    def add_screening_factor(z1, a1, z2, a2):
        """
        add_screening_factor(z1, a1, z2, a2)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 154-228
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 230-281
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 283-504
        
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
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-screen.F90 lines 506-692
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines \
        14-373
    
    """
    @staticmethod
    def actual_conductivity_init():
        """
        actual_conductivity_init()
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines 22-27
        
        
        """
        _StarKillerMicrophysics.f90wrap_actual_conductivity_init()
    
    @staticmethod
    def actual_conductivity(self):
        """
        actual_conductivity(self)
        
        
        Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-stellar_conductivity.F90 lines \
            29-373
        
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
    
    
    Defined at tmp_build_dir/f/3d.gnu.EXE/F90PP-extern.F90 lines 113-236
    
    Parameters
    ----------
    probin : str
    
    """
    _StarKillerMicrophysics.f90wrap_runtime_init(probin=probin)

