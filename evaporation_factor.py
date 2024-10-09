from utils import round_to_nearest

# Data: Evaporation correction factors dictionary
evaporation_correction_factors = {
    30: -2,
    35: -3,
    40: -3,
    45: -3,
    50: -3,
    55: -3,
    60: -4,
    65: -4,
    70: -4,
    75: -4,
    80: -5,
    85: -5,
    90: -6,
    95: -6,
    100: -6,
    105: -7,
    110: -7,
    115: -8,
    120: -8,
    125: -9,
}


# Function to get the evaporation index
def fuel_surf_temp_evap_ind(fuel_surf_temp):
    if fuel_surf_temp <= 30:
        return 30
    elif fuel_surf_temp > 122.5:
        return 125
    else:
        return round_to_nearest(fuel_surf_temp, 5)


# Main function to get the evaporation correction factor
def get_evaporation_correction_factor(fuel_surf_temp):
    return evaporation_correction_factors[fuel_surf_temp_evap_ind(fuel_surf_temp)]
