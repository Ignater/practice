def find_shortest_angle(hour, minute):
    if hour < 0 or hour > 12 or minute < 0 or minute >= 60:
        return "Некорректный формат времени"

    hour_angle = 0.5 * (60 * (hour % 12) + minute)
    minute_angle = 6 * minute

    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

time_str = input("Введите время в формате hh:mm: ")
try:
    hour, minute = map(int, time_str.split(':'))
    result = find_shortest_angle(hour, minute)
    print(f"Кратчайший угол между часовой и минутной стрелками: {result} градусов")
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите время в корректном формате.")
