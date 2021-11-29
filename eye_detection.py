# import asyncio
# from scipy.spatial import distance as dist
# from imutils.video import VideoStream
# from imutils import face_utils
# from threading import Thread
# import threading
# import numpy as np
# import argparse
# import imutils
# from time import *
# import threading
# import dlib
# import cv2
# from pygame import mixer
# import os
#
# freq = 1000
# duration = 1000
#
# def all_functions():
#     global alarm_status
#     global alarm_status2
#     global saying
#
#     def alarm(msg):
#
#         while alarm_status:
#             global myTimer
#             myTimer = 5
#             mixer.init()
#             mixer.music.load('Alarm-ringtone.mp3')
#             mixer.music.set_volume(0.7)
#
#             for x in range(5):
#                 myTimer = myTimer - 1
#                 sleep(1)
#             print('Alerting🔔')
#             mixer.music.play(freq, duration)
#
#         if alarm_status2:
#             print('call2')
#             mixer.music.play(freq, duration)
#
#     def eye_aspect_ratio(eye):
#         A = dist.euclidean(eye[1], eye[5])
#         B = dist.euclidean(eye[2], eye[4])
#         C = dist.euclidean(eye[0], eye[3])
#         ear = (A + B) / (2.0 * C)
#         return ear
#
#     def final_ear(shape):
#         (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
#         (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
#         leftEye = shape[lStart:lEnd]
#         rightEye = shape[rStart:rEnd]
#         leftEAR = eye_aspect_ratio(leftEye)
#         rightEAR = eye_aspect_ratio(rightEye)
#         ear = (leftEAR + rightEAR) / 2.0
#         return (ear, leftEye, rightEye)
#
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-w", "--webcam", type=int, default=0,
#                     help="index of webcam on system")
#     args = vars(ap.parse_args())
#     EYE_AR_THRESH = 0.3
#     EYE_AR_CONSEC_FRAMES = 30
#     YAWN_THRESH = 50
#     alarm_status = False
#     alarm_status2 = False
#     saying = False
#     COUNTER = 0
#     print("-> Loading the predictor and detector...")
#     # detector = dlib.get_frontal_face_detector()
#     detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Faster but less accurate
#     predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#     print("-> Starting Video Stream")
#     vs = VideoStream(src=args["webcam"]).start()
#     # vs= VideoStream(usePiCamera=True).start()       //For Raspberry Pi
#     sleep(1.0)
#     while True:
#         frame = vs.read()
#         frame = imutils.resize(frame, width=450)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         rects = detector.detectMultiScale(gray, scaleFactor=1.1,
#                                           minNeighbors=5, minSize=(30, 30),
#                                           flags=cv2.CASCADE_SCALE_IMAGE)
#         # for rect in rects:
#         for (x, y, w, h) in rects:
#             rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
#             shape = predictor(gray, rect)
#             shape = face_utils.shape_to_np(shape)
#             eye = final_ear(shape)
#             ear = eye[0]
#             leftEye = eye[1]
#             rightEye = eye[2]
#             leftEyeHull = cv2.convexHull(leftEye)
#             rightEyeHull = cv2.convexHull(rightEye)
#             cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
#             cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
#             lip = shape[48:60]
#             # cv2.drawContours(frame, [lip], -1, (0, 0, 255), 1)
#             if ear < EYE_AR_THRESH:
#                 COUNTER += 1
#                 if COUNTER >= EYE_AR_CONSEC_FRAMES:
#                     if alarm_status == False:
#                         alarm_status = True
#                         t = Thread(target=alarm, args=('wake up sir',))
#                         t.deamon = True
#                         t.start()
#                     cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             else:
#                 COUNTER = 0
#                 alarm_status = False
#             cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         cv2.imshow("Sleep Detector", frame)
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord("q"):
#             break
#     cv2.destroyAllWindows()
#     vs.stop()
#
#
################
import asyncio

from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import threading
import winsound
# from win10toast import ToastNotifier
import numpy as np
import argparse
import imutils
from time import *
import threading
import dlib
import cv2
import os
def all():
    freq = 1000  # THE FREQ OF BEEP SOUND
    duration = 1000  # FOR HOW LONG IN WILL KEEP GOING EVERY TIME
    global alarm_status
    global alarm_status2
    global saying

    def alarm(msg):

        while alarm_status:
            global myTimer
            myTimer = 5
            for x in range(5):
                myTimer = myTimer - 1
                sleep(1)
            print('Alerting🔔')
            winsound.Beep(freq, duration)

        if alarm_status2:
            print('call2')
            winsound.Beep(freq, duration)


    def eye_aspect_ratio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        C = dist.euclidean(eye[0], eye[3])

        ear = (A + B) / (2.0 * C)

        return ear


    def final_ear(shape):
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0
        return (ear, leftEye, rightEye)


    ap = argparse.ArgumentParser()
    ap.add_argument("-w", "--webcam", type=int, default=0,
                    help="index of webcam on system")
    args = vars(ap.parse_args())

    EYE_AR_THRESH = 0.3
    EYE_AR_CONSEC_FRAMES = 30
    YAWN_THRESH = 50
    alarm_status = False
    alarm_status2 = False
    saying = False
    COUNTER = 0

    print("-> Loading the predictor and detector...")
    # detector = dlib.get_frontal_face_detector()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Faster but less accurate
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    print("-> Starting Video Stream")
    vs = VideoStream(src=args["webcam"]).start()
    # vs= VideoStream(usePiCamera=True).start()       //For Raspberry Pi
    sleep(1.0)

    while True:

        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

        # for rect in rects:
        for (x, y, w, h) in rects:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            eye = final_ear(shape)
            ear = eye[0]
            leftEye = eye[1]
            rightEye = eye[2]
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            lip = shape[48:60]
            # cv2.drawContours(frame, [lip], -1, (0, 0, 255), 1)

            if ear < EYE_AR_THRESH:
                COUNTER += 1

                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    if alarm_status == False:
                        alarm_status = True
                        t = Thread(target=alarm, args=('wake up sir',))
                        t.deamon = True
                        t.start()

                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            else:
                COUNTER = 0
                alarm_status = False
            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()