import cv2 # OpenCV library for computer vision tasks like video processing.
import cvzone # cvzone library provides helper functions for computer vision projects.
from cvzone.FaceMeshModule import FaceMeshDetector # Imports FaceMeshDetector for face and landmark detection.
from cvzone.PlotModule import LivePlot # Imports LivePlot for real-time data visualization.

# Initialize video capture.
# To use an external camera, replace '0' with the appropriate camera index.
# '0' typically refers to the default webcam, '1' or higher for external cameras.
cap = cv2.VideoCapture(0) # Changed to 0 for default/external camera input

detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640, 360, [20,50], invert=True)

idList = [22,23,24,26,110,157,158,159,160,161,130,243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255,0,255)

while True:
    
    # If using a video file, this part would loop it.
    # For live camera feed, this check is not strictly necessary but harmless.
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    success, img = cap.read()
    
    if not success:
        print("Failed to read camera frame. Exiting program.") # Changed message for camera
        break

    img, faces = detector.findFaceMesh(img, draw=False)
    
    if faces : 
        face = faces[0]
        
        for id in idList :
            cv2.circle(img, face[id], 5, color, cv2.FILLED)
            
            
        leftUp = face[159]
        leftDown = face[23]
        
        leftLeft = face[130]
        leftRight = face[243]
        
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)
        
        cv2.line(img, leftUp, leftDown, (0,200,0), 3)
        cv2.line(img, leftLeft, leftRight, (0,200,0), 3)
        
        ratio = int((lenghtVer/lenghtHor) * 100)
        ratioList.append(ratio)
        
        if len(ratioList) > 3 :
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)
        
        if ratioAvg < 35 and counter == 0:
            blinkCounter += 1
            counter = 1
            color = (0,200,0)
            
        if counter != 0 :
            counter += 1
            if counter > 10 :
                counter = 0
                color = (255,0,255)
            
        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50,100), colorR=color)
        
        imgPlot = plotY.update(ratioAvg, color)
        
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
        
    else : 
        
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1) 
        
    cv2.imshow("Image", imgStack)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()