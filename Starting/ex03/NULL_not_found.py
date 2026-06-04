def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"{object} is NULL")
        return 0
    elif type(object) == float and object != object:  # NaN check
        print(f"{object} is NaN")
        return 0
    elif object == 0 and type(object) != bool:
        print(f"{object} is ZERO")
        return 0
    elif object == "":
        print(f"{object} is EMPTY")
        return 0
    elif object is False:
        print(f"{object} is FALSE")
        return 0
    else:
        print("OK")
        return 1
