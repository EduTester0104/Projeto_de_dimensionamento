import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        print(f"\033[1;33;45m {('Projeto de dimensionamento - SOLRAC'):^75}\033[0m\n")

        mts = int(input("Distância entre a fonte de tensão e carga em metros: "))
        limpar()

        cabo = int(input("""Selecione a opção da sessão do condutor utilizado:
        [1] 1.5 mm²
        [2] 2.5 mm²
        [3] 4.0 mm²
        [4] 6.0 mm²
        [5] 10  mm²
        [6] 16  mm²
        [7] 25  mm²
        [8] 50  mm²
        [9] 70  mm²
        [10] 90 mm²
        [11] 120 mm

        """))
        limpar()

        match cabo:
            case 1: cabo = 1.5
            case 2: cabo = 2.5
            case 3: cabo = 4.0
            case 4: cabo = 6.0
            case 5: cabo = 10.0
            case 6: cabo = 16.0
            case 7: cabo = 25.0
            case 8: cabo = 50.0
            case 9: cabo = 70.0
            case 10: cabo = 90.0
            case 11: cabo = 120.0
            case _:
                print("O programa está em desenvolvimento 😉!")
                time.sleep(3)
                output.clear()
                continue

        carga = float(input("Digite quantos amperes seu equipamento consome: "))
        limpar()

        tensao = int(input("""Tensão do máquinario:
        [1] Monofásico
        [2] Bifásico
        [3] Trifásico
        """))
        limpar()

        cobre = 0.0173
        n2 = 220 * 4 / 100
        resis = 0

        
        match tensao:
            case 1 | 2:
                resis = (cobre * (mts * 2)) / cabo
                n1 = resis * carga
            case 3:
                resis = (cobre * (mts * 3)) / cabo
                n1 = resis * carga
            case _:
                print("O programa está em desenvolvimento 😉!")
                time.sleep(3)
                limpar()
                continue

        
        if n1 <= n2:
            print(f"A sua distância é de: {mts}m\n\nA sessão do seu cabo é: {cabo}mm²\n\nSua carga foi de: {carga}A\n\n"
                  "Parabéns! Você está de acordo com a norma! Seu equipamento não sofrerá danos com a queda de tensão!")
            break
        else:
            print("Infelizmente seu dimensionamento não funcionou. Aumente a sessão do cabo para evitar problemas!")
            
            while n1 > n2 and cabo < 70:
                cabo += 3.5
                resis = (cobre * (mts * (2 if tensao in [1, 2] else 3))) / cabo
                n1 = resis * carga

            print(f"Uma sugestão para o seu dimensionamento é usar um cabo de {cabo:.1f}mm².")
            time.sleep(8)
            limpar()
            break

    except ValueError:  
        print("Valor inválido! Por favor, insira um número válido.")
        time.sleep(10)
        limpar()
        break
