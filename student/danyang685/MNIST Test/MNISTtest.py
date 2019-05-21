import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

img = cv2.imread("enhancedPic.jpg")
img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
cv2.waitKey(0)
picSize = img.shape
smallW = int(picSize[1]/4)
smallH = int(picSize[0]/2)
for i in range(2):
    for j in range(4):
        imgSlice = img[smallH*i:smallH*i+smallH,
                       smallW*j:smallW*j+smallW]  # sliced small pic
        filename = "slicedPic{}_{}.jpg".format(i, j)
        cv2.rectangle(img, (smallW*j, smallH*i), (smallW*j+smallW,
                                                  smallH*i+smallH), (0, 128, 128), 3)  # draw boundary rectangle
        cv2.imwrite(filename, imgSlice)
cv2.waitKey(0)
cv2.destroyAllWindows()


# pre process
for i in range(2):
    for j in range(4):
        rawImg = cv2.imread("slicedPic{}_{}.jpg".format(i, j))
        img = cv2.cvtColor(rawImg, cv2.COLOR_BGR2GRAY)
        # img = cv2.GaussianBlur(img, (2, 2), 10)#gauss morph
        ret, thresholdedImg = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY)

        validShape = [0, 0, 0, 0]

        okFlag = False
        for y in range(thresholdedImg.shape[0]):
            if okFlag:
                break
            for x in range(thresholdedImg.shape[1]):
                if thresholdedImg[y, x] != 255:
                    validShape[0] = y
                    okFlag = True
                    break
        okFlag = False
        for y in range(thresholdedImg.shape[0]-1, -1, -1):
            if okFlag:
                break
            for x in range(thresholdedImg.shape[1]):
                if thresholdedImg[y, x] != 255:
                    validShape[1] = y
                    okFlag = True
                    break
        okFlag = False
        for x in range(thresholdedImg.shape[1]):
            if okFlag:
                break
            for y in range(thresholdedImg.shape[0]):
                if thresholdedImg[y, x] != 255:
                    validShape[2] = x
                    okFlag = True
                    break
        okFlag = False
        for x in range(thresholdedImg.shape[1]-1, -1, -1):
            if okFlag:
                break
            for y in range(thresholdedImg.shape[0]):
                if thresholdedImg[y, x] != 255:
                    validShape[3] = x
                    okFlag = True
                    break

        boxHalfSize = int(max(
            validShape[1]-validShape[0], validShape[3]-validShape[2])*1.5/2)  # set 30% margin
        boxCenter = (int((validShape[1]+validShape[0])/2),
                     int((validShape[3]+validShape[2])/2))

        limitedImg = thresholdedImg[boxCenter[0]-boxHalfSize:boxCenter[0] +
                                    boxHalfSize, boxCenter[1]-boxHalfSize:boxCenter[1]+boxHalfSize]

        resized_image = ~cv2.resize(limitedImg, (28, 28))
        outFilename = "slicedPic{}_{}mono.jpg".format(i, j)
        cv2.imwrite(outFilename, resized_image)



dafaultstderr = sys.stderr
nullstderr=open(os.devnull, 'w')

print('loading Keras')
sys.stderr =nullstderr
from keras.models import load_model
sys.stderr = dafaultstderr

print('loading model')
sys.stderr =nullstderr
model = load_model('mnistModel.h5')
sys.stderr = dafaultstderr
X_pred = np.zeros(shape=(8, 28, 28))
index = 0
for i in range(2):
    for j in range(4):
        img = cv2.imread("slicedPic{}_{}mono.jpg".format(i, j))
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        X_pred[index] = cv2.resize(imgGray, (28, 28))
        index += 1

X_test = X_pred.reshape(8, 784).astype('float32') / 255
y_test = [1, 2, 3, 4, 5, 6, 7, 8]


print('pridicting...')
sys.stderr =nullstderr
y_predict = model.predict_classes(X_test)
sys.stderr = dafaultstderr
correctCount = len(np.nonzero(y_predict == y_test)[0])
print('correct:{},total:{},percentage:{:.1f}%'.format(
    correctCount, len(y_predict), 100*correctCount/len(y_predict)))
