import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import random as random

# open camera
# vid = cv2.VideoCapture(0)

# initialize mediapipe
classNames = ['okay', 'peace', 'thumbs up', 'thumbs down', 'call me', 'stop', 'rock', 'live long', 'fist', 'smile']


def generate_random_ges():
    random_ges = random.choice(classNames)
    return random_ges


def generate_gesture():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7,
                          max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils

    model = load_model('hand-gesture-recognition-code/mp_hand_gesture')

    # randomly generate a sequence of gestures
    random_ges = generate_random_ges()

    # Initialize the webcam for Hand Gesture Recognition Python project
    cap = cv2.VideoCapture(0)
    flag = 0
    while True:

        # Read each frame from the webcam
        val, frame = cap.read()
        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)

        # release the webcam and destroy all active windows

        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Get hand landmark prediction
        result = hands.process(framergb)
        # result = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # print(result.multi_hand_landmarks)

        className = ''

        mp_drawing_styles = mp.solutions.drawing_styles

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)
                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
                # mpDraw.plot_landmarks(handslms, mpHands.HAND_CONNECTIONS, azimuth=5)

                for i in range(3):
                    # Predict gesture in Hand Gesture Recognition project
                    prediction = model.predict([landmarks])
                    classID = np.argmax(prediction)
                    className = classNames[classID]
                    # show the prediction on the frame
                    cv2.putText(frame, random_ges, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    print(className, random_ges)
                    if className == random_ges:
                        cv2.putText(frame, 'True', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        random_ges = generate_random_ges()
                        flag += 1
                    else:
                        cv2.putText(frame, 'False', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        print(flag)
        # Show the final output
        cv2.imshow("Hand gesture game", frame)
        if cv2.waitKey(1) == ord('q'):
            break
        if flag == 3:
            break

    cap.release()
    cv2.destroyAllWindows()
