# Climate Change Dashboard
# A Streamlit app to visualize global warming trends using temperature data.
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Climate Change Dashboard 🌍",
    layout="wide",
    page_icon="🌡️"
)


st.title("🌍 Climate Change Dashboard")
st.markdown("##### Analyze global warming trends over time using interactive visualizations.")
st.markdown("---")


@st.cache_data
def load_global_data():
    df = pd.read_csv("GlobalTemperatures.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df[df['Year'] >= 1900]
    return df

global_df = load_global_data()


global_yearly = global_df.groupby('Year')['LandAverageTemperature'].mean().reset_index()
global_yearly['TempChange'] = global_yearly['LandAverageTemperature'].diff()


tab1, tab2, tab3, tab4 = st.tabs(["🌡️ Global Trend", "📈 Year-on-Year Change", "📌 Data Explorer", "🌐 Country-wise Trend"])


with tab1:
    st.subheader("📊 Global Average Land Temperature (1900 - 2015)")
    
    # Metrics
    latest_temp = global_yearly['LandAverageTemperature'].iloc[-1]
    first_temp = global_yearly['LandAverageTemperature'].iloc[0]
    change = round(latest_temp - first_temp, 2)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📅 First Year Avg Temp", f"{first_temp:.2f} °C")
    col2.metric("📅 Latest Year Avg Temp", f"{latest_temp:.2f} °C", f"{change:+.2f} °C")
    col3.metric("📈 Overall Change", f"{change:+.2f} °C")

    fig = px.line(
        global_yearly,
        x="Year",
        y="LandAverageTemperature",
        title="🌍 Average Land Temperature Over Time",
        labels={"LandAverageTemperature": "Avg Temp (°C)"},
        markers=True
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)


with tab2:
    st.subheader("📉 Year-on-Year Temperature Change")
    fig_change = px.bar(
        global_yearly,
        x="Year",
        y="TempChange",
        title="🔺 Yearly Temperature Difference",
        labels={"TempChange": "Change in Avg Temp (°C)"},
        color="TempChange",
        color_continuous_scale="RdBu"
    )
    st.plotly_chart(fig_change, use_container_width=True)


with tab3:
    st.subheader("📋 Explore Raw Data (GlobalTemperatures.csv)")
    st.dataframe(global_df[['dt', 'LandAverageTemperature', 'LandMaxTemperature', 'LandMinTemperature']].dropna().reset_index(drop=True), use_container_width=True)


with tab4:
    st.subheader("🌐 Country-wise Average Temperature Trend")
    
    # Load country data
    @st.cache_data
    def load_country_data():
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        df = df[df['Year'] >= 1900]
        return df

    country_temp = load_country_data()

    # Country dropdown
    country = st.selectbox("🌍 Choose a country", sorted(country_temp['Country'].unique()))
    
    # Filter and group
    country_filtered = country_temp[country_temp['Country'] == country]
    country_yearly = country_filtered.groupby('Year')['AverageTemperature'].mean().reset_index()

    # Chart
    fig_country = px.line(
        country_yearly,
        x="Year",
        y="AverageTemperature",
        title=f"📈 Average Temperature in {country} (1900–2013)",
        labels={"AverageTemperature": "Avg Temp (°C)"},
        markers=True
    )
    st.plotly_chart(fig_country, use_container_width=True)
