lst= [2200,2350,2600,2130,2190]


# 1 
print(f"${lst[1] - lst[0]}")

# 2
print(f"You spent ${lst[0] + lst[1] +lst[2]} ")

# 3


for expense in lst:
    if expense == 2000:
        print(expense + " is exactly 2000")
    print("month is $2000") 

lst.append(1980)


lst[3] = lst[3] - 200

print(lst[3])