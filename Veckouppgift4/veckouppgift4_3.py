#Veckouppgift4_3: loop_function
def loop_function():
    end  = 5
    y = 1
    for x in range(1,100):
        y*=2
        if x == 5:
            break
    return y
print(loop_function())