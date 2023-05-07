import cv2
face_cap  = cv2.CascadeClassifier("E:/ML/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
video_cap = cv2.VideoCapture(0)
while True :
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle( video_data, (x,y), (x+y,y+h),(0,255,0),2)
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10000) == ord("a"):
        break
    video_cap.release()

# camera enable

# video_cap = cv2.VideoCapture(0)
# while True :
#     ret, video_data = video_cap.read()
#     cv2.imshow("video_live", video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
#     video_cap.release()