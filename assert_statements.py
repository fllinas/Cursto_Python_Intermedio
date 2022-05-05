def divisors(num):
    assert num>=0, "Debes ingresar un numero positivo"
    divisors = [i for i in range(1,num+1) if num%i == 0]  

    return divisors


def run():
    
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Terminó mi programa")
    
     

if __name__ == "__main__":
    run()