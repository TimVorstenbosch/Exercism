color_dict = {
    "black": 0
    ,"brown": 1
    ,"red": 2
    ,"orange": 3
    ,"yellow": 4
    ,"green": 5
    ,"blue": 6
    ,"violet": 7
    ,"grey": 8
    ,"white": 9
}

tolerance_dict = {
    "grey" : "±0.05%"
    ,"violet": "±0.1%"
    ,"blue" : "±0.25%"
    ,"green" : "±0.5%"
    ,"brown" : "±1%"
    ,"red" : "±2%"
    ,"gold" : "±5%"
    ,"silver" : "±10%"
}

def resistor_label(colors):

    if len(colors) == 1:
        return "0 ohms"

    #assuming there are 5 colors
    colors_list = colors[:2] if len(colors) == 4 else colors[:3]
    multiplier = color_dict[colors[-2].lower()]
    tolerance = tolerance_dict[colors[-1].lower()]

    number = int( "".join(str (color_dict[color.lower()] ) for color in colors_list) )
    total = int( str( number ) + "0" * multiplier )

    if total / 1_000_000_000 > 1:
        return f"{str( total // 1_000_000_000 if (total / 1_000_000_000).is_integer() else total / 1_000_000_000 ) } gigaohms {tolerance}"
    
    elif total / 1_000_000 > 1:
        return f"{str( total // 1_000_000 if (total / 1_000_000).is_integer() else total / 1_000_000 ) } megaohms {tolerance}"
    
    elif total / 1_000 > 1:
        return f"{str( total // 1_000 if (total / 1_000).is_integer() else total / 1_000 ) } kiloohms {tolerance}"
    
    else:
        return f"{str(total)} ohms {tolerance}"
    

