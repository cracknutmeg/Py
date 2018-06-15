def seconds2time(seconds):
    hour = int ( seconds / 3600 )
    minute = int ((seconds%3600)/60)
    seconds = int ((seconds%3600)%60)

    time = str(hour+minute+seconds)

    return hour

print(seconds2time(985214))
print(seconds2time(3600))
