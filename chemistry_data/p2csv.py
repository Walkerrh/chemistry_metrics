import pandas as pd

# Define the complete data for phase change properties of pure substances
data = {
    "Name": [
        "acetic acid", "aluminum", "ammonia", "argon", "benzene", "benzonitrile", "biphenyl", "butane", "carbon dioxide",
        "carbon disulfide", "carbon tetrachloride", "chloroform", "copper", "cyclohexane", "diamond", "dibenzyl ether",
        "diethyl ether", "ethanol", "ethylene glycol", "formamide", "gold", "graphite", "hexane", "hydrogen", "iron", "lead",
        "mercury", "methane", "methanol", "naphthalene", "nitrogen", "octane", "oxygen", "sodium chloride", "sulfur hexafluoride",
        "trichlorosilane", "water"
    ],
    "Chemical Formula": [
        "CH3CO2H", "Al", "NH3", "Ar", "C6H6", "C6H5CN", "C12H10", "C4H10", "CO2", "CS2", "CCl4", "CHCl3", "Cu", "C6H12", "C",
        "(C6H5CH2)2O", "(CH3CH2)2O", "CH3CH2OH", "(CH2OH)2", "NH2COH", "Au", "C", "C6H14", "H2", "Fe", "Pb", "Hg", "CH4",
        "CH3OH", "C10H8", "N2", "C8H18", "O2", "NaCl", "SF6", "SiHCl3", "H2O"
    ],
    "Melting Point (°C)": [
        17.0, 660.323, -77.65, -189.34, 5.538, -12.82, 68.93, -138.2, -56.561, -111.7, -22.8, -63.3, 1084.62, 6.7, 4440,
        1.8, -116.22, -114.14, -13.0, 2.57, 1064.18, 4489, -95.27, -259.16, 1538, 327.462, -38.829, -182.475, -97.5, 80.22,
        -210, -56.73, -218.79, 802.018, -49.596, -128.2, 0
    ],
    "Boiling Point (°C)": [
        117.9, 2519, -33.33, -185.848, 80.08, 191, 255.2, -0.5, -78.464, 46.2, 76.7, 61.2, 2560, 80.7, None, 298, 34.4,
        78.24, 197.5, 217, 2836, 3825, 68.72, -252.879, 2861, 1749, 356.619, -161.5, 64.5, 218, -195.795, 125.62, -182.962,
        1465, -63.8, 33, 99.974
    ],
    "Specific Heat Capacity (J·g-1·°C-1) at 25°C": [
        2.053, 0.897, 35.1, 0.52, 1.741, 1.602, 1.287, None, 0.843, 1.003, 0.85, 0.957, 0.385, 1.841, 0.51, None, 2.369,
        2.438, 2.394, 2.389, 0.129, 0.709, 2.27, 14.304, 0.449, 0.13, 0.14, 2.23, 2.531, 1.293, 1.04, 2.229, 0.918, 0.864,
        0.664, 0.56, 4.184
    ],
    "Heat of fusion (ΔHfus) kJ·mol-1": [
        11.73, 10.71, 5.66, 1.18, 9.87, 9.1, 18.57, 4.66, 9.02, 4.39, 2.56, 9.5, 13.26, 2.68, None, None, 7.19, 4.931, 9.96, 8.44, 12.55, 117.4, 13.08, 0.12, 13.81, 4.774, 2.295, 0.94, 3.215, 19.01, 0.71, 20.73, 0.44, 28.16, 5.02, None, 6.01
    ],
    "Heat of vaporization (ΔHvap)kJ·mol-1": [
    23.7, 294, 23.33, 6.43, 30.72, 45.9, None, 22.44, 16.7, 26.74, 29.82, 29.24, None, 29.97, None, 45.6, 26.52, 38.56, 50.5, 60.2, 324, None, 28.85, 0.9, None, 179.5, 59.11, 8.19, 35.21, 43.2, 5.57, 34.41, 6.82, None, None, None, 40.65
    ],
    "Critical temp °C": [
    320, 6427, 132.41, -122.463, 289, 418, 499.85, None, 30.98, 278.85, 283.35, 262.85, None, 280.3, None, None, 193.7, 242, 446, None, None, None, 234.4, -240.212, 9067, None, 1491, -82.59, 239.6, 475.15, -146.958, 295.6, -118.569, None, 45.573, 205.85, 374
    ],
    "Critical pressure atm": [
    57.1, None, 112.08, 47.99, 48.4, 41.6, 33.9, None, 72.79, 78, 45.1, 54, None, 40.2, None, None, 35.9, 61.7, 80, None, None, None, 29.9, 12.69, None, None, 1648, 45, 79.1, 40.1, 33.514, 24.5, 49.77, None, 37.2, None, 217.7
    ],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
csv_path = "/Users/walkerhutchinson/Desktop/chemistry_data/Phase_Change_Properties.csv"
df.to_csv(csv_path, index=False)

csv_path
