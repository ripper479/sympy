"""
SI unit system.
Based on MKSA, which stands for "meter, kilogram, second, ampere".
Added kelvin, candela and mole.

"""

from __future__ import division

from sympy.physics.units import DimensionSystem, Dimension

from sympy import Rational, pi, sqrt, S
from sympy.physics.units.definitions.dimension_definitions import (
    acceleration, action, current, impedance, length, mass, time, velocity,
    amount_of_substance, temperature, information, frequency, force, pressure,
    energy, power, charge, voltage, capacitance, conductance, magnetic_flux,
    magnetic_density, inductance, luminous_intensity
)
from sympy.physics.units.prefixes import (
    kibi, mebi, gibi, tebi, pebi, exbi
)
from sympy.physics.units.definitions import (
    kilogram, newton, second, meter, gram, cd, K, joule, watt, pascal, hertz,
    coulomb, volt, ohm, siemens, farad, henry, tesla, weber, dioptre, lux,
    katal, gray, becquerel, inch, liter, julian_year, gravitational_constant,
    speed_of_light, elementary_charge, planck, hbar, electronvolt,
    avogadro_number, avogadro_constant, boltzmann_constant,
    stefan_boltzmann_constant, atomic_mass_constant, molar_gas_constant,
    faraday_constant, josephson_constant, von_klitzing_constant,
    acceleration_due_to_gravity, magnetic_constant, vacuum_permittivity,
    vacuum_impedance, coulomb_constant, atmosphere, bar, pound, psi, mmHg,
    milli_mass_unit, quart, lightyear, astronomical_unit, planck_mass,
    planck_time, planck_temperature, planck_length, planck_charge, planck_area,
    planck_volume, planck_momentum, planck_energy, planck_force, planck_power,
    planck_density, planck_energy_density, planck_intensity,
    planck_angular_frequency, planck_pressure, planck_current, planck_voltage,
    planck_impedance, planck_acceleration, bit, byte, kibibyte, mebibyte,
    gibibyte, tebibyte, pebibyte, exbibyte, curie, rutherford, radian, degree,
    steradian, angular_mil, atomic_mass_unit, gee, kPa, ampere, u0, c, kelvin,
    mol, mole, candela, m, kg, s, electric_constant, G, boltzmann
)
from sympy.physics.units.prefixes import PREFIXES, prefix_unit
from sympy.physics.units.systems.mksa import MKSA, dimsys_MKSA

derived_dims = (frequency, force, pressure, energy, power, charge, voltage,
                capacitance, conductance, magnetic_flux,
                magnetic_density, inductance, luminous_intensity)
base_dims = (amount_of_substance, luminous_intensity, temperature)

units = [mol, cd, K, lux, hertz, newton, pascal, joule, watt, coulomb, volt,
        farad, ohm, siemens, weber, tesla, henry, candela, lux, becquerel,
        gray, katal]
all_units = []
for u in units:
    all_units.extend(prefix_unit(u, PREFIXES))

all_units.extend([mol, cd, K, lux])


dimsys_SI = dimsys_MKSA.extend(
    [
        # Dimensional dependencies for other base dimensions:
        temperature,
        amount_of_substance,
        luminous_intensity,
    ])

dimsys_default = dimsys_SI.extend(
    [information],
)

SI = MKSA.extend(base=(mol, cd, K), units=all_units, name='SI', dimension_system=dimsys_SI)

One = S.One


# Angular units (dimensionless)
SI.set_quantity_dimension(radian, One)
SI.set_quantity_scale_factor(radian, One)

SI.set_quantity_dimension(degree, One)
SI.set_quantity_scale_factor(degree, pi/180)

SI.set_quantity_dimension(steradian, One)
SI.set_quantity_scale_factor(steradian, One)

SI.set_quantity_dimension(angular_mil, One)
SI.set_quantity_scale_factor(angular_mil, 2*pi/6400)

# Base units:
SI.set_quantity_dimension(meter, length)
SI.set_quantity_scale_factor(meter, One)

# gram; used to define its prefixed units

SI.set_quantity_dimension(gram, mass)
SI.set_quantity_scale_factor(gram, One)

SI.set_quantity_dimension(second, time)
SI.set_quantity_scale_factor(second, One)

SI.set_quantity_dimension(ampere, current)
SI.set_quantity_scale_factor(ampere, One)

