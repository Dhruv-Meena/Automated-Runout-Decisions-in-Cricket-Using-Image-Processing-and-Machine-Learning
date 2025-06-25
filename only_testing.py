from ultralytics import YOLO
import cv2

# Load your custom trained YOLOv8 model
model = YOLO(r"C:\Users\dhruv\Desktop\Cricket_Learning\YOLOv8\YOLOv8\best.pt")
# Replace with the path to your trained model
# C:\Users\skapn\cricket_paper_and_code\YOLOv8\runs\detect\yolov8_custom\weights

# # Perform inference on an image
# image_path = "test1.jpg"  # Replace with the path to your image
# results = model(image_path)  # Perform inference

# # Visualize the results
# for result in results:
#     result.show()  # Display the image with bounding boxes
#     result.save("result_image.jpg")  # Save the result image

# Alternatively, you can perform inference on a video
video_path = "trimmed_video3.mp4"  # Replace with the path to your video
cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Visualize the results
    for result in results:
        annotated_frame = result.plot()  # Get the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)  # Display the annotated frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()