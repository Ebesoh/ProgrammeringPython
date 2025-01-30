#Veckouppgift4_2_2a: eko
def eko(strings):
    print(f"{strings}{strings}")


#Veckouppgift4_2_2b: eko_count
def eko_count(input_string,count):
    eko_string = ""
    for i in range(count):
        eko_string = eko_string + input_string
    return eko_string

#Veckouppgift4_2_1: my_function
def my_function(strings):
    print(f"{strings}, är en riktig hacker")
