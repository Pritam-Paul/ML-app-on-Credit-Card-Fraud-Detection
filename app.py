import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
sns.set_theme(style="darkgrid")
from random import seed,sample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier # Random forest tree algorithm
from sklearn.metrics import average_precision_score
import pickle
import streamlit as st

pickle_in = open('random_forest_regression_model.pkl','rb')
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def fraud_detection_system(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest,type_CASH_OUT,type_TRANSFER):
    errorbalanceOrg = float(newbalanceOrig) + float(amount) - float(oldbalanceOrg)
    errorbalanceDest = float(oldbalanceDest) + float(amount) - float(newbalanceDest)
    #errorbalanceOrg = 2566.60
    #errorbalanceDest = 145666
    HourOfDay = int(step) % 24
    prediction = classifier.predict([[step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest, errorbalanceOrg, errorbalanceDest, HourOfDay, type_CASH_OUT, type_TRANSFER]])
    print(prediction)
    return prediction



def main():
    type_CASH_OUT = 0
    type_TRANSFER = 0
    st.title("Credit Card Fraud Detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fraud Detection ML App by Pritam Paul </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    Type = st.selectbox('Select Type of Transaction:',
                                ('Select','Cash Out', 'Transfer'))
    st.write('You selected:', Type)
    if Type == 'Cash Out':
        type_CASH_OUT = 1
    elif Type == 'Transfer':
        type_TRANSFER = 1

    step= st.text_input('Step',"Type Number Here")
    amount = st.text_input('Amount','Type Number Here')
    oldbalanceOrg = st.text_input('Old Balance of Origin','Type Number Here')
    newbalanceOrig = st.text_input('New Balance of Origin','Type Number Here')
    oldbalanceDest = st.text_input('Old Balance of Destination','Type Number Here')
    newbalanceDest = st.text_input('New Balance of Destination', 'Type Number Here')



    result = ' '
    if st.button("Predict"):
        result = fraud_detection_system(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, type_CASH_OUT,type_TRANSFER)
        if result == 0:
            st.success('The transaction is Valid')
        else:
            st.success('The transaction is Fraud')
if __name__=='__main__':
        main()