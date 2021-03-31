def add_time(start, duration, day=""):

  # Splitting start between time and meridian
  start_time = start.split()
  # Splitting the start_time between the hours and minutes
  split_start_time= start_time[0].split(":")
  #Typecasting to int
  split_hours = int(split_start_time[0])
  split_mins = int(split_start_time[1])

  # Splitting duration between time and meridian
  added_time = duration.split()
  # Splitting the added_time between the hours and minutes
  split_added_time = added_time[0].split(":")
  #Typecasting to int
  split_add_hours = int(split_added_time[0])
  split_add_mins = int(split_added_time[1])

  n_days = 0 #number of days to be added

  # Add 12 hours if meridian is PM
  if start_time[1] == "PM":
    split_hours += 12

  mins_sum = split_mins + split_add_mins
  hours_sum = split_hours + split_add_hours

  # Add 1 hour if the minute sum is greater than 60
  if mins_sum > 60:
    mins_sum -= 60
    hours_sum +=1
  
  # Add n days if hours_sum is greater than 24 
  if hours_sum > 24:
    n_days = hours_sum//24
    hours_sum = hours_sum - n_days*24

  # Assigning meridians
  if hours_sum < 12:
    meridian = "AM"
  else:
    hours_sum -=12
    meridian = "PM"

  # Mod hours in mod 12 operation
  if hours_sum == 0:
    hours_sum = 12
  
  # For single digit minutes
  if mins_sum<10: 
    mins_sum = "0" + str(mins_sum)

  # Calculating new_time
  new_time = str(hours_sum) + ":" + str(mins_sum) + " " + meridian 
  
  # Selection of a day
  def week(convar):

    switcher={
      1:'Sunday',
      2:'Monday',
      3:'Tuesday',
      4:'Wednesday',
      5:'Thursday',
      6:'Friday',
      7:'Saturday'
      }
    return switcher.get(convar,"Invalid day of the week")
  
  # Setting new day
  if day!= "":
    if day.lower() == "sunday":
      new_day = week((n_days+1)%7)
    if day.lower() == "monday":
      new_day = week((n_days+2)%7)    
    if day.lower() == "tuesday":
      new_day = week((n_days+3)%7)
    if day.lower() == "wednesday":
      new_day = week((n_days+4)%7)
    if day.lower() == "thursday":
      new_day = week((n_days+5)%7)
    if day.lower() == "friday":
      new_day = week((n_days+6)%7)
    if day.lower() == "saturday":
      new_day = week((n_days+7)%7)
    
    new_time += ", " + new_day

  # Final output
  if n_days > 0:
    if n_days == 1:
      new_time += " (next day)"
    else:
      new_time += " (" + str(n_days) + " days later)"


  return new_time