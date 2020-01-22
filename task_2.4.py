
user_says = input('Open your favorite book on a random page and type in the first line you see.\nNo punctuation signs,'
                  ' only words.')
user_line = user_says.split(" ")

for num, val in enumerate(user_line, 1):
    print(f"{num}. {val[:10]}")


