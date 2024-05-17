from tkinter import *
from tkinter import messagebox
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def clear_all() :
    entry_blood_glucose_level.delete(0, END)   
    entry_hba1c_level.delete(0, END) 
    entry_bmi.delete(0, END)
    #entry_smoking_history.delete(0, END)
    entry_heart_disease.delete(0, END)
    entry_hypertension.delete(0, END)
    entry_age.delete(0, END)
    entry_age.focus_set()


# Load the trained model
with open('trained1_model.sav', 'rb') as model_file:
    rfc = pickle.load(model_file)

# Create a function to predict diabetes
def predict_diabetes():
    try:
        age = float(entry_age.get())
        hypertension = int(entry_hypertension.get())
        heart_disease = int(entry_heart_disease.get())
        smoking_history = str(var.get())
        bmi = float(entry_bmi.get())
        hba1c_level = float(entry_hba1c_level.get())
        blood_glucose_level = float(entry_blood_glucose_level.get())

        # Create a DataFrame with the input data
        data = pd.DataFrame({
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'smoking_history': [smoking_history],
            'bmi': [bmi],
            'HbA1c_level': [hba1c_level],
            'blood_glucose_level': [blood_glucose_level]
        })

        # Make the prediction
        prediction = rfc.predict(data)

        print("Input data:", data)
        print("Prediction:", prediction)

        if prediction[0] == 1:
            messagebox.showinfo(title="Diabetic",icon="info",message="Patient is diabetic")
        else:
            messagebox.showinfo(title="Diabetic",icon="info",message="Patient is not diabetic")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Error", "Invalid input. Please check the values.")



# Create the main application window
if __name__ == "__main__" :
    
    root = Tk()  
    var = DoubleVar()  
    # Set the background colour of GUI window 
    root.configure(background = 'light green')   
    # Set the configuration of GUI window 
    root.geometry("420x420")    
    # set the name of tkinter GUI window 
    root.title("Diabetes Calculation")  

    label = Label(root, text = "DIABETICS PREDICTION  ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=40, bg = '#F5F5DC',bd=10,compound='center')
       
   
    label1 = Label(root, text = "Blood glucose level : ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0')
    label2 = Label(root, text = "HbAlc level : ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0')
    label3 = Label(root, text = "BMI : ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0')
    label4 = Label(root, text = "Smoking history:""\n"
                                "0:never""\n"
                                "1:no info""\n"
                                "2:CURRENT""\n"
                                "3:former""\n"
                                "4:Ever""\n"
                                "5:not current", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=20,height=7, bg = '#FFFDD0')
    #labeli = Label(root, text = "Smoking history:  ", relief=RAISED,
                   #font=('Arial',15),fg = 'black',width=20,height= bg = '#FFFDD0')
    
    scale = Scale(root,from_=0,to=5,length=600,orient=HORIZONTAL,tickinterval=1,
                  font=('Arial',15),showvalue=1,troughcolor="#B87333",bg='light green',variable=var)
    
    label5 = Label(root, text = "Heart disease:(0 for No, 1 for Yes) ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0') 
    label6 = Label(root, text = "Hypertension: (0 for No, 1 for Yes)", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0') 
    label7 = Label(root, text = "Age: ", relief=RAISED,
                   font=('Arial',15),fg = 'black',width=30, bg = '#FFFDD0') 
    
    label.grid(row = 1, column = 1, padx = 30, pady = 12)
    label1.grid(row = 2, column = 0, padx = 30, pady = 12)  
    label2.grid(row = 3, column = 0, padx = 30, pady = 12)  
    label3.grid(row = 4, column = 0, padx = 30, pady = 12)
    label4.grid(row = 5, column = 0, padx = 30, pady = 12)
    scale.grid(row = 5, column = 1, padx = 30, pady = 12)
    label5.grid(row = 6, column = 0, padx = 30, pady = 12)
    label6.grid(row = 7, column = 0, padx = 30, pady = 12)
    label7.grid(row = 8, column = 0, padx = 30, pady = 12)
    
    entry_blood_glucose_level = Entry(root,width=50)  
    entry_hba1c_level = Entry(root,width=50)  
    entry_bmi = Entry(root,width=50)
    #entry_smoking_history = Label(root,command=sel)
    entry_heart_disease = Entry(root,width=50)
    entry_hypertension = Entry(root,width=50)
    entry_age = Entry(root,width=50)
    
    entry_blood_glucose_level.grid(row = 2, column = 1, padx = 10, pady = 10)  
    entry_hba1c_level.grid(row = 3, column = 1, padx = 10, pady = 10)  
    entry_bmi.grid(row = 4, column = 1, padx = 10, pady = 10)
    #entry_smoking_history.grid(row = 5, column = 1, padx = 10, pady = 10)
    entry_heart_disease.grid(row = 6, column = 1, padx = 10, pady = 10)
    entry_hypertension.grid(row = 7, column = 1, padx = 10, pady = 10)
    entry_age.grid(row = 8, column = 1, padx = 10, pady = 10)
    
    button1 = Button(root, text = "Submit", bg = "#FFFDD0",bd=20,  
                     width=10,relief=RAISED,font=("Helvetica",15),fg = "black",command=predict_diabetes) 
    button2 = Button(root, text = "Clear", bg = "#FFFDD0",bd=20, 
                     width=10,relief=RAISED,font=("Helvetica",15),fg = "black", command = clear_all)
   
    button1.grid(row = 9, column = 1, pady = 10) 
    button2.grid(row = 10, column = 1, pady = 10)
    
      
    root.mainloop()