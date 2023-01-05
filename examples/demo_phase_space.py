
from ParticlePhaseSpace import DataLoaders
from ParticlePhaseSpace.ParticlePhaseSpace import ParticlePhaseSpace
from pathlib import Path
import matplotlib as mpl

mpl.rcParams['figure.dpi'] = 200

# load topas data
test_data_loc = Path(r'coll_PhaseSpace_xAng_0.00_yAng_0.00_angular_error_0.0.phsp').absolute()
ps_data = DataLoaders.LoadTopasData(test_data_loc)
PS = ParticlePhaseSpace(ps_data)

# print report ro the screen
PS.report()
# generate new phase spaces based on different particle species
electrons_only = PS('electrons')
gamma_only, positrons_only = PS(['gammas', 'positrons'])
# we can add these back together using the + operator:
all_particles = electrons_only + gamma_only + positrons_only
# we cannot add phase space objects together when they contain the same particles
# you have to change the particle IDs if you really want to do this.
try:
    doubled = electrons_only + electrons_only
except:
    print('that didnt work')
# or we can create a phase space by subtracting one set of particles from the rest:
electrons_and_gamma = all_particles - positrons_only

downsampled = PS.get_downsampled_phase_space(downsample_factor=10)