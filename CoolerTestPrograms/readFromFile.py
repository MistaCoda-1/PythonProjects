import os

#C:\Users\izdag\OneDrive\Desktop\RandomlyLocatedFolder

def lineCounter(filePath):
    lineCount = 0
    with open(filePath, 'r') as f:
        for line in f:
            lineCount += 1    
        return lineCount

def wordCounter(filePath):
    try:
        with open(filePath, 'r') as f:
            content = f.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

fileCount = 0
totalWords = 0
print('Folder Scanner 9000!')
folderPath = input("Enter in folder path to scan: ")

print('\n\t\t=== Files & Word count ===\n')

for file in os.listdir(folderPath):
    fullPath = os.path.join(folderPath, file)
    if os.path.isfile(fullPath):
        fileCount +=1
        if file.endswith(".txt"):
            try:
                lines = lineCounter(fullPath)
                words = wordCounter(fullPath)
                print(f"{file:<20} : {lines:>10}      Word count: {words:>10}")
                totalWords += words
            except Exception as e:
                print(f"Error reading {file}: {e}")

print(f"\nFolder Path: {folderPath}")
print(f"Files in folder: {fileCount}")
print(f"Words in all folders: {totalWords}")