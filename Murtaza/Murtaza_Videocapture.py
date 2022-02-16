#this module capture image from cam and write in in folder
import cv2
import os

def capture_the_frame():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        cv2.imshow('frame, press q to quit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            os.chdir(os.getcwd())
            filename = 'CaptureImage.jpg'
            print(cv2.imwrite(filename, frame))
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_the_frame()