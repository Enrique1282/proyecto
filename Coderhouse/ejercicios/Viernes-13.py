from datetime import datetime

def tiene_viernes_13(year: int, month: int)-> bool:
    date = datetime(year, month, 13)
    return date.weekday() == 4
    

if __name__ == "__main__":
    print(tiene_viernes_13(2023, 10))