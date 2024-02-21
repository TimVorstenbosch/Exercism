def convert(number):
    raindrop = ""

    for num,string in zip([3,5,7], ["Pling", "Plang", "Plong"]):
        if number % num == 0 : raindrop += string

    return raindrop if raindrop != "" else str(number)
