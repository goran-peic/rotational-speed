%pip install plotly
%pip install nbformat
%pip install ipykernel
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Setup Constants
EARTH_RADIUS_KM = 6378.1
SECONDS_IN_SIDEREAL_DAY = 86164.09  # 23.93 hours
ANGULAR_VELOCITY = (2 * np.pi) / SECONDS_IN_SIDEREAL_DAY

# 2. Generate Data
# Degrees from 0 (Equator) to 90 (North Pole)
latitudes = np.linspace(0, 90, 500)
lat_radians = np.radians(latitudes) # Convert to radians for calculation

# Calculate tangential speed: v = omega * R * cos(latitude)
speeds_km_s = ANGULAR_VELOCITY * EARTH_RADIUS_KM * np.cos(lat_radians)
speeds_km_h = speeds_km_s * 3600 # Convert to km/h

# Create DataFrame
df = pd.DataFrame({
    'Latitude (Degrees)': latitudes,
    'Rotational Speed (km/h)': speeds_km_h
})

# 3. Generate Interactive Plot
fig = px.line(
    df, 
    x='Latitude (Degrees)', 
    y='Rotational Speed (km/h)',
    title='<b>Rotational Speed Across Latitudes</b>',
    template='plotly_dark',  # Dark theme requirement
    labels={'Latitude (Degrees)': 'Degrees from Equator', 'Rotational Speed (km/h)': 'Speed (km/h)'}
)

# 4. Update the plot to have the Seaborn-type look
fig.update_traces(line=dict(color='#00D4FF', width=3))
fig.update_layout(
    hovermode="x unified",
    font=dict(family="Arial", size=12),
    title_x=0.5
)

fig.show()
