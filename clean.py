import string

def main():

    file = open('silent_sea.txt', 'r')
    content = file.read()
    file.close()
    L = []
    for ch in content:
        if ch not in string.punctuation:
            L.append(ch)
        else:
            L.append('')
    cleaned = ''.join(L)

    file = open('silent_sea_clean.txt', 'w')
    file.write(cleaned)
    file.close()

if __name__== "__main__":
    main()

