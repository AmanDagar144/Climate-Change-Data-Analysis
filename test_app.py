import pandas as pd
from app import load_global_data

def test_load_global_data():
    df = load_global_data()
    # Check if DataFrame is not empty
    assert not df.empty
    # Verify expected columns exist
    assert 'LandAverageTemperature' in df.columns
    # Ensure years are within expected range
    assert df['Year'].min() >= 1900
def test_global_trend_calculation():
    df = load_global_data()
    grouped = df.groupby('Year')['LandAverageTemperature'].mean().reset_index()
    assert 'Year' in grouped.columns
    assert 'LandAverageTemperature' in grouped.columns
    assert grouped['LandAverageTemperature'].dtype == float
