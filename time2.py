#Justin Mitchell 2/7/2021
#Program asks user what time it is and how long they will be waiting for
str_time = input("What time is it now?")
str_wait_time = input("What is the number of Hours to wait?")
time = (str_time)
wait_time = (str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
