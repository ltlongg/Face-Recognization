import cv2
import numpy
import pymysql

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '12345678',
        database = 'face_recognition'
)
if conn.open:
    print("Successfully connected to the database")
def insertOrUpdate(id, name, age):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * from users where id_user = %s"
            results = cursor.execute(query, (id,)) #Trả về số dòng dữ liệu khớp với truy vấn
            if results != 0:
                print('Đã tồn tại người có id = ',id)
                print("Bạn có muốn update (y/n):")
                update = str(input())
                if update == 'y':
                    print("Bạn muốn nhập tên mới (y/n)")
                    update_name = str(input())
                    if update_name == 'y':
                        query = "UPDATE users set name_user = %s where id_user = %s"
                        new_name = str(input('Nhập tên mới: '))
                        cursor.execute(query, (new_name, id))
                        conn.commit()
                    print("Bạn muốn nhập tuổi mới (y/n)")
                    update_age = str(input())
                    if update_age == 'y':
                        query = "UPDATE users set age_user = %s where id_user = %s"
                        new_age = int(input('Nhập tuổi mới: '))
                        cursor.execute(query, (new_age, id))
                        conn.commit() 
                    print("Cập nhật thành công")
                else:
                    print("Không có thay đổi nào được thực hiện")
            else:
                query  = "INSERT INTO users(id_user, name_user, age_user) values(%s, %s, %s)"
                cursor.execute(query, (id, name, age))
                conn.commit()
                print("Thêm mới thành công")
    finally:
        conn.close()
        print("Đã đóng kết nối với cơ sở dữ liệu")
id = str(input('Nhập id: '))
name = str(input('Nhập tên: '))
age = int(input('Nhập tuổi: '))
insertOrUpdate(id, name, age)

count_face = 0
while (True):
    ret, img = cap.read()
    if not ret:
        print('Không thể lấy hình ảnh từ camera')
        break
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(img_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        count_face += 1
        img_face = img_gray[y:y+h, x:x+w]
        img_face = cv2.resize(img_face, (200, 200))
        cv2.imwrite("dataSet/User." + str(id) + "." + str(count_face) + ".jpg", img_face)
        print("Đã thêm ảnh thứ:", count_face)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.waitKey(10)
    cv2.imshow('Face', img)
    if count_face > 30:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()