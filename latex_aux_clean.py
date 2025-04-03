import os

root_dir = "INSERT PATH HERE LATER"

aux_exntensions = {
    ".aux",
    ".log",
    ".toc",
    ".out",
    ".lof",
    ".lot",
    ".bbl",
    ".blg",
    ".synctex.gz"
}

for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if any(filename.endswith(ext) for ext in aux_extensions):
            file_path = os.path.join(foldername, filename):
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
