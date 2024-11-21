def perpangkatan(base, power):
   
   
    if power == 0:
        return 1  
    elif power > 0:
        return base * perpangkatan(base, power - 1)  
    else:
        return 1 / perpangkatan(base, -power)  
def input_data():
    base_input = input("angka :").strip()
    if base_input == "":  
        print("byee")
        return
    
    base = float(base_input)
    
    power_input = input("pangkat : ").strip()
    if power_input == "":  
        print("byee")
        return
    
    power = int(power_input)
    
    hasil = perpangkatan(base, power)
    print(f"{hasil}")
    
    input_data()

input_data()
