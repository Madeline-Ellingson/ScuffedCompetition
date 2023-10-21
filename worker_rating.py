def main():
    input()
    lst = input().split()
    counter = 0
    max_length = 0
    for i in range(len(lst)):
        if int(lst[i]) > 6:
            counter += 1
        else:
            if counter > max_length:
                max_length = counter
            counter = 0
        if i == len(lst) - 1 and counter > max_length:
            max_length = counter
    print(max_length)


if __name__ == "__main__":
    main()