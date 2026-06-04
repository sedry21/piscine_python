def all_thing_is_obj(object: any) -> int:
    if object is None:
        print(f"{object} is {type(object)}")
        return -1
    
    obj_type = type(object).__name__
    print(f"{object} is {obj_type}")
    return -1