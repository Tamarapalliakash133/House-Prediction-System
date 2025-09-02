import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
a=pd.DataFrame({
    "size":[100,364,343,499,256,567],
    "rooms":[1,2,3,2,3,3],
    "price":[50000,76000,56572,535234,78687,98987]
    })

x = a[["size","rooms"]]
y = a["price"]

lin = LinearRegression()
lin.fit(x,y)

st.title("🏠 house prediction app")
st.write("Adjust the slider for predecting house")


siz = st.slider("house size(sqft)",min_value = 100,max_value = 580,value = 250)
room = st.slider("no of rooms",min_value = 1,max_value = 3,value = 2)

if st.button("predict_button"):
    final = lin.predict([[siz,room]])[0]
    st.success(f"predicted house value is{round(final)}")

