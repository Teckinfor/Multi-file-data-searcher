# -*- coding: utf-8 -*-

# Version 1.0.2
# Created by Teckinfor with the help of Groumache
# GitHub : https://github.com/Teckinfor/Multi-file-data-searcher


from os import listdir
from os import system
from os.path import isfile, join

files = [f for f in listdir("database/") if isfile(join("database/", f))]
nb_files = len(files)

loading = [' '] * 100
loading_percent = 0

counter = 0


print("--------- List of files ---------")
for file in files:
    print(file)
print("---------------------------------")
print()

entry = input("Enter search : ")
print("Searching for", entry)
system("cls")

isIn = False

count = 0

results = []

for fichier in files:

    print("Searching for", entry, "--- [Currently",counter,"found]")
    print("Loading [", end="")
    for char in loading:
        print(char, end="")
    print("]", round(float(loading_percent), 2), "%")

    count += 1
    loading_percent = int(100 * count / nb_files)

    i = 0
    while i < loading_percent and i < 99:
        loading[i] = "="
        i += 1

    with open("database/" + fichier, "r", errors="ignore") as f:

        while True:
            line = f.readline()
            if not line:
                break

            if entry in line:
                result = [fichier, line]
                results.append(result)
                counter += 1
                isIn = True
                break

    system("cls")

if not isIn:
    print(entry, "is not in files")

else:
    print(entry, 'is in :')
    for result in results:
        print("-", result[0], "--->", result[1])
    print()
print()

input("Press ENTER to close")
