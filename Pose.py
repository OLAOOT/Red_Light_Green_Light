import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

webcam = cv2.VideoCapture(0)

prevTime = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    enable_segmentation=True
) as pose:
  while webcam.isOpened():
    success, image = webcam.read()
    if not success:
      print('error')
      continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
    )

    cv2.imshow('Squid Game', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break

webcam.release()