# OpenCV Line Follower (Vision-Based)

A real-time computer vision system that detects a dark line (e.g. black tape) against a light background using a webcam, and determines a steering direction (LEFT / RIGHT / FORWARD) based on the line's position relative to the center of the frame.

This is the software-only foundation for a vision-based line-following robot — built as a natural extension of an earlier IR-sensor-based autonomous buggy project, replacing physical sensors with a camera-driven control signal.

## How it works

1. Captures live video from a webcam using OpenCV
2. Converts each frame to grayscale and applies Gaussian blur to reduce noise
3. Applies binary thresholding to isolate dark regions (the line) from the light background
4. Finds contours in the thresholded image and selects the largest one (the line)
5. Computes the line's centroid using image moments
6. Compares the centroid's horizontal position to the frame's center to determine a steering direction
7. Displays the live feed with the detected contour, centroid, and direction label overlaid, alongside a threshold view for debugging

## Demo 
![Line follower detecting a line and outputting FORWARD direction]
(line_follower_demo.png)

*The system detecting the line's contour (blue outline) and centroid (green dot), with the computed steering direction shown in the top-left corner.*

## Tech Stack

- Python
- OpenCV (`opencv-python`)
- NumPy

## Setup

1. Clone this repository:
```bash
   git clone <your-repo-url>
   cd opencv-line-follower
```

2. Install dependencies:
```bash
   pip install opencv-python numpy
```

3. Run the script:
```bash
   python line_follower_cv.py
```

4. Press `q` at any time to quit.

## Usage Notes

- Works best with a clear contrast between the line and the background (e.g. black tape on white paper).
- The threshold sensitivity can be adjusted in `detect_line()` — lower the threshold value if the line isn't being detected, raise it if background clutter is being picked up as the line.
- Two windows are shown while running: the main camera feed with overlays, and a black-and-white threshold view for debugging what the algorithm is actually seeing.

## Next Steps

- Test and tune detection on curved paths, not just straight lines
- Improve robustness with adaptive thresholding for varying lighting conditions
- Integrate with microcontroller hardware (e.g. Arduino) via serial communication to drive an actual robot based on the detected direction

## Background

This project builds on an earlier Engineering Design Project (Arduino-based autonomous RoboCar using IR line-following sensors), extending the same directional control concept into computer vision.