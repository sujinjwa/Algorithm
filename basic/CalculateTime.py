hour, mins = 2, 5
elapsed_time = 0

while True:
    if hour == 4 and mins == 1:
        break
    
    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
    
print(elapsed_time)