SI.set_quantity_dimension(kelvin, temperature)
SI.set_quantity_scale_factor(kelvin, One)

SI.set_quantity_dimension(mole, amount_of_substance)
SI.set_quantity_scale_factor(mole, One)

SI.set_quantity_dimension(candela, luminous_intensity)
SI.set_quantity_scale_factor(candela, One)

# derived units

SI.set_quantity_dimension(newton, force)
SI.set_quantity_scale_factor(newton, kilogram*meter/second**2)

SI.set_quantity_dimension(joule, energy)
SI.set_quantity_scale_factor(joule, newton*meter)

SI.set_quantity_dimension(watt, power)
SI.set_quantity_scale_factor(watt, joule/second)

SI.set_quantity_dimension(pascal, pressure)
SI.set_quantity_scale_factor(pascal, newton/meter**2)

SI.set_quantity_dimension(hertz, frequency)
SI.set_quantity_scale_factor(hertz, One)

# MKSA extension to MKS: derived units


SI.set_quantity_dimension(coulomb, charge)
SI.set_quantity_scale_factor(coulomb, One)

SI.set_quantity_dimension(volt, voltage)
SI.set_quantity_scale_factor(volt, joule/coulomb)

SI.set_quantity_dimension(ohm, impedance)
SI.set_quantity_scale_factor(ohm, volt/ampere)

SI.set_quantity_dimension(siemens, conductance)
SI.set_quantity_scale_factor(siemens, ampere/volt)

SI.set_quantity_dimension(farad, capacitance)
SI.set_quantity_scale_factor(farad, coulomb/volt)

SI.set_quantity_dimension(henry, inductance)
SI.set_quantity_scale_factor(henry, volt*second/ampere)

SI.set_quantity_dimension(tesla, magnetic_density)
SI.set_quantity_scale_factor(tesla, volt*second/meter**2)

SI.set_quantity_dimension(weber, magnetic_flux)
SI.set_quantity_scale_factor(weber, joule/ampere)


# Other derived units:

SI.set_quantity_dimension(dioptre, 1 / length)
SI.set_quantity_scale_factor(dioptre, 1/meter)

SI.set_quantity_dimension(lux, luminous_intensity / length ** 2)
SI.set_quantity_scale_factor(lux, steradian*candela/meter**2)

# katal is the SI unit of catalytic activity

SI.set_quantity_dimension(katal, amount_of_substance / time)
SI.set_quantity_scale_factor(katal, mol/second)

# gray is the SI unit of absorbed dose

SI.set_quantity_dimension(gray, energy / mass)
SI.set_quantity_scale_factor(gray, meter**2/second**2)

# becquerel is the SI unit of radioactivity

SI.set_quantity_dimension(becquerel, 1 / time)
SI.set_quantity_scale_factor(becquerel, 1/second)


# Common volume and area units

SI.set_quantity_dimension(liter, length ** 3)
SI.set_quantity_scale_factor(liter, meter**3 / 1000)


#### CONSTANTS ####

# Newton constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(gravitational_constant, length ** 3 * mass ** -1 * time ** -2)
SI.set_quantity_scale_factor(gravitational_constant, 6.67430e-11*m**3/(kg*s**2))

# speed of light

SI.set_quantity_dimension(speed_of_light, velocity)
SI.set_quantity_scale_factor(speed_of_light, 299792458*meter/second)

# elementary charge
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(elementary_charge, charge)
SI.set_quantity_scale_factor(elementary_charge, 1.602176634e-19*coulomb)

# Planck constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(planck, action)
SI.set_quantity_scale_factor(planck, 6.62607015e-34*joule*second)

# Reduced Planck constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(hbar, action)
SI.set_quantity_scale_factor(hbar, planck / (2 * pi))

# Electronvolt
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(electronvolt, energy)
SI.set_quantity_scale_factor(electronvolt, 1.602176634e-19*joule)

# Avogadro number
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(avogadro_number, One)
SI.set_quantity_scale_factor(avogadro_number, 6.02214076e23)

# Avogadro constant

SI.set_quantity_dimension(avogadro_constant, amount_of_substance ** -1)
SI.set_quantity_scale_factor(avogadro_constant, avogadro_number / mol)

# Boltzmann constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(boltzmann_constant, energy / temperature)
SI.set_quantity_scale_factor(boltzmann_constant, 1.380649e-23*joule/kelvin)

