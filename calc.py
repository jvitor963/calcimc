print("="*198)
#Declaração de Variáveis
Nome=input("Digite seu nome: ")
Idade=int(input("Digite sua idade: ")) 
Altura=float(input("Digite sua altura: "))
Peso=float(input("Digite seu peso: "))
IMC=Peso/Altura**2


#Saída de Dados
print("Os dados coletados foram: ")
print("Seu nome é: ",Nome)
print("Sua idade é: ",Idade, "anos")
print("Sua altura é: ",Altura,"mts")
print("Seu peso é: ",Peso,"Kg")
print("Seu IMC é: ",IMC)
  
if IMC <=16:
    print("MAGREZA GRAVE")
elif IMC <18.5:
    print("MAGREZA LEVE")
elif IMC <24.9:
    print("SAUDÁVEL")
elif IMC <29.9:
    print("SOBREPESO")
elif IMC <34.9:
    print("OBESIDADE")
elif IMC <39.9:
    print("OBESIDADE SEVERA")
else:
    print("OBESIDADE MÓRBIDA")
    