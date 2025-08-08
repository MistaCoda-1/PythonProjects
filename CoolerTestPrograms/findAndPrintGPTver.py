import os
from collections import Counter

#C:\Users\izdag\OneDrive\Desktop\RandomlyLocatedFolder

def search_file(filepath, target):
    word_count = 0
    found_lines = []
    target_lower = target.lower()
    try:
        with open(filepath, 'r') as f:
            for lineno, line in enumerate(f, 1):
                line_lower = line.lower()
                if target_lower in line_lower:
                    found_lines.append((lineno, line.strip()))
                    words = line_lower.split()
                    word_count += words.count(target_lower)
        return word_count, found_lines
    except FileNotFoundError:
        return 0, []
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0, []

print("\t=== Ultra word snooper 9000 ===\n")
folderPath = input("Enter folder to search: ")
wordToFind = input("Enter word to sniff out: ")

files_sniffed = 0
total_word_count = 0

print("\n\t=== Files Sniffed Through Summary ===")

for file in os.listdir(folderPath):
    fullPath = os.path.join(folderPath, file)
    if os.path.isfile(fullPath) and file.endswith(".txt"):
        files_sniffed += 1
        word_count, lines = search_file(fullPath, wordToFind)
        total_word_count += word_count
        found = word_count > 0
        print(f"{file:<25} Found: {str(found):<5}  Count: {word_count}")
        # Uncomment below to print matching lines with line numbers
        # for lineno, line in lines:
        #     print(f"  Line {lineno}: {line}")

print(f"\nFiles sniffed through: {files_sniffed}")
print(f"Total occurrences of '{wordToFind}': {total_word_count}")
