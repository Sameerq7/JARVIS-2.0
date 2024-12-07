# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize MediaPipe Hand Detector
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)  # Track only one hand at a time
# mp_drawing = mp.solutions.drawing_utils

# # Get screen size
# screen_width, screen_height = pyautogui.size()

# # Open webcam
# cap = cv2.VideoCapture(0)

# scroll_enabled = False  # Track scrolling state
# previous_y = 0          # Store previous y-coordinate for scrolling
# scroll_distance = 0     # Variable to store the distance moved for scrolling
# scroll_amount = 20      # Fixed scroll amount (can be adjusted)

# while True:
#     # Read frames from webcam
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Flip the frame horizontally for a mirror effect
#     frame = cv2.flip(frame, 1)

#     # Get frame dimensions
#     frame_height, frame_width, _ = frame.shape

#     # Convert the BGR image to RGB for Mediapipe
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process the frame with Mediapipe
#     result = hands.process(rgb_frame)

#     # Draw hand landmarks and perform actions
#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Extract index and middle finger coordinates
#             index_x = int(hand_landmarks.landmark[8].x * frame_width)
#             index_y = int(hand_landmarks.landmark[8].y * frame_height)
#             middle_x = int(hand_landmarks.landmark[12].x * frame_width)
#             middle_y = int(hand_landmarks.landmark[12].y * frame_height)

#             # Draw circles on fingers
#             cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
#             cv2.circle(frame, (middle_x, middle_y), 10, (255, 0, 0), -1)

#             # Map coordinates to screen
#             mapped_x = screen_width / frame_width * index_x
#             mapped_y = screen_height / frame_height * index_y

#             # Click Gesture (Index and Thumb fingers close)
#             thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
#             thumb_y = int(hand_landmarks.landmark[4].y * frame_height)
#             if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
#                 pyautogui.click()
#                 pyautogui.sleep(0.2)  # Prevent multiple clicks

#             # Cursor Movement (Only Index Finger moves)
#             pyautogui.moveTo(mapped_x, mapped_y)

#             # Enable scrolling when index and middle fingers are detected
#             if abs(index_x - middle_x) < 50:  # Ensure the index and middle fingers are close
#                 scroll_enabled = True

#                 # Calculate scroll distance
#                 scroll_diff = index_y - previous_y

#                 # Scroll only if there's a significant movement
#                 if abs(scroll_diff) > 10:
#                     if scroll_diff > 10:  # Scroll Down
#                         pyautogui.scroll(-scroll_amount)
#                     elif scroll_diff < -10:  # Scroll Up
#                         pyautogui.scroll(scroll_amount)

#                 # Store the movement for next comparison
#                 previous_y = index_y

#             else:
#                 scroll_enabled = False
#                 previous_y = 0

#     # Display the output
#     cv2.imshow("Virtual Mouse", frame)

#     # Break loop on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
#NEW CODE
# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize MediaPipe Hand Detector
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)  # Track only one hand at a time
# mp_drawing = mp.solutions.drawing_utils

# # Get screen size
# screen_width, screen_height = pyautogui.size()

# # Open webcam
# cap = cv2.VideoCapture(0)

# scroll_enabled = False  # Track scrolling state
# previous_y = 0          # Store previous y-coordinate for scrolling
# scroll_distance = 0     # Variable to store the distance moved for scrolling
# scroll_amount = 20      # Fixed scroll amount (can be adjusted)

# while True:
#     # Read frames from webcam
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Flip the frame horizontally for a mirror effect
#     frame = cv2.flip(frame, 1)

#     # Get frame dimensions
#     frame_height, frame_width, _ = frame.shape

#     # Convert the BGR image to RGB for Mediapipe
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process the frame with Mediapipe
#     result = hands.process(rgb_frame)

#     # Draw hand landmarks and perform actions
#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Extract index, middle, and thumb finger coordinates
#             index_x = int(hand_landmarks.landmark[8].x * frame_width)
#             index_y = int(hand_landmarks.landmark[8].y * frame_height)
#             middle_x = int(hand_landmarks.landmark[12].x * frame_width)
#             middle_y = int(hand_landmarks.landmark[12].y * frame_height)
#             thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
#             thumb_y = int(hand_landmarks.landmark[4].y * frame_height)

#             # Draw circles on fingers
#             cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
#             cv2.circle(frame, (middle_x, middle_y), 10, (255, 0, 0), -1)
#             cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 0, 255), -1)

#             # Map coordinates to screen
#             mapped_x = screen_width / frame_width * index_x
#             mapped_y = screen_height / frame_height * index_y

#             # Click Gesture (Index and Thumb fingers close)
#             if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
#                 pyautogui.click()
#                 pyautogui.sleep(0.2)  # Prevent multiple clicks

#             # Cursor Movement (Only Index Finger moves)
#             pyautogui.moveTo(mapped_x, mapped_y)

#             # Enable scrolling when index and middle fingers are detected
#             if abs(index_x - middle_x) < 50:  # Ensure the index and middle fingers are close
#                 scroll_enabled = True

#                 # Calculate scroll distance
#                 scroll_diff = index_y - previous_y

#                 # Scroll only if there's a significant movement
#                 if abs(scroll_diff) > 10:
#                     if scroll_diff > 10:  # Scroll Down
#                         pyautogui.scroll(-scroll_amount)
#                     elif scroll_diff < -10:  # Scroll Up
#                         pyautogui.scroll(scroll_amount)

#                 # Store the movement for next comparison
#                 previous_y = index_y

#             else:
#                 scroll_enabled = False
#                 previous_y = 0

#             # Continuous scroll down with index and thumb
#             if abs(index_x - thumb_x) < 50 and abs(index_y - thumb_y) < 50:  # Fingers close
#                 pyautogui.scroll(-scroll_amount)

#             # Scroll up with only thumb
#             elif abs(index_x - thumb_x) > 50:  # Only Thumb shown
#                 pyautogui.scroll(scroll_amount)

#     # Display the output
#     cv2.imshow("Virtual Mouse", frame)

#     # Break loop on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
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

scroll_enabled = False  # Track scrolling state
previous_y = 0          # Store previous y-coordinate for scrolling
scroll_distance = 0     # Variable to store the distance moved for scrolling
scroll_amount = 20      # Fixed scroll amount (can be adjusted)

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

            # Extract index and thumb coordinates
            index_x = int(hand_landmarks.landmark[8].x * frame_width)
            index_y = int(hand_landmarks.landmark[8].y * frame_height)
            thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
            thumb_y = int(hand_landmarks.landmark[4].y * frame_height)

            # Draw circles on fingers
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), -1)

            # Map coordinates to screen
            mapped_x = screen_width / frame_width * index_x
            mapped_y = screen_height / frame_height * index_y

            # Click Gesture (Index and Thumb fingers close)
            if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
                pyautogui.click()
                pyautogui.sleep(0.2)  # Prevent multiple clicks

            # Cursor Movement (Only Index Finger moves)
            pyautogui.moveTo(mapped_x, mapped_y)

            # Scroll when index and middle fingers are detected
            if abs(index_x - thumb_x) < 50 and abs(index_y - thumb_y) < 50:  # Fingers close
                scroll_enabled = True

                # Scroll down if index and thumb continuously shown
                pyautogui.scroll(-scroll_amount)

            elif abs(index_x - thumb_x) > 50:  # Only Thumb shown
                # Scroll up when only thumb is visible
                pyautogui.scroll(scroll_amount)

    # Display the output
    cv2.imshow("Virtual Mouse", frame)

    # Break loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
