year,month,day=map(int,input().split(','))
time=int(input())
years_common=[31,28,31,30,31,30,31,31,30,31,30,31]
day=day+time
while day>years_common[month-1]:
    if year%4==0 and month==2:
         day-=1
    day=day-years_common[month-1]
    month=month+1
    if month>12:
        month=1
        year=year+1
print(f"{year}-{month:02d}-{(day):02d}")