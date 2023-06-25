def cargar_imagenes_entrenamiento(directorio):
    caras = []
    etiquetas = []
    nombres = []
    etiqueta_actual = 0

    for nombre_usuario in os.listdir(directorio):
        etiqueta_actual += 1
        nombres.append(nombre_usuario)

        for imagen_nombre in os.listdir(f"{directorio}/{nombre_usuario}"):
            imagen = cv2.imread(f"{directorio}/{nombre_usuario}/{imagen_nombre}")
            imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            caras.append(imagen_gris)
            etiquetas.append(etiqueta_actual)

    return caras, etiquetas, nombres

def entrenar_reconocedor(caras_entrenamiento, etiquetas_entrenamiento):
    reconocedor = cv2.face.EigenFaceRecognizer_create()
    reconocedor.train(caras_entrenamiento, np.array(etiquetas_entrenamiento))
    return reconocedor

def reconocer_caras(reconocedor, nombres, imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    caras_detectadas = detector.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in caras_detectadas:
        cara_roi = imagen_gris[y:y+h, x:x+w]
        etiqueta, confianza = reconocedor.predict(cara_roi)

        if confianza < 100:
            nombre = nombres[etiqueta]
        else:
            nombre = "Desconocido"

        cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imagen, nombre, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return imagen

def reconocimiento_facial():
    directorio_entrenamiento = "ruta/a/directorio_entrenamiento"
    caras_entrenamiento, etiquetas_entrenamiento, nombres = cargar_imagenes_entrenamiento(directorio_entrenamiento)

    reconocedor = entrenar_reconocedor(caras_entrenamiento, etiquetas_entrenamiento)

    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video_captura = cv2.VideoCapture(0)

    while True:
        ret, imagen = video_captura.read()