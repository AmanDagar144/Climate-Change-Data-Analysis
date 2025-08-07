
# 🌍 Climate Change Dashboard using Streamlit

An interactive and dynamic dashboard built with **Streamlit** that visualizes historical global temperatures and analyzes the **impact of climate change** across the globe.

---

## 🚀 Features

✨ **Global Temperature Visualization** (1900–2015)  
🌐 **Country-wise Climate Trends**  
📊 **Interactive Line Charts using Plotly**  
📋 **Year-wise Aggregation of Average Temperatures**  
🧮 Built entirely using **Python + Streamlit**

---

## 🧰 Technologies & Libraries

| Tool        | Purpose                      |
|-------------|------------------------------|
| Python      | Core Programming             |
| Streamlit   | Dashboard/Web Interface      |
| Pandas      | Data Processing              |
| Plotly      | Interactive Visualizations   |

---

## 📁 Dataset Source

All datasets used are from the **Berkeley Earth Project** (via Kaggle):

- `GlobalLandTemperaturesByCountry.csv`
- `GlobalLandTemperaturesByMajorCity.csv`

> Dataset: [Kaggle – Climate Change Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)

---

## 📸 App Preview

```python
st.title("🌍 Climate Change Dashboard")

# Global Trend Chart
st.line_chart(global_yearly.set_index('Year')['LandAverageTemperature'])

# Country Selection and Chart
country = st.selectbox("🌐 Choose a Country", country_temp['Country'].unique())
country_filtered = country_temp[country_temp['Country'] == country]
country_yearly = country_filtered.groupby('Year')['AverageTemperature'].mean().reset_index()
st.line_chart(country_yearly.set_index('Year'))
```

