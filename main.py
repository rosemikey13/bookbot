def main():
    total = 0
    book = ""
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        total += countWords(contents)
        book += contents
    chars = countChars(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words found in the document\n\n")
    for k in chars:
        print(f"The '{k}' character was found {chars[k]} times")
def countChars(book):
    charCount = {}
    for char in book.lower():
        if char.isalpha():
            if char not in charCount:
                charCount[char] = 1
            else:
                charCount[char] += 1
    return charCount

def countWords(line):
    words = line.split()
    count = 0
    for word in words:
        count += 1
    return count        
main()