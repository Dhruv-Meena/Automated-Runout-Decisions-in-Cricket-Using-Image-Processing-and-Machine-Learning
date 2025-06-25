# Automated Runout Decisions in Cricket Using Image Processing and Machine Learning

This project aims to automate runout decision-making in cricket using image processing techniques and machine learning algorithms. It analyzes video frames, detects key events like bails dislodging, and determines whether a player is inside or outside the crease at the moment of the runout.

---

## Objective

To reduce human error and increase the speed of decision-making in cricket by automating the detection of runout scenarios through real-time video analysis.

---

## Features

- Extracts and processes video frames using OpenCV
- Detects dislodgement of bails using trained YOLOv8 model
- Determines crease position and player's foot position
- Measures pixel distances to infer timing of runout
- GUI for user to input video and select analysis parameters
- Generates a final decision: **"OUT"** or **"NOT OUT"**

---

## Technologies Used

- Python
- OpenCV
- NumPy
- PIL (Pillow)
- Ultralytics YOLOv8
- Tkinter (GUI)
- Matplotlib (optional for visualization)

---
