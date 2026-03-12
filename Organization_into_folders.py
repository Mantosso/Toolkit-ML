import os
import shutil

SOURCE_FOLDER = r"E:\DOTA\None\images"
BATCH_SIZE = 99               # сколько нужно фоток в одной папке


EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff')

files = [
    f for f in os.listdir(SOURCE_FOLDER)
    if f.lower().endswith(EXTENSIONS) and os.path.isfile(os.path.join(SOURCE_FOLDER, f))
]

files.sort()

total = len(files)
print(f"Найдено {total} изображений.")

for i in range(0, total, BATCH_SIZE):
    batch = files[i:i+BATCH_SIZE]
    folder_name = f"batch_{i//BATCH_SIZE + 1:03d}"
    folder_path = os.path.join(SOURCE_FOLDER, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    for file in batch:
        src = os.path.join(SOURCE_FOLDER, file)
        dst = os.path.join(folder_path, file)
        shutil.move(src, dst)

    print(f"Создана папка {folder_name} — файлов: {len(batch)}")
