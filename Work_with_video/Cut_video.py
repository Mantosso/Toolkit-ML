import cv2
import os

video_path = r"D:\DS\video\video\watermarked_preview.mp4"
output_dir = r"D:\DS\video\Start"

start_time = 0      # секунда начала
end_time = 12       # секунда конца
interval = 0.8        # каждые N секунд

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
start_frame = int(start_time * fps)
end_frame = int(end_time * fps)
step_frames = int(interval * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

frame_id = start_frame
img_id = 0


def get_unique_filename(directory, base_name, ext):
    filename = f"{base_name}{ext}"
    full_path = os.path.join(directory, filename)

    if not os.path.exists(full_path):
        return full_path

    counter = 1
    while True:
        filename = f"{base_name}_{counter}{ext}"
        full_path = os.path.join(directory, filename)
        if not os.path.exists(full_path):
            return full_path
        counter += 1


while frame_id <= end_frame:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = cap.read()
    if not ret:
        break

    base_name = f"frame_{img_id:04d}"
    filename = get_unique_filename(output_dir, base_name, ".png")

    cv2.imwrite(filename, frame)  # PNG — без потерь
    img_id += 1
    frame_id += step_frames

cap.release()
