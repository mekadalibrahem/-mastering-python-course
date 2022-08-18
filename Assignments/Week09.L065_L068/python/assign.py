
import os

#  1  creat 50 text file


def create_multFile(path, basename, ext, number_of_files):
    for i in range(1, number_of_files + 1):
        if i == 25:
            file = open(f"{path}/special-text.{ext}", "a")
            content_file = "Elzero Web School => " + str(i) + "\n"
            file.write(content_file)
            file.close()
        else:
            file = open(f"{path}/{basename}{i}.{ext}", "a")
            content_file = "Elzero Web School => " + str(i) + "\n"
            file.write(content_file)
            file.close()


current_file = os.path.abspath(__file__)
foldername = os.path.dirname(current_file)

create_multFile(foldername, "text", "txt", 50)
print(foldername)
print(current_file)
print(len(os.listdir(foldername)))
