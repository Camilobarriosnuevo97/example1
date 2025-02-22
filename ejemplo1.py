#Example 1
import streamlit as st ## para crear la aplicación
import plotly.express as px ### gráficas interactivas
import pandas as pd ### Manipulación de datos

# Title of the app
st.title("Streamlit Dashboard with Plotly")

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)
