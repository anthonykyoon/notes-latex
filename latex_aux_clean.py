import os

root_dir = "/Users/anthonyyoon/Documents/LaTeX"

aux_extensions = {
    ".aux",
    ".log",
    ".toc",
    ".out",
    ".lof",
    ".lot",
    ".bbl",
    ".blg",
    ".synctex.gz",
    ".fls",
    ".fdb_latexmk",
    ".tdo"
}

for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if any(filename.endswith(ext) for ext in aux_extensions):
            file_path = os.path.join(foldername, filename)
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
