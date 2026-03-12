import os
import shutil

LABEL_DIR = r"D:\DS\video\labels_y"

changed = 0

for file in os.listdir(LABEL_DIR):
    if not file.endswith(".txt"):
        continue

    path = os.path.join(LABEL_DIR, file)

    with open(path, "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            new_lines.append(line)
            continue

        if parts[0] == "0":
            parts[0] = "11"
            changed += 1

        new_lines.append(" ".join(parts) + "\n")

    with open(path, "w") as f:
        f.writelines(new_lines)

print(f"Заменено class_id:", changed)
