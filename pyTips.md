# Python File Handling & Basic Syntax Cheat Sheet

# 1. Opening and Reading Files
#Using 'with' to safely open and read a whole file

with open('filename.txt', 'r') as f:
    content = f.read()
    print(content)

# 1. Reading a file line-by-line
with open('filename.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Removes trailing newline

# 2. Writing to Files
with open('filename.txt', 'w') as f:
    f.write("Some text\n")

# 3. Handling File Not Found Errors
try:
    with open('filename.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
    
# 4. Working with File Paths
import os

folder = r"C:\path\to\folder"
filename = "file.txt"
filepath = os.path.join(folder, filename)

# 5. Listing Files in a Directory
import os

for file in os.listdir(folder):
    if file.endswith(".txt"):
        print(file)

# 6. Counting Lines and Words in a File
def line_counter(filepath):
    with open(filepath, 'r') as f:
        return sum(1 for _ in f)

def word_counter(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        words = content.split()
        return len(words)

# 7. Looping with Limits and Error Handling
max_files = 100

try:
    for i in range(max_files):
        filename = f"file_{i}.txt"
        with open(filename, 'w') as f:
            f.write(f"File number {i}\n")
except KeyboardInterrupt:
    print("Process interrupted by user.")
except Exception as e:
    print(f"Error: {e}")

# 8. String Formatting with f-strings for Output Alignment
filename = "example.txt"
lines = 10
words = 200

print(f"{filename:<20} : {lines:>10} lines    Word count: {words:>10}")

# 9. Inserting Blank Lines in Output
print()             # Simple blank line
print("\n")         # New line character
print("\n\t=== Header ===\n")  # New line + tab + text + new line
