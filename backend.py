import pandas as pd
import folium

# Function to load the Excel file correctly
def load_data(file_path):
    try:
        df = pd.read_excel(file_path, engine="openpyxl")

        # Fix column names to match the Excel sheet
        df.rename(
            columns={
                "LATITUDE": "Latitude",
                "LONGITUDE": "Longitude",
                "STATION": "Station"
            }, inplace=True
        )

        # Ensure the required columns exist
        if not {"Latitude", "Longitude", "Station"}.issubset(df.columns):
            raise KeyError("Missing required columns: 'Latitude', 'Longitude', or 'Station'")

        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to create an interactive map using Folium
def create_map(data):
    if data is None:
        print("No data available to generate the map.")
        return

    # Center map at the first location in the dataset
    first_lat, first_lon = data.iloc[0]["Latitude"], data.iloc[0]["Longitude"]
    my_map = folium.Map(location=[first_lat, first_lon], zoom_start=8)

    # Add markers for each weather station
    for _, row in data.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=row["Station"],
            icon=folium.Icon(color="blue", icon="cloud"),
        ).add_to(my_map)

    # Save the map as an HTML file
    my_map.save("map.html")
