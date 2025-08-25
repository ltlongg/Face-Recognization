import cv2
import numpy as np
import pymysql

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678',
    database = 'face_recognition'

)
def get_profile(id):
    with conn.cursor() as cursor:
        query = 'SELECT * FROM users WHERE id_user = %s'
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read() 
    if not ret:
        print("Không thể mở webcam")
        break
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(img_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img_face = img_gray[y:y+h, x:x+w]
        img_face = cv2.resize(img_face,(200,200))
        img_face_roi = cv2.equalizeHist(img_face)
        id, conf = recognizer.predict(img_face_roi)
        print("Đang dự đoán....")
        profile = get_profile(id)
        if profile != None:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            text = f"{profile[0], profile[2]}"
            cv2.putText(frame, text, (x+5,y-10), cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0,0,255), thickness=1)
    cv2.imshow("Prediction", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
conn.close()
cam.release()
cv2.destroyAllWindows()
print("Webcam đóng")
