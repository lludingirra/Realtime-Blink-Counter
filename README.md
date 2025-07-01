# Blink Detection with Face Mesh and Live Plot

This project uses **OpenCV**, **cvzone**, and **FaceMesh** to detect face landmarks and count eye blinks in real time via webcam. It also visualizes the eye aspect ratio dynamically using a live plot.

---

## 📦 Features

- Real-time face landmark detection  
- Automatic eye blink detection based on eye aspect ratio  
- Live plotting of eye aspect ratio data  
- Simple and efficient user interface with `cvzone`  
- Works with your default webcam (can be switched to external cameras)  

---

## 🛠️ Requirements

Make sure you have the following libraries installed:

```bash
pip install opencv-python
pip install mediapipe
pip install cvzone
```

**Note:** `cvzone` includes the required `mediapipe` dependency for face mesh detection.

---

## 🚀 How to Run

Run the Python file with:

```bash
python BlinkCounter.py
```

The default webcam will be used. To use a different camera, change this line:

```python
cap = cv2.VideoCapture(0)  # Change '0' to another camera index if needed
```

---

## 🎯 How It Works

- The program uses **FaceMeshDetector** to detect face landmarks.
- Specific eye-related landmarks are tracked.
- Vertical and horizontal distances between landmarks are calculated.
- An eye aspect ratio is computed and tracked over time.
- If the ratio drops below a certain threshold, a blink is detected.
- A real-time plot displays the ratio for visual feedback.

---

## 🎒 Acknowledgments

This project is built using:

- [OpenCV](https://opencv.org/)
- [cvzone](https://github.com/cvzone/cvzone)
- [MediaPipe](https://mediapipe.dev/)

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or contact me.
