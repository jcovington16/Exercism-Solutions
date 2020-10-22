def convert(number: int) -> str:
    list_sounds = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    result = ""    
    for num, sounds in list_sounds:
        if number % num == 0:
            result += sounds
    return str(number) if result == "" else result
    #if result == "":
     #   result == str(number)
   # return result 
