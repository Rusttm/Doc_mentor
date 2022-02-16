import cv2
print('OpenCV version is ', cv2.__version__)
import os
print('Work directory is ', os.getcwd())
import numpy

CUR_DIR = '/Users/johnlennon/My Drive/Python/Pdf/Murtaza'
IMG_DIR = '/Users/johnlennon/My Drive/Python/Pdf/data/Murtaza_img'
IMG_DIR_TRAIN = '/Users/johnlennon/My Drive/Python/Pdf/data/Murtaza_img/train'
IMG_DIR_TEST = '/Users/johnlennon/My Drive/Python/Pdf/data/Murtaza_img/test'
VIDEO_TEST = '/Users/johnlennon/My Drive/Python/Pdf/data/Murtaza_img/test/IMG_6202.MOV'
orb = cv2.ORB_create(nfeatures=1000)
bf = cv2.BFMatcher()

# img2 = cv2.imread(f'{IMG_DIR_TRAIN}/Phone.jpg')
# kp2, des2 = orb.detectAndCompute(img2, None)
def classes():
    """return dict {classes:[], images: []}"""
    images = []
    typeNames = []
    descriptors = []
    filesList1 = os.listdir(IMG_DIR_TRAIN)
    filesList = [name for name in filesList1 if os.path.splitext(name)[-1]=='.jpg']
    for name in filesList:
        imgCur = cv2.imread(f'{IMG_DIR_TRAIN}/{name}', 0)
        images.append(imgCur)

        typeNames.append(os.path.splitext(name)[0])
        kp, desc = orb.detectAndCompute(imgCur, None)
        descriptors.append(desc)
    return {'classes': typeNames, 'images': images, 'descriptors': descriptors}

images_descriptors = classes()['descriptors']
images_classes = classes()['classes']

def findDes(images = classes()['images']):
    """looks descriptors in images and return descriptor list"""
    desList = []

    for image in images:
        kp, des = orb.detectAndCompute(image, None)
        desList.append(des)
    return desList

def percList(matchList):
    if sum(matchList):
        summ = sum(matchList)
    else:
        summ = 1
    perc_List = []
    max_perc = 0
    answer = 'No matches'
    for i, data in enumerate(matchList):
        perc = int(data*100/summ)
        if perc >= max_perc:
            max_perc = perc
            answer = f'{images_classes[i]}({perc}%)'
        perc_List.append(perc)
    print(answer)
    return answer


def matcher(image):
    kp, des = orb.detectAndCompute(image, None)
    images_descriptors = classes()['descriptors']
    #bf = cv2.BFMatcher()
    matchList = []
    for desc2 in images_descriptors:
        matches = bf.knnMatch(des, desc2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.9 * n.distance:
                good.append(m)
        matchList.append(len(good))
    return percList(matchList)

def capture_the_frame():
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(VIDEO_TEST)
    while True:
        img_text = 'Unknown'
        success, frame = cap.read()
        capImg = frame.copy()
        try:
            img_text = matcher(capImg)
        except Exception as e:
            print(type(capImg))
            #img_text = 'Unknown'
            print('exception', e)
        #im2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.putText(capImg, img_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)

        cv2.imshow('press q for quit', capImg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            #os.chdir(os.getcwd())
            #filename = 'CaptureImage.jpg'
            #print(cv2.imwrite(filename, frame))
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture_the_frame()