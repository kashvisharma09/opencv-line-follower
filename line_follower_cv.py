"""
Vision-based line follower - Step 1 (software only)
Detects a dark line (e.g. black tape) on a light background using a webcam,
and prints/displays a steering direction (LEFT / RIGHT / FORWARD).

Controls:
    q - quit
"""

import cv2


def detect_line(frame):
    """Convert frame to a binary threshold image and find contours."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # THRESH_BINARY_INV: dark line becomes white (255), background becomes black (0)
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return thresh, contours


def get_steering_direction(cx, frame_width, tolerance=30):
    """Compare the line's centroid x-position to the frame center."""
    center = frame_width // 2
    if cx < center - tolerance:
        return "LEFT"
    elif cx > center + tolerance:
        return "RIGHT"
    else:
        return "FORWARD"


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam. Check the camera index or permissions.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        frame = cv2.resize(frame, (640, 480))
        thresh, contours = detect_line(frame)

        direction = "NO LINE"
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 500:  # filter out small noise blobs
                moments = cv2.moments(largest)
                if moments["m00"] != 0:
                    cx = int(moments["m10"] / moments["m00"])
                    cy = int(moments["m01"] / moments["m00"])
                    direction = get_steering_direction(cx, frame.shape[1])

                    cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)
                    cv2.drawContours(frame, [largest], -1, (255, 0, 0), 2)

        # Draw center reference line
        cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 0, 255), 1)
        cv2.putText(frame, f"Direction: {direction}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Line Follower - Camera Feed", frame)
        cv2.imshow("Threshold View", thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()