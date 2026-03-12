import os
from collections import defaultdict

CLASS_NAMES = [
    "малый транспорт",
    "большой транспорт",
    "самолет",
    "резервуар",
    "корабль",
    "гавань",
    "кольцевая развязка",
    "мост",
    "вертолет",
    "вертолетная площадка",
    "аэропорт",
    "танк"
]

def analyze_dataset(labels_dir):
    class_counts = defaultdict(int)
    images_with_class = defaultdict(int)
    total_objects = 0

    txt_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]

    for file in txt_files:
        classes_in_image = set()
        path = os.path.join(labels_dir, file)

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) != 5:
                    continue

                class_id = int(parts[0])

                class_name = (
                    CLASS_NAMES[class_id]
                    if class_id < len(CLASS_NAMES)
                    else f"class_{class_id}"
                )

                class_counts[class_name] += 1
                total_objects += 1
                classes_in_image.add(class_name)

        for cl in classes_in_image:
            images_with_class[cl] += 1

    print(f"Всего файлов разметки: {len(txt_files)}")
    print(f"Всего объектов: {total_objects}")
    print(f"Количество уникальных классов: {len(class_counts)}\n")

    print("Классы и количество объектов:")
    for cl, cnt in class_counts.items():
        print(f"  {cl}: {cnt}")

    print("\nКлассы и количество изображений, где они встречаются:")
    for cl, cnt in images_with_class.items():
        print(f"  {cl}: {cnt}")

analyze_dataset(r"D:\DS\All_DS\labels")