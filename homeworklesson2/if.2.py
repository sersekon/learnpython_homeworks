def main(one, two):
    if not isinstance(one, str) or not isinstance(two, str):
        return ()
    if one == two:
        return (1)
    if len(one) > len(two):
        return 2
    if two == 'learn':
        return 3
print(main('1', 'learn'))
print(main(2, 2))
print(main('tree', 'two'))
print(main('one', 'one'))