# import cv2
# import numpy as np
# from PIL import Image
# import screeninfo
# import time

# def display_gif(gif_path):
#     gif = Image.open(gif_path)

#     frames = []
#     try:
#         while True:
#             frame = np.array(gif.convert('RGB'))
#             frames.append(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
#             gif.seek(len(frames))
#     except EOFError:
#         pass

#     screen = screeninfo.get_monitors()[0]
#     screen_width, screen_height = screen.width, screen.height

#     # Calculate display duration in milliseconds
#     display_duration = 3000  # 3 seconds

#     # Capture start time
#     start_time = time.time()

#     while True:
#         for frame in frames:
#             # Resize the frame to cover the entire screen
#             resized_frame = cv2.resize(frame, (screen_width, screen_height))
#             cv2.imshow("Starting JARVIS 2.0", resized_frame)

#             # Check if the display duration has been reached
#             if (time.time() - start_time) * 1000 > display_duration:
#                 cv2.destroyAllWindows()
#                 return  # Exit the function

#             if cv2.waitKey(100) & 0xFF == 27:  # Break if 'Esc' is pressed
#                 cv2.destroyAllWindows()
#                 return  # Exit the function

#     cv2.destroyAllWindows()
