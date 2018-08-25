# Elgibility

current_hour = 12
current_minute = 37
current_section = "PM"
due_hour = 12
due_minute = 47
due_section = "PM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current time and deadline time represented by the
#variables above, determine if an assignment is still eligible
#for submission. An assignment is eligible if the time
#represented by current_hour, current_minute, and
#current_section is before the time represented by due_hour,
#due_minute, and due_section.

#Add your code here!

# Just optimized variables
ch = current_hour
cm = current_minute
cs = current_section
dh = due_hour
dm = due_minute
ds = due_section

# We need do this convertation because 12 AM is less than 1 AM and 12 PM is less than 1 PM
if(dh == 12):
    dh = 0
if(ch == 12):
    ch = 0


# PM greater than AM
S = ds > cs
# Section is equal we compare hours
H = (ds == cs) and dh > ch
# compare minutes
M = (ds == cs) and (dh == ch) and (dm > cm)

# elgible if one of variants is true
elgible = S or H or M
print(elgible)