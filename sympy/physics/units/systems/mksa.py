"""
MKS unit system.

MKS stands for "meter, kilogram, second, ampere".
"""

from __future__ import division

from sympy.physics.units.definitions import Z0, A, C, F, H, S, T, V, Wb, ohm
from sympy.physics.units.definitions.dimension_definitions import (
    capacitance, charge, conductance, current, impedance, inductance,
    magnetic_density, magnetic_flux, voltage)
from sympy.physics.units.prefixes import PREFIXES, prefix_unit
from sympy.physics.units.systems.mks import MKS, dimsys_MKS

dims = (voltage, impedance, conductance, current, capacitance, inductance, charge,
        magnetic_density, magnetic_flux)

units = [A, V, ohm, S, F, H, C, T, Wb]
all_units = []
for u in units:
    all_units.extend(prefix_unit(u, PREFIXES))

all_units.extend([Z0])

dimsys_MKSA = dimsys_MKS.extend([
    # Dimensional dependencies for base dimensions (MKSA not in MKS)
    current,
], new_dim_deps=dict(
    # Dimensional dependencies for derived dimensions
    voltage=dict(mass=1, length=2, current=-1, time=-3),
    impedance=dict(mass=1, length=2, current=-2, time=-3),
    conductance=dict(mass=-1, length=-2, current=2, time=3),
    capacitance=dict(mass=-1, length=-2, current=2, time=4),
    inductance=dict(mass=1, length=2, current=-2, time=-2),
    charge=dict(current=1, time=1),
    magnetic_density=dict(mass=1, current=-1, time=-2),
    magnetic_flux=dict(length=2, mass=1, current=-1, time=-2),
))

MKSA = MKS.extend(base=(A,), units=all_units, name='MKSA', dimension_system=dimsys_MKSA)
