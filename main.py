ticket_count = int(input("Укажите необходимое количетсво билетов: "))
age_for_ticket = [(i, int(input(f"Укажите возраст посетителя для билета № {i+1}: "))) for i in range(ticket_count)]

total_coast = 0

for i in age_for_ticket:
    if 18 <= i[1] <= 25:
        total_coast += 990
    elif i[1] > 25:
        total_coast += 1390

if len(age_for_ticket) > 3:
    total_coast *= 0.9

print(total_coast)
