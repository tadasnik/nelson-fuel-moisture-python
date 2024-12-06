"""
A simplified Nelson's dead fuel moisture model as
described in the following documents: https://www.wfas.net/ffmc/docs
author: Tadas Nikonovas tadas.nik@gmail.com
"""

from fuel_surface_temperature import get_fuel_surf_temp
from equilibrium_moisture import get_eq_moist_content
from rainfall_factor import get_rainfall_factor
from evaporation_factor import get_evaporation_correction_factor
from moisture_factor import get_moisture_correction_factor


def nelson_fuel_moisture(
    prev_moist: float | None,
    temp: float,
    sol_rad: float,
    rel_hum: float,
    rainfall: float,
) -> float:
    """Calculate the new hourly fuel moisture content.

    params:

    prev_moist: Previous dead fuel moisture content. If None,
    it is assumed to be the equilibrium moisture content.
    temp: Temperature in Celsius (current hour).
    sol_rad: Solar radiation in W/m^2 (current hour).
    rel_hum: Relative humidity in % (current hour).
    rainfall: Rainfall in mm during the last hour.
    """

    fuel_temp = get_fuel_surf_temp(temp, sol_rad)

    equilibrium_moisture_content = get_eq_moist_content(fuel_temp, rel_hum)
    if prev_moist is None:
        init_moisture = equilibrium_moisture_content
    else:
        init_moisture = prev_moist
    if rainfall > 0:
        rMF = get_rainfall_factor(rainfall)
    elif init_moisture > 30:
        eCF = get_evaporation_correction_factor(fuel_temp)
    else:
        mCF = get_moisture_correction_factor(
            init_moisture, equilibrium_moisture_content, fuel_temp, rel_hum
        )

    newFMC = init_moisture + rMF + eCF + mCF
    if newFMC > 60:
        return 60
    else:
        return newFMC
