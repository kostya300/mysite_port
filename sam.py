def get_sum(it):
    s = 0
    for i in it:
            if isinstance(i, int) and type(i) != bool:
                s += i
    print(s)
print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))
print(get_sum({5, 6, 7, '8', 5, '4'}))
print(get_sum((10, "f", '33', True, 12)))
print(get_sum(['1', True, False, (1, 23)]))