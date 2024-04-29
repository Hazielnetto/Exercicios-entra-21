minutos=42
segundos=minutos*60+42
print("Há",segundos,"segundos em 42 minutos e 42 segundos\n")

km=10
print(km,"Quilômetros equivalem a",round(km/1.61,2),"Milhas\n")

velocidade=((km/1.61) / (segundos/3600))
print("Sua velocidade é de",round(velocidade,2),"mph")
print(round(velocidade/60,2),"milhas por minutos")
print(round(velocidade/3600,4),"milhas por segundo")
print("Com um tempo médio de",round(segundos/6.21,2),"segundos por milha\n")