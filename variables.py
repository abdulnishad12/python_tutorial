def variables():
    integer_variable = 10
    string_variable = 'hello python'
    float_vaariable = '0.3'
    complex_varible = 2+4j
    complex_varible_2 = complex(1,2)

    print(integer_variable, type(integer_variable))
    print((string_variable, type(string_variable)))
    print(float_vaariable, type(float_vaariable))
    print(complex_varible, type(complex_varible))
    print(complex_varible_2, type(complex_varible_2))

#     different way of variable assignments
    a=b=c=100
    print(a,b,c)
    x,y,z = 'a','b','c'
    print(x,y,z)
    print(x*3)

if __name__ == '__main__':
    variables()