#predict and send
import pickle
import os.path
import cv2
file_path='okepic.jpg'

#    from keras.models import model_from_json
#
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# load weights into new model
#    loaded_model.load_weights("model.h5")
#    if(cv2.imread('okEpic.jpg')):
#        y_pred=loaded_model.predict('okEpic.jpg')
#        with open('predict_1', 'wb') as f:
#            pickle.dump(your_content, f)
#        

while(1):
    if(os.path.exists(file_path)):
      
        img = cv2.imread('okepic.jpg')
       
     
        img = cv2.resize(img, (64, 64))
            
        img = img.reshape((-1, 64, 64, 3))
        y_pred = loaded_model.predict(img)

        with open('predict_1.pickle', 'wb') as f:
            pickle.dump(y_pred, f)
   
    else:
        continue
        
        


while(1):
    if(os.path.exists(file_path)):

        print('gulab')
        break
    else:
            print('galib')