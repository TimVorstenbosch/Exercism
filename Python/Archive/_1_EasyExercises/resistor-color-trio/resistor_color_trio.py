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

def label(colors: list) -> str:
    number = int( "".join(str (color_dict[color.lower()] ) for color in colors[:2]) )
    total = int( str( number ) + "0" * color_dict[colors[:3][-1].lower()] )

    if total / 1_000_000_000 > 1:
        return f"{str(total // 1_000_000_000) } gigaohms"
    elif total / 1_000_000 > 1:
        return f"{str(total // 1_000_000) } megaohms"
    elif total / 1_000 > 1:
        return f"{str(total // 1_000) } kiloohms"
    else:
        return f"{str(total)} ohms"
