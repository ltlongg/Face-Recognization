from PIL import Image
import numpy as np
import cv2
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
imgs_path = [os.path.join('D:/Face Recognition/dataSet', f) for f in os.listdir('D:/Face Recognition/dataSet')]

imgs = []
ids = []
for img_path in imgs_path:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # print(img.shape)
    # print(type(img))
    id = int(img_path.split('.')[1])
    imgs.append(img)
    ids.append(id)
recognizer.train(imgs, np.array(ids))
print("Train thành công")
recognizer.save('trainer.yml')