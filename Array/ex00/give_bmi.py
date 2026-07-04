```python
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")

    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length")

    bmi = []

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)):
            raise TypeError("height values must be int or float")

        if not isinstance(w, (int, float)):
            raise TypeError("weight values must be int or float")

        bmi.append(w / (h ** 2))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if not isinstance(limit, int):
        raise TypeError("limit must be an int")

    result = []

    for value in bmi:
        if not isinstance(value, (int, float)):
            raise TypeError("bmi values must be int or float")

        result.append(value > limit)

    return result
```