# Stefan-Boltzmann constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(stefan_boltzmann_constant, energy * time ** -1 * length ** -2 * temperature ** -4)
SI.set_quantity_scale_factor(stefan_boltzmann_constant, pi**2 * boltzmann_constant**4 / (60 * hbar**3 * speed_of_light ** 2))

# Atomic mass
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(atomic_mass_constant, mass)
SI.set_quantity_scale_factor(atomic_mass_constant, 1.66053906660e-24*gram)

# Molar gas constant
# REF: NIST SP 959 (June 2019)

SI.set_quantity_dimension(molar_gas_constant, energy / (temperature * amount_of_substance))
SI.set_quantity_scale_factor(molar_gas_constant, boltzmann_constant * avogadro_constant)

# Faraday constant

SI.set_quantity_dimension(faraday_constant, charge / amount_of_substance)
SI.set_quantity_scale_factor(faraday_constant, elementary_charge * avogadro_constant)

# Josephson constant

SI.set_quantity_dimension(josephson_constant, frequency / voltage)
SI.set_quantity_scale_factor(josephson_constant, 0.5 * planck / elementary_charge)

# Von Klitzing constant

SI.set_quantity_dimension(von_klitzing_constant, voltage / current)
SI.set_quantity_scale_factor(von_klitzing_constant, hbar / elementary_charge ** 2)

# Acceleration due to gravity (on the Earth surface)

SI.set_quantity_dimension(acceleration_due_to_gravity, acceleration)
SI.set_quantity_scale_factor(acceleration_due_to_gravity, 9.80665*meter/second**2)

# magnetic constant:

SI.set_quantity_dimension(magnetic_constant, force / current ** 2)
SI.set_quantity_scale_factor(magnetic_constant, 4*pi/10**7 * newton/ampere**2)

# electric constat:

SI.set_quantity_dimension(vacuum_permittivity, capacitance / length)
SI.set_quantity_scale_factor(vacuum_permittivity, 1/(u0 * c**2))

# vacuum impedance:

SI.set_quantity_dimension(vacuum_impedance, impedance)
SI.set_quantity_scale_factor(vacuum_impedance, u0 * c)

# Coulomb's constant:
SI.set_quantity_dimension(coulomb_constant, force * length ** 2 / charge ** 2)
SI.set_quantity_scale_factor(coulomb_constant, 1/(4*pi*vacuum_permittivity))

SI.set_quantity_dimension(atmosphere, pressure)
SI.set_quantity_scale_factor(atmosphere, 101325 * pascal)

SI.set_quantity_dimension(bar, pressure)
SI.set_quantity_scale_factor(bar, 100*kPa)

SI.set_quantity_dimension(pound, mass)
SI.set_quantity_scale_factor(pound, Rational(45359237, 100000000) * kg)

SI.set_quantity_dimension(psi, pressure)
SI.set_quantity_scale_factor(psi, pound * gee / inch ** 2)

dHg0 = 13.5951  # approx value at 0 C

SI.set_quantity_dimension(mmHg, pressure)
SI.set_quantity_scale_factor(mmHg, dHg0 * acceleration_due_to_gravity * kilogram / meter**2)

SI.set_quantity_dimension(milli_mass_unit, mass)
SI.set_quantity_scale_factor(milli_mass_unit, atomic_mass_unit/1000)

SI.set_quantity_dimension(quart, length ** 3)
SI.set_quantity_scale_factor(quart, Rational(231, 4) * inch**3)

# Other convenient units and magnitudes


SI.set_quantity_dimension(lightyear, length)
SI.set_quantity_scale_factor(lightyear, speed_of_light*julian_year)

SI.set_quantity_dimension(astronomical_unit, length)
SI.set_quantity_scale_factor(astronomical_unit, 149597870691*meter)

# Fundamental Planck units:

SI.set_quantity_dimension(planck_mass, mass)
SI.set_quantity_scale_factor(planck_mass, sqrt(hbar*speed_of_light/G))

SI.set_quantity_dimension(planck_time, time)
SI.set_quantity_scale_factor(planck_time, sqrt(hbar*G/speed_of_light**5))

SI.set_quantity_dimension(planck_temperature, temperature)
SI.set_quantity_scale_factor(planck_temperature, sqrt(hbar*speed_of_light**5/G/boltzmann**2))

