time_sec = int(input('Type in how much time you spent at work yesterday, but in seconds'))
announce = input('Now this script will decode it back into hh:mm:ss format. Press "Enter" to continue.')
convert_sec = time_sec % 60
convert_min = (time_sec // 60) % 60
convert_hour = time_sec // 3600


print(f"Yesterday you spent at work {convert_hour:02}:{convert_min:02}:{convert_sec:02}")

