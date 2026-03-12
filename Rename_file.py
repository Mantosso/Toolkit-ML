import os
import shutil
from PIL import Image


SRC_IMAGES = r"G:\DS\images"
SRC_LABELS = r"G:\DS\labels"

DST_IMAGES = r"G:\DS\images_y"
DST_LABELS = r"G:\DS\labels_y"

START_NUMBER = 10146
PREFIX = "P"

os.makedirs(DST_IMAGES, exist_ok=True)
os.makedirs(DST_LABELS, exist_ok=True)

images = sorted([
    f for f in os.listdir(SRC_IMAGES)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

print("Найдено изображений:", len(images))

counter = START_NUMBER + 1
log = []
missing_label = []

for img in images:
    src_img_path = os.path.join(SRC_IMAGES, img)

    name = os.path.splitext(img)[0]
    old_label = name + ".txt"
    src_label_path = os.path.join(SRC_LABELS, old_label)

    new_name = f"{PREFIX}{counter:04d}.png"
    new_label = f"{PREFIX}{counter:04d}.txt"

    dst_img_path = os.path.join(DST_IMAGES, new_name)
    dst_label_path = os.path.join(DST_LABELS, new_label)

    try:
        with Image.open(src_img_path) as im:
            im = im.convert("RGB")
            im.save(dst_img_path, "PNG")
    except Exception as e:
        print("Ошибка обработки:", img, e)
        continue

    if os.path.exists(src_label_path):
        shutil.copy(src_label_path, dst_label_path)
    else:
        missing_label.append(img)

    log.append(f"{img} -> {new_name}")
    counter += 1

with open("copy_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))

print("Скопировано:", len(log))
print("Без label:", len(missing_label))

if missing_label:
    print("\nПримеры без label:")
    for x in missing_label[:10]:
        print(" -", x)