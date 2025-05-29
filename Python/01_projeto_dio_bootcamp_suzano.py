saldo = 0
extrato = ''
numero_saques = 0
limite_saques = 3


pergunta = (
            '\nPara prosseguirmos com a operação, digite uma das seguintes opções:'
            '\nDigite a letra "d" para deposito,'
            '\nDigite a letra "s" para saque,'
            '\nDigite a letra "e" para extrato ou'
            '\nDigite a letra "q" para sair.\n'
            ' ' )

while True:
  operacao = input(pergunta)
  if operacao == 'd':
      valor_depositado = float(input('Digite o valor a ser depositado: '))

      if valor_depositado>0:
            saldo += valor_depositado
            extrato += f'Depósito: R$ {valor_depositado:.2f}'
            print(f'Depósito: R$ {valor_depositado:.2f} realizado com sucesso!')

      else:
            print('#ERRO identificado no valor preenchido, operação não efetuada.'
            '\nPor favor, digite novamente a operação que deseja efetuar e na sequência o valor de depósito.\n')

  elif operacao == 's':
      valor_saque = float(input('Digite o valor a ser sacado: '))

      if valor_saque>500:   #só pode sacar valor menor que R$500,00
          print('#ERRO#'
                '\nO valor sacado é acima do limite permitido, operação não efetuada')

      elif valor_saque>saldo:
          print('#ERRO'
                '\nSaldo insuficiente, operação não efetuada')

      elif numero_saques>=limite_saques:
          print('#ERRO#'
                '\nLimite de saques excedido, operação não efetuada')

      elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"\nSaque: R$ {valor_saque:.2f}"
            numero_saques += 1
            print(f'Saque: R${valor_saque:.2f} realizado com sucesso')
      else:
            print("#ERRO /nO valor informado é inválido.")

  elif operacao =='e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

  elif operacao == "q":
      break

  else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")
