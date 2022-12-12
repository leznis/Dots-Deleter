import os

print("This will affect EVERY file and subfolder in your folder. Use carefully.")
path = input("Specify your path e.g. (D:\\Videos\\Summer2020): ")
items = [f for f in os.listdir(path)]
print(items)

filename = ""
nodot_list = []

if len(items) != 0:
    for filename in items:
        print("name:", filename)

        # find extension dot
        index = len(filename)  # number of indexes (including 0!)
        for i in range(len(filename)-1, -1, -1):  # from last char to first char
            index -= 1
            if filename[i] == ".":
                break

        print("index of extension dot:", index)
        # save extension to other var
        extension = filename[index:len(filename)+1]
        print("extension:", extension)

        # delete the extension
        filename = filename[:index]
        print("filename without extension:", filename)

        # delete all fucking dots
        filename = filename.replace(".", " ")
        print("filename without dots:", filename)

        filename = filename + extension
        print("filename WITH EXTENSION, NO DOTS:", filename, "\n")

        nodot_list.append(filename)
else:
    print("There are no files, you imbecile!")

for name in range(0, len(items)):
    old_name = items[name]
    new_name = nodot_list[name]
    os.replace(path + "\\" + old_name, path + "\\" + new_name)

print("\n DONE!")