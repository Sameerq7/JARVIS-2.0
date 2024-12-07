import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)  # Track only one hand at a time
mp_drawing = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Open webcam
cap = cv2.VideoCapture(0)

scroll_amount = 20      # Fixed scroll amount (can be adjusted)
previous_y = 0          # Store previous y-coordinate for scrolling

while True:
    # Read frames from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert the BGR image to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe
    result = hands.process(rgb_frame)

    # Draw hand landmarks and perform actions
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract the coordinates of the fingers
            index_x = int(hand_landmarks.landmark[8].x * frame_width)
            index_y = int(hand_landmarks.landmark[8].y * frame_height)
            thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
            thumb_y = int(hand_landmarks.landmark[4].y * frame_height)

            # Map coordinates to screen
            mapped_x = screen_width / frame_width * index_x
            mapped_y = screen_height / frame_height * index_y

            # Click Gesture (Thumb and Index finger pressed together)
            if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
                pyautogui.click()
                pyautogui.sleep(0.2)  # Prevent multiple clicks

            # Scroll Up with Index Finger Only
            if abs(index_x - thumb_x) > 50 and abs(index_y - thumb_y) > 50:  # Only Index
                pyautogui.scroll(scroll_amount)

            # Scroll Down with Thumb Only (Thumb-up Symbol)
            elif abs(index_x - thumb_x) < 50 and index_y < thumb_y:  # Only Thumb up
                pyautogui.scroll(-scroll_amount)

            # Move Cursor with Open Hand (All fingers open)
            if all(abs(hand_landmarks.landmark[i].x - hand_landmarks.landmark[i-1].x) > 0.05 for i in [4, 8, 12, 16, 20]):
                pyautogui.moveTo(mapped_x, mapped_y)

    # Display the output
    cv2.imshow("Virtual Mouse", frame)

    # Break loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
