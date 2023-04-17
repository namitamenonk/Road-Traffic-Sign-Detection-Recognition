# Importing neccessary libraries for the GUI Implementation.

import tkinter as tk                       # GUI Toolkit
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image             # To open image content into an array
from keras.models import load_model        # To load existing model
from gtts import gTTS
import pyttsx3                             # library for text to speech output
import os                                  # To iterate over all the classes 
import numpy

# Load the trained model to classify sign.
model = load_model('Traffic_Sign_AI_Model.h5')

# Dictionary to label all traffic signs class.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

#initialise GUI
top=tk.Tk()
top.geometry('600x400')
top.title('Traffic sign Detection -Final')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', foreground='black',font=('Cambria',20,'bold'))
sign_image = Label(top)
txtsign=""

"""
@desc     Function to predict the traffic sign, ie., converting the image into the dimension of shape
@param    file_path : File path of the image
@return   sign : name of the traffic sign associated with the matching label from classes
"""

def classify(file_path):
    print(file_path)
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    predict_x=model.predict([image])
    print(predict_x)
    classes_x=numpy.argmax(predict_x,axis=1)
    print(classes_x)
    
    sign = classes[classes_x[0]+1]
    print(sign)
    label.configure(foreground='#011638', text=sign)
    return sign

"""
@desc     Function to produce speech output of the traffic sign
@param    txtSign:predicted traffic sign in text format
"""
def speak_sign(txtSign):
    engine = pyttsx3.init()
    engine.say(txtSign)
    engine.runAndWait()
  
"""
@desc     Function to show the classify button and its functionalities
@param    file_path:contains the uploaded image path
"""    
def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda:speak_sign(classify(file_path)),padx=10,pady=5)
    classify_b.configure(background='#000000', foreground='white',font=('Cambria',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    
"""
@desc     Function to upload the image for detection and prediction 
          it will show the thumbnail for the uploaded image in GUI
"""  
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

# Configurations for upload button
upload=Button(top,text="Select Image",command=upload_image,padx=10,pady=5)
upload.configure(background='#000000', foreground='white',font=('Cambria',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)

# Configurations for heading in GUI
heading = Label(top, text="Traffic sign Detection",pady=20, font=('Cambria',20,'bold','underline'))
heading.configure(background='#ffffff',foreground='#ff1100')
heading.pack()
top.mainloop()