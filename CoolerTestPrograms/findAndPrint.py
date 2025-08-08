import os
from collections import Counter

#C:\Users\izdag\OneDrive\Desktop\RandomlyLocatedFolder

def isFound(filePath, target):
    try:
        with open(filePath, 'r') as f:
            for line in f:
                if target in line:
                    return "True"
        return "False"
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    
def sniffer9000(filePath, target):
    wordCount = Counter()
    with open(filePath, 'r') as f:
        for line in f:
            wordInLine = line.strip().lower().split()
            for word in wordInLine:
                wordCount[word] += 1
    return wordCount[target.lower()]

print("\t=== Ultra word snooper 9000 ===\n")
folderPath = input("Enter which folder to use [Ultra word snooper 9000]: ")
wordToFind = input("Enter what word to sniff out: ")

filesSniffed = 0
wordsSniffed = 0

print("\n\t=== Files Sniffed Through Summary ===")

for file in os.listdir(folderPath):
    fullPath = os.path.join(folderPath, file)
    if os.path.isfile(fullPath):
        filesSniffed +=1
        if file.endswith(".txt"):
            try:
                found = isFound(fullPath, wordToFind)
                words = sniffer9000(fullPath, wordToFind)
                print(f"{file:<20} =>   Found: {found:<10} Sniffed words: {words}")
            except Exception as e:
                print(f"Error reading {file}: {e}")

print(f"\nFiles sniffed through: {filesSniffed}")