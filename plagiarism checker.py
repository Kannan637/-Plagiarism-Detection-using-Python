from difflib import SequenceMatcher

with open("/content/Demo#1.txt") as file1, open("/content/Demo#2.txt") as file2:
    file1_data = file1.read()
    file2_data = file2.read()

    matches = SequenceMatcher(None, file1_data, file2_data).ratio()

    print(f"Plagiarism Detection {matches * 100}%")
