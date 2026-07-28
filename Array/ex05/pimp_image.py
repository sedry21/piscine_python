def ft_invert(array) -> array:
    array = 255 - array
        return array
def ft_red(array) -> array:
    array[:, :, 1] = array[:, :, 1] * 0
    array[:, :, 2] = array[:, :, 2] * 0
    return array
def ft_green(array) -> array:
    array[:, :, 0] = array[:, :, 0] - array[:, :, 0]
    array[:, :, 2] = array[:, :, 2] - array[:, :, 2]
    return array
def ft_blue(array) -> array:
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array
def ft_grey(array) -> array:
    grey = array.sum(axis=2) / 3
    array[:, :, 0] = grey
    array[:, :, 1] = grey
    array[:, :, 2] = grey
    return arrayS