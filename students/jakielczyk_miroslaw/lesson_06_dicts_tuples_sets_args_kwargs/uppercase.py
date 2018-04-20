def capitalize(word):
    return word[0].upper() + word[1:]


def main():
    words_list = input().split(' ')
    for word in words_list:
        print(capitalize(word), end=' ')


if __name__ == "__main__":
    main()
