def timeConversion(s):
    if (s[-2::] == "PM"):
        hour = str(int(s[0:2]) + 12) if s[0:2] != "12" else "12"
        return hour + s[2:-2]
    elif (s[0:2] == "12"):
        return "00" + s[2:-2]
    else:
        return s[0:-2]

time = input() #Eg.:    04:20:00PM or 12:06:09AM
print(timeConversion(time))