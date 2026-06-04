def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print(f"List : {type(object)}")
        return -1
    elif type(object) == tuple:
        print(f"Tuple : {type(object)}")
        return -1
    elif type(object) == set:
        print(f"Set : {type(object)}")
        return -1
    elif type(object) == dict:
        print(f"Dict : {type(object)}")
        return -1
    elif type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
        return -1
    else:
        print("Type not found")
        return 42