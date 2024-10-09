def dms(degree_float):
    degrees = int(degree_float)
    minute_float = 60 * (degree_float - degrees)
    minutes = int(minute_float)
    second_float = 60 * (minute_float - minutes)
    seconds = int(second_float)
    return f"{degrees}°{minutes:02d}'{seconds:02d}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
