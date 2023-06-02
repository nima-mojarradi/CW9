def division(a:int, b:int):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print('try again')
        return division(a,b)