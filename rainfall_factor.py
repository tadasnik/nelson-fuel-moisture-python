from utils import round_to_nearest

# Rainfall factor dictionary
rainfall_factors = {
    0.0: 4,
    0.25: 8,
    0.5: 15,
    0.75: 19,
    1.0: 22,
    1.25: 25,
    1.5: 26,
    1.75: 28,
    2.0: 29,
    2.25: 29,
    2.5: 30,
    2.75: 30,
    3.0: 30,
    3.25: 30,
    3.5: 31,
}


# Function to get the rain index
def rain_ind(rainfall):
    if rainfall <= 0:
        return 0.0
    elif rainfall > 3.31:
        return 3.5
    else:
        return round_to_nearest(rainfall, 0.25)


# Main function to get the rainfall factor
def get_rainfall_factor(rainfall):
    return rainfall_factors[rain_ind(rainfall)]
