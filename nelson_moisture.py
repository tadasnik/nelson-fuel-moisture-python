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
    init_moisture = 0
    rMF = 0
    eCF = 0
    mCF = 0
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
