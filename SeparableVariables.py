
def parse_eq():
    eq = 'xydx + xydy = 0'
    parsed_eq = eq.split(' ')
    except_simbols = ['+', '-', '*', '/', '=', '0']

    for item in parsed_eq:
        if item in except_simbols:
            parsed_eq.remove(item)
    define_eq(parsed_eq)
    print(parsed_eq)


def define_eq(units):

    is_separable = True
    is_egregated = True
    answer = ''
    
    #for item in units:
        #print(item)
        #if 'dx' in item:
            #print(item.split('x')
            #if ('y' in item[:-2]):
                #is_separable = False
                #print(item.split('x')

parse_eq()

