#write a program which accepts time interval in hours, minutes and seconds.

# hours       minutes        seconds      Total seconds
# 1           10              20              4220

hours = int(input())
minutes = int(input())
seconds = int(input())

print(hours * 3600 + minutes * 60 + seconds)