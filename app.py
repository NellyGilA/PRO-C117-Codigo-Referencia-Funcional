from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    print("Entró a predict-emotion")   # 👈 DEBUG
    print("JSON recibido:", request.json)  # 👈 DEBUG

    # Obtener el texto ingresado del requerimiento POST.
    input_text = request.json.get("text")  
    
    print("Texto recibido:", input_text)  # 👈 DEBUG

    if not input_text:
        # Respuesta para enviar si input_text está indefinido.
        response = {
                    "status": "error",
                    "message": "¡Por favor, ingresa algún texto para predecir la emoción!"
                  }
        return jsonify(response)
    else:  
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        
        # Respuesta para enviar si input_text no está indefinido.
        response = {
                    "status": "success",
                    "data": {
                            "predicted_emotion": predicted_emotion,
                            "predicted_emotion_img_url": predicted_emotion_img_url
                            }  
                   }

        # Enviar respuesta.         
        return jsonify(response)
       
app.run(debug=True)



    