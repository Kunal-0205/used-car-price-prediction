
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# Load model and dataset
model = joblib.load("used_car_price_model.pkl")
cars = pd.read_csv("Car Sell Dataset.csv")

# Wine-red styling
st.markdown("""
<style>
.stApp {
    background-color: #1A1015;
    color: #F8F1F4;
}

h1, h2, h3 {
    color: #F8F1F4;
}

div.stButton > button {
    background-color: #722F45;
    color: white;
    border: 1px solid #91445E;
    border-radius: 8px;
    font-weight: bold;
    min-height: 45px;
}

div.stButton > button:hover {
    background-color: #91445E;
    color: white;
    border-color: #B76E85;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #291922;
    border-color: #492735;
    border-radius: 8px;
}

.result-card {
    background: linear-gradient(135deg, #35202B, #241720);
    border: 1px solid #91445E;
    border-radius: 14px;
    padding: 22px;
    margin: 12px 0;
}

.price-label {
    color: #D9A1B4;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.price-value {
    color: #F2C5D3;
    font-size: 36px;
    font-weight: bold;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# Page heading
st.title("🚗 Used Car Price Prediction")
st.caption("Estimate a used car's price using Machine Learning.")
st.divider()

# Two-column layout
left, right = st.columns(2, gap="large")

with left:
    st.subheader("🚘 Car Details")

    brand = st.selectbox(
        "Brand",
        sorted(cars["Brand"].dropna().unique())
    )

    # Show models for the selected brand
    models = sorted(
        cars.loc[
            cars["Brand"] == brand, "Model Name"
        ].dropna().unique()
    )

    model_name = st.selectbox("Model Name", models)

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Manufacturing Year",
            min_value=2000,
            max_value=2023,
            value=2018
        )

    with col2:
        kilometers = st.number_input(
            "Kilometers Driven",
            min_value=10000,
            max_value=179998,
            value=50000,
            step=1000
        )

    fuel = st.selectbox(
        "Fuel Type",
        sorted(cars["Fuel Type"].dropna().unique())
    )

    transmission = st.selectbox(
        "Transmission",
        sorted(cars["Transmission"].dropna().unique())
    )

    predict = st.button(
        "Predict Price",
        use_container_width=True
    )

with right:
    st.subheader("Prediction Result")

    if predict:
        input_data = pd.DataFrame([{
            "Brand": brand,
            "Model Name": model_name,
            "Year": year,
            "Kilometers": kilometers,
            "Fuel Type": fuel,
            "Transmission": transmission
        }])

        try:
            price = model.predict(input_data)[0]

            st.markdown(f"""
            <div class="result-card">
                <div class="price-label">Estimated Price</div>
                <div class="price-value">₹{price:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

            st.write(f"**Car:** {brand} {model_name}")
            st.write(f"**Year:** {year} · **Distance:** {kilometers:,} km")

            st.caption(
                "Actual market prices may vary depending on the car's condition, location, and market demand."
            )

        except Exception as error:
            st.error(f"Prediction failed: {error}")


# Footer
st.divider()
