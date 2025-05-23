import cv2
import time
import face_recognition


async def capture_face():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb)

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if time.time() - start_time > 6 and len(face_locations) == 1:
            encoding = face_recognition.face_encodings(rgb, face_locations)[0]
            cap.release()
            cv2.destroyAllWindows()
            return encoding
    
    cap.release()
    cv2.destroyAllWindows()
    return None