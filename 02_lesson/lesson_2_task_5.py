def month_to_season(month):


    winter = (1, 2, 12)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)
    if len(winter) == 3 and month in winter:


        return ("Зима")
    elif len(spring) == 3 and month in spring:


        return ("Весна")
    elif len(summer) == 3 and month in summer:


        return ("Лето")
    elif len(autumn) == 3 and month in autumn:


        return ("Осень")
    else:

        
        return "Некорректный номер месяца"
    

        print (month_to_season(input("Введите номер месяца: ")))
    