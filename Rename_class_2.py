import os

LABELS_DIR = r"G:\DS\labels_y"  # <-- путь к папке с .txt

# old_index -> new_index
CLASS_MAPPING = {
    0: 2,
    1: 10,
    2: 7,
    3: 5,
    4: 8,
    5: 9,
    6: 6,
    7: 4,
    8: 3
}

def remap_labels():
    for filename in os.listdir(LABELS_DIR):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(LABELS_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue

            old_class = int(parts[0])
            if old_class not in CLASS_MAPPING:
                raise ValueError(f"Неизвестный класс {old_class} в файле {filename}")

            new_class = CLASS_MAPPING[old_class]
            parts[0] = str(new_class)
            new_lines.append(" ".join(parts) + "\n")

        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    print("✅ Перенумерация классов завершена")

if __name__ == "__main__":
    remap_labels()
