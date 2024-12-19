import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set page configuration
st.set_page_config(page_title="Biomass Pyrolysis Predictor", layout="wide")

# Title and description
st.title("Biomass Pyrolysis Yield Predictor")
st.write("Enter the input parameters to predict H2 and Char yields")

def load_and_prepare_data():
    # Read the data
    df = pd.read_excel('data_outliers_removed.xlsx')
    
    # Separate features and targets
    X = df[['H (%)', 'N (%)', 'O (%)', 'S (%)', 'VM (%)', 
            'Ash (%)', 'FC (%)', 'T (°C)', 'OC (%)', 'SBR']]
    y_h2 = df['H2 (wt.%)']
    y_char = df['Char yield (wt.%)']
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train Random Forest models
    rf_h2 = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_char = RandomForestRegressor(n_estimators=100, random_state=42)
    
    rf_h2.fit(X_scaled, y_h2)
    rf_char.fit(X_scaled, y_char)
    
    return rf_h2, rf_char, scaler

# Load models and scaler
rf_h2, rf_char, scaler = load_and_prepare_data()

# Create input form
st.sidebar.header("Input Parameters")

# Dictionary to store input ranges
input_ranges = {
    'H (%)': (5.4, 7.0),
    'N (%)': (0.1, 2.7),
    'O (%)': (37.0, 53.0),
    'S (%)': (0.0, 0.5),
    'VM (%)': (67.0, 88.0),
    'Ash (%)': (0.4, 19.0),
    'FC (%)': (4.5, 27.0),
    'T (°C)': (500, 1300),
    'OC (%)': (10, 60),
    'SBR': (0.5, 5.0)
}

# Create input sliders
user_inputs = {}
for feature, (min_val, max_val) in input_ranges.items():
    user_inputs[feature] = st.sidebar.slider(
        f"Select {feature}",
        min_value=float(min_val),
        max_value=float(max_val),
        value=float((min_val + max_val) / 2),
        step=0.1
    )

# Create prediction button
if st.sidebar.button('Predict Yields'):
    # Prepare input data
    input_data = pd.DataFrame([user_inputs])
    
    # Scale input data
    input_scaled = scaler.transform(input_data)
    
    # Make predictions
    h2_pred = rf_h2.predict(input_scaled)[0]
    char_pred = rf_char.predict(input_scaled)[0]
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("H2 Yield Prediction")
        st.markdown(f"### {h2_pred:.2f} wt.%")
        
    with col2:
        st.info("Char Yield Prediction")
        st.markdown(f"### {char_pred:.2f} wt.%")
    
    # Feature importance
    st.subheader("Feature Importance Analysis")
    
    # Calculate feature importance for both models
    h2_importance = pd.DataFrame({
        'Feature': input_ranges.keys(),
        'Importance': rf_h2.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    char_importance = pd.DataFrame({
        'Feature': input_ranges.keys(),
        'Importance': rf_char.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.write("H2 Yield Feature Importance")
        st.bar_chart(data=h2_importance.set_index('Feature'))
        
    with col4:
        st.write("Char Yield Feature Importance")
        st.bar_chart(data=char_importance.set_index('Feature'))

# Add model performance metrics
st.sidebar.markdown("---")
st.sidebar.markdown("### Model Information")
st.sidebar.write("Random Forest Regressor")
st.sidebar.write("- Number of trees: 100")
st.sidebar.write("- Features used: 10")

# Add instructions
st.markdown("---")
st.markdown("""
### How to Use:
1. Adjust the input parameters using the sliders in the sidebar
2. Click the 'Predict Yields' button to get predictions
3. View the predictions and feature importance analysis
""")

# Add footer with disclaimer
st.markdown("---")
st.markdown("""
*Disclaimer: This is a prediction model based on historical data. 
Actual results may vary depending on specific conditions and circumstances.*
""")
