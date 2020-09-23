import pynucastro as pyna
from pynucastro.networks import StarKillerNetwork

library_file = "/usr/local/lib/python3.8/dist-packages/pynucastro-1.4.0-py3.8.egg/pynucastro/library/20180319default2"
mylibrary = pyna.rates.Library(library_file)

data_list = mylibrary.get_rates()

all_nuclei = ["p","he4","ne20","o20","f20","mg24","al27","o16","si28","s32","p31","na24","mg27"]

escn_library = mylibrary.linking_nuclei(all_nuclei,with_reverse=True)
escn_tabular = ["f20--o20-toki","ne20--f20-toki","o20--f20-toki","f20--ne20-toki","mg24--na24-toki","na24--mg24-toki","al27--mg27-toki","mg27--al27-toki"]

rc = pyna.RateCollection(libraries=[escn_library])

#print(len(ecsn_rates))
#ecsn = pyna.StarKillerNetwork(rate_files=ecsn_rates)
comp = pyna.Composition(rc.get_nuclei())
comp.set_nuc("o16", 0.5)
comp.set_nuc("ne20", 0.3)
comp.set_nuc("mg24", 0.1)
comp.set_nuc("o20", 1.e-5)
comp.set_nuc("f20", 1.e-5)
comp.set_nuc("p", 1.e-5)
comp.set_nuc("he4", 1.e-2)
comp.set_nuc("al27", 1.e-2)
comp.set_nuc("si28", 1.e-2)
comp.set_nuc("s32", 1.e-2)
comp.set_nuc("p31", 1.e-2)
comp.normalize()

new_rate_list = []
#ydots = rc.evaluate_rates(rho=7.e9, T=1.e9, composition=comp)
for rate in rc.rates:
    if not rate.weak:
        new_rate_list.append(rate)

#ecsn = pyna.RateCollection(rates=new_rate_list, rate_files=escn_tabular)
ecsn = StarKillerNetwork(rates=new_rate_list, rate_files=escn_tabular)


print(ecsn)
print("The number of reactions in the ECSN network is",len(ecsn.rates))

print(ecsn.network_overview())


ecsn.write_network(use_cse=True)

