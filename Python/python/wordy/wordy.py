from copy import deepcopy

valid_operations = ["plus", "minus", "multiplied", "divided"]

def check_and_return_number(string):
    try:
        if "-" in string:
            number = int( string.replace("-", "") ) * -1
        else:
            number = int( string )

        return number

    except:
        raise ValueError("syntax error")

def answer(question) -> int:
    parsed_question = question.replace("?", "").split(" ")[2:] #remove ? ; split sentence, remove "What is"
    value = None
    previous_operation = ""
    detected_previous_number = False
    
    if not parsed_question:
        raise ValueError("syntax error")
    elif not any(char.isdigit() for char in question):
        raise ValueError("unknown operation")

    for question_part in parsed_question:

        if previous_operation != "" and question_part == "by":
            continue

        elif detected_previous_number:

            if question_part not in valid_operations:

                try:
                    number = int( question_part.replace("-", "") ) * -1
                    is_number = True
                except:
                    is_number = False

                if is_number:
                    raise ValueError("syntax error")
                else:
                    raise ValueError("unknown operation")
                
            else:
                previous_operation = question_part
                detected_previous_number = False

        else:
            number = check_and_return_number(question_part)

            if value == None:
                value = number
            else:
                match previous_operation:
                    case "plus":  
                        value += number
                    case "minus":
                        value -= number
                    case "multiplied":
                        value *= number
                    case "divided":
                        value /= number

            detected_previous_number = True
            previous_operation = ""

    if previous_operation != "":
        raise ValueError("syntax error")

    return value

# print( answer("What is 2 2 minus 3?") )
                    

    #                     detected_previous_number = False
    # previous_operation = ""

    # for question_part in parsed_question:

    #     if previous_operation != "" and parsed_question == "by":
    #         continue

    #     if value is None:
    #         if not question_part.is_numeric():
    #             raise ValueError("Non math question detected")
    #         else:
    #             value += int(question_part)
    #             detected_previous_number = True
    #             continue

    #     if detected_previous_number == False:
    #         if not question_part.is_numeric():
    #             raise ValueError("No number detected after operation")
    #         else:
    #             match previous_operation:
    #                 case "plus":  
    #                     value += int(question_part)
    #                 case "minus":
    #                     value -= int(question_part)
    #                 case "multiplied":
    #                     value *= int(question_part)
    #                 case "divided":
    #                     value /= int(question_part)
                        
    #             detected_previous_number == True
    #             previous_operation = ""
    #             continue
        
    #     if detected_previous_number == True:
    #         if question_part.is_numeric() or question_part not in valid_operations:
    #             raise ValueError("No operation detected after number")
    #         else:
    #             previous_operation = value.deepcopy()
    #             detected_previous_number = False


