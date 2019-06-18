print('##Exercicio 53##')

palavras = ('JOAO', 'VITOR','SKONIENCZWY','BRASILEIRO','HOLANDA','ENGINEER')

for c in palavras:
 print(f'\nA palavra {c} tem : ' , end='')
 for letra in c:
  if letra in 'AaEeIiOoUu':
      print(letra,end=' ')
