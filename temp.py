import dill
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_models = dill.load(open('C:/Users/y/Downloads/saved models/diabetes_model.sav', 'rb'))
hearts_models = dill.load(open('C:/Users/y/Downloads/saved models/heart_disease_model.sav', 'rb'))
parkinsons_models = dill.load(open('C:/Users/y/Downloads/saved models/parkinsons_model.sav', 'rb'))




#streamlit run C:\Users\y\Downloads\mdps\temp.py

with st.sidebar:
    selected = option_menu('multiple disease prediction system',
                           ['diabetes prediction','heart disease prediction',
                            'parkinsons disease'],
                           icons= ['activity','heart','person'],
                           default_index=0)


if (selected == 'diabetes prediction'):
    st.title('diabetes prediction')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
            Pregnancies = st.text_input('number of pregnancies')
        
    with col2:
        Glucose= st.text_input('glucose level')
    with col3:
        BloodPressure =  st.text_input('blood pressure')
    with col1:
        SkinThickness= st.text_input('skin thickness')
        
    with col2:
        Insulin= st.text_input('insulin')
        
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('diabetes pedigree function')
    with col2:
        Age=  st.text_input('age of the person')
        
        
        
        
        
   
  
    
   
    
    
    diab_diagnosis = ''
    
    if st.button('diabetes test result'):
        diab_prediction = diabetes_models.predict([[Pregnancies, Glucose, BloodPressure,
                                                    SkinThickness, Insulin, BMI,
                                                    DiabetesPedigreeFunction, Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis= " The person is diabetic"
        else:
            diab_diagnosis = " The person is not diabetic"
    st.success(diab_diagnosis)
    
    

if (selected == 'heart disease prediction'):
    st.title('heart disease prediction')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
         age = st.text_input('Age')     
    with col2:
        sex= st.text_input('Sex')
    with col3:
        cp =  st.text_input('chest pain')
    with col1:
        treastbps= st.text_input('Resting Blood pressure')
        
    with col2:
        chol = st.text_input('serum cholerstrol  in mg/dl')
        
    with col3:
        fbs= st.text_input('fasting blood sugar >120 mg/dl')
    with col1:
         restecg= st.text_input('resting elctrocardiographic results')
    with col2:
        thalach=  st.text_input('maximum heart rate achieved')
    with col3:
        exang=  st.text_input('exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope= st.text_input('the slope of the peak exercise ST segment')
    with col3:
        ca =  st.text_input('ca ')
        
	
    with col1:
        thal =  st.text_input('number of major vessels (0-3) colored by flourosopy')
        
        
    heart_diagnosis = ''
    
    if st.button('heart test result'):
        heart_prediction = hearts_models.predict([[age, sex, cp,
                                                    treastbps, chol, fbs,
                                                    restecg, thalach, exang,
                                                   oldpeak, slope, ca,thal ]])
        if(heart_prediction[0]==1):
            heart_diagnosis= " The person has heat disease"
        else:
            heart_diagnosis = " The person does not heart disease"
    st.success(heart_diagnosis)   
        
    
    

if (selected == 'parkinsons disease'):
    st.title('parkinsons disease')
    col1,col2,col3 = st.columns(3)
    
    with col1:
         fo = st.text_input('MDVP:Fo(Hz)')     
    with col2:
        fhi= st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo =  st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter_percent= st.text_input('MDVP:Jitter(%)')
        
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP= st.text_input('MDVP:RAP')
    with col1:
         PPQ= st.text_input('MDVP:PPQ')
    with col2:
        DDP=  st.text_input('Jitter:DDP')
    with col3:
        shimmer=  st.text_input('MDVP:Shimmer')
    with col1:
        shimmer_dB = st.text_input('Shimmer,MDVP:Shimmer(dB)')
        
    with col2:
        APQ3= st.text_input('Shimmer:APQ3')
    with col3:
        APQ5 =  st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA= st.text_input('Shimmer:DDA')
    with col3:
        NHR =  st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE= st.text_input('RPDE')
 
    with col3:
        DFA =  st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
        
    with col2:
        spread2= st.text_input('spread2')
    with col3:
        D2 =  st.text_input('D2')
              
    with col1:
        PPE = st.text_input('PPE')
        
  
        
        
    parkinsons_diagnosis = ''
    
    if st.button('parkinsons test result'):
       parkinsons_prediction = parkinsons_models.predict([[fo, fhi, flo,
                                                      Jitter_percent,  
                                                      Jitter_Abs,RAP,PPQ,DDP,
                                                      shimmer,
                                                      shimmer_dB,APQ3,
                                                      APQ5, APQ, DDA,
                                                      NHR,HNR,RPDE,
                                                       DFA, spread1,
                                                      spread2,D2,PPE]])
       if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis= " The person has parkinsons"
       else:
            parkinsons_diagnosis = " The person does not has parkinsons"
    st.success(parkinsons_diagnosis)   
        
    

    