SI.set_quantity_dimension(planck_length, length)
SI.set_quantity_scale_factor(planck_length, sqrt(hbar*G/speed_of_light**3))

SI.set_quantity_dimension(planck_charge, charge)
SI.set_quantity_scale_factor(planck_charge, sqrt(4*pi*electric_constant*hbar*speed_of_light))

# Derived Planck units:

SI.set_quantity_dimension(planck_area, length ** 2)
SI.set_quantity_scale_factor(planck_area, planck_length**2)

SI.set_quantity_dimension(planck_volume, length ** 3)
SI.set_quantity_scale_factor(planck_volume, planck_length**3)

SI.set_quantity_dimension(planck_momentum, mass * velocity)
SI.set_quantity_scale_factor(planck_momentum, planck_mass * speed_of_light)

SI.set_quantity_dimension(planck_energy, energy)
SI.set_quantity_scale_factor(planck_energy, planck_mass * speed_of_light**2)

SI.set_quantity_dimension(planck_force, force)
SI.set_quantity_scale_factor(planck_force, planck_energy / planck_length)

SI.set_quantity_dimension(planck_power, power)
SI.set_quantity_scale_factor(planck_power, planck_energy / planck_time)

SI.set_quantity_dimension(planck_density, mass / length ** 3)
SI.set_quantity_scale_factor(planck_density, planck_mass / planck_length**3)

SI.set_quantity_dimension(planck_energy_density, energy / length ** 3)
SI.set_quantity_scale_factor(planck_energy_density, planck_energy / planck_length**3)

SI.set_quantity_dimension(planck_intensity, mass * time ** (-3))
SI.set_quantity_scale_factor(planck_intensity, planck_energy_density * speed_of_light)

SI.set_quantity_dimension(planck_angular_frequency, 1 / time)
SI.set_quantity_scale_factor(planck_angular_frequency, 1 / planck_time)

SI.set_quantity_dimension(planck_pressure, pressure)
SI.set_quantity_scale_factor(planck_pressure, planck_force / planck_length**2)

SI.set_quantity_dimension(planck_current, current)
SI.set_quantity_scale_factor(planck_current, planck_charge / planck_time)

SI.set_quantity_dimension(planck_voltage, voltage)
SI.set_quantity_scale_factor(planck_voltage, planck_energy / planck_charge)

SI.set_quantity_dimension(planck_impedance, impedance)
SI.set_quantity_scale_factor(planck_impedance, planck_voltage / planck_current)

SI.set_quantity_dimension(planck_acceleration, acceleration)
SI.set_quantity_scale_factor(planck_acceleration, speed_of_light / planck_time)

# Information theory units:

SI.set_quantity_dimension(bit, information)
SI.set_quantity_scale_factor(bit, One)

SI.set_quantity_dimension(byte, information)
SI.set_quantity_scale_factor(byte, 8*bit)

SI.set_quantity_dimension(kibibyte, information)
SI.set_quantity_scale_factor(kibibyte, kibi*byte)

SI.set_quantity_dimension(mebibyte, information)
SI.set_quantity_scale_factor(mebibyte, mebi*byte)

SI.set_quantity_dimension(gibibyte, information)
SI.set_quantity_scale_factor(gibibyte, gibi*byte)

SI.set_quantity_dimension(tebibyte, information)
SI.set_quantity_scale_factor(tebibyte, tebi*byte)

SI.set_quantity_dimension(pebibyte, information)
SI.set_quantity_scale_factor(pebibyte, pebi*byte)

SI.set_quantity_dimension(exbibyte, information)
SI.set_quantity_scale_factor(exbibyte, exbi*byte)

# Older units for radioactivity

SI.set_quantity_dimension(curie, 1 / time)
SI.set_quantity_scale_factor(curie, 37000000000*becquerel)

SI.set_quantity_dimension(rutherford, 1 / time)
SI.set_quantity_scale_factor(rutherford, 1000000*becquerel)


# check that scale factors are the right SI dimensions:
for _scale_factor, _dimension in zip(
    SI._quantity_scale_factors.values(),
    SI._quantity_dimension_map.values()
):
    dimex = SI.get_dimensional_expr(_scale_factor)
    if dimex != 1:
        if not DimensionSystem.equivalent_dims(_dimension, Dimension(dimex)):
            raise ValueError("quantity value and dimension mismatch")
del _scale_factor, _dimension
