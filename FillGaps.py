import os, shutil, re

digits_re = re.compile(r"\d\d\d$")
preffix_num = 1
preffix = f"{preffix_num:03}"


for filename in os.listdir(path):
    file_split = os.path.splitext(filename)
    mo = digits_re.search(file_split[0])

    if file_split[0].endswith(preffix):
        print("good file: " + filename)
        preffix_num += 1
        preffix = f"{preffix_num:03}"


    elif mo != None:
        new_root = digits_re.sub(preffix, file_split[0])
        new_filename = new_root + file_split[1]
        shutil.move(path / filename, path / new_filename)
        print(f"File renamed: {filename} to {new_filename}")
        preffix_num += 1
        preffix = f"{preffix_num:03}"

    else:
        continue