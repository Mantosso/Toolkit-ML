import os

# Папка датасета
dataset_dir = r"D:\DS\RBF\Tank_DS"

# Подпапки
images_dir = os.path.join(dataset_dir, "images_y")
labels_dir = os.path.join(dataset_dir, "labels_y")

# Собираем список изображений и лейблов (имена без расширений)
images = {os.path.splitext(f)[0] for f in os.listdir(images_dir)
          if f.lower().endswith(('.jpg', '.png', '.jpeg'))}

labels = {os.path.splitext(f)[0] for f in os.listdir(labels_dir)
          if f.lower().endswith('.txt')}

# Лейблы, для которых НЕТ фотографии
labels_without_images = labels - images

print(f"Найдено разметок без фото: {len(labels_without_images)}")

# Удаляем лишние лейблы
for name in labels_without_images:
    label_path = os.path.join(labels_dir, name + ".txt")
    if os.path.exists(label_path):
        os.remove(label_path)

print("\nГотово!")
