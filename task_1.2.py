time_sec = int(input('Type in how much time you spent at work yesterday, but in seconds'))
announce = input('Now this script will decode it back into hh:mm:ss format. Press "Enter" to continue.')
convert_sec = time_sec % 60
convert_min = (time_sec // 60) % 60
convert_hour = time_sec // 3600

if convert_hour < 10:
    convert_hour = "0" + str(convert_hour)
if convert_min < 10:
    convert_min = "0" + str(convert_min)
if convert_sec < 10:
    convert_sec = "0" + str(convert_sec)

print(f"Yesterday you spent at work {convert_hour}:{convert_min}:{convert_sec}")

