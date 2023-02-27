import shutil

src_path = r"sample.txt"
dst_path = r"sample2.txt"
shutil.copy(src_path, dst_path)
print("Copied")