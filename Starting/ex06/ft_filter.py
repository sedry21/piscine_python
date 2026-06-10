
def ft_filter(function, iterable):
    if function is None:
        for x in iterable:
            if x:
                yield x
    else:
        for x in iterable:
            if function(x):
                yield x

# def main():
#     """Test the ft_filter function."""
#     numbers = [1, 2, 3, 4, 5, 6]
#     result = ft_filter(lambda x: x % 2 == 0, numbers)
#     print(list(result))

#     values = [0, 1, False, True, '', 'hello', [], [1, 2]]
#     result = ft_filter(None, values)
#     print(list(result))


# if __name__ == "__main__":
#     main()
