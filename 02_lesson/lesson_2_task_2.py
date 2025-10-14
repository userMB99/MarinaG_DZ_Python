def is_year_leap(year): 
    if year % 4 == 0: 
        return True
    else: 
        return False


    year_ch = 2020
    is_year_leap(year_ch) 
    rezult = is_year_leap(year_ch) 
    print(f"год{year_ch}:{rezult}")
    year_ch = 2025
    rezult = is_year_leap(year_ch) 
print(f"год{year_ch}:{rezult}")
          