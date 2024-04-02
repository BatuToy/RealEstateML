# Includes the predict function in here :
 
import joblib

def predict(housing):
    rf = joblib.load('rf_model.sav')
    return rf.predict(housing)