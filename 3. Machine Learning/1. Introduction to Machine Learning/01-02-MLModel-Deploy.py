import pandas as pd
import numpy as np
import pickle
import streamlit as st
#from PIL import Image
  
f = open('rfc.pkl', 'rb')
rfc = pickle.load(f)
species = {0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'}

def predict():
    st.title("Iris Flower Species Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
      
    sepal_length = st.text_input("Sepal Length", "Type Here")
    sepal_width = st.text_input("Sepal Width", "Type Here")
    petal_length = st.text_input("Petal Length", "Type Here")
    petal_width = st.text_input("Petal Width", "Type Here")
    result =""
      
    if st.button("Predict"):
        result = rfc.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        predicted_species = 'Unknown'
        if result[0] in species.keys():
            predicted_species = species[result[0]]
        st.success('The predicted species is {}'.format(predicted_species))
        #st.success('The Output is {}'.format(result))
    return
    
predict()