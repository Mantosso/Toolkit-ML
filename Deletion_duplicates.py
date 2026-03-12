from pathlib import Path
import hashlib
import os

ROOT = Path(r"DS\All_DS\dataset_tiled")

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def collect_hashes(split):
    img_dir = ROOT / "images" / split
    hashes = {}
    for f in img_dir.glob("*.jpg"):
        hashes[get_hash(f)] = f.name
    return hashes

print("Сбор хэшей...")

train_hashes = collect_hashes("train")
val_hashes = collect_hashes("val")
test_hashes = collect_hashes("test")

removed = 0

def remove_if_duplicate(split_hashes, split_name):
    global removed
    img_dir = ROOT / "images" / split_name
    lbl_dir = ROOT / "labels" / split_name

    for h, name in list(split_hashes.items()):
        if h in train_hashes:
            img_path = img_dir / name
            lbl_path = lbl_dir / (Path(name).stem + ".txt")

            if img_path.exists():
                os.remove(img_path)
            if lbl_path.exists():
                os.remove(lbl_path)

            removed += 1

print("Удаление дубликатов из val...")
remove_if_duplicate(val_hashes, "val")

print("Удаление дубликатов из test...")
remove_if_duplicate(test_hashes, "test")

print("Готово. Удалено:", removed)