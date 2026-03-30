import os
import sys
import zipfile

# Get root directory here
root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

# Walk through all directories and collect PDFs
pdf_files = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(dirpath, filename))

if not pdf_files:
    print("No PDF files found.")
    sys.exit(0)

# Return as a zip file
output_zip = os.path.join(root_dir, "pdfs.zip")
with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for pdf_path in pdf_files:
        arcname = os.path.relpath(pdf_path, root_dir)
        zf.write(pdf_path, arcname)
        print(f"Added: {arcname}")

print(f"\nDone. {len(pdf_files)} PDF(s) zipped to: {output_zip}")
