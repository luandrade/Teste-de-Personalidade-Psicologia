seus_pontos = 0
pergunta1 = input('''Em Que Momento Você Se Sente Melhor?

a)Pela Manhã
b)À Tarde
c)À Noite

Resposta--> ''')

if (pergunta1 == 'a'):
  seus_pontos = seus_pontos + 2
elif (pergunta1 == 'b'):
  seus_pontos = seus_pontos + 4
else:
  seus_pontos = seus_pontos + 6
print('\n') 
pergunta2 = input('''Normalmente Você Anda...

a)Bem Rápido, Com Passos Longos
b)Bem Rápido, Com Passos Curtos
c)Menos Rápido, Cabeça Levantada, Olhando Pra Tudo
d)Menos Rápido, Cabeça Abaixada
e)Bem Devagar

Resposta--> ''')

if (pergunta2=='a'):
  seus_pontos = seus_pontos + 6
elif (pergunta2=='b'):
  seus_pontos = seus_pontos + 4
elif (pergunta2=='c'):
  seus_pontos=seus_pontos + 7
elif (pergunta2=='d'):
  seus_pontos=seus_pontos + 2
else:
  seus_pontos = seus_pontos + 1 
print('\n')

pergunta3 = input(''' Quando fala com as  pessoas você usualmente:

a) fica de braços cruzados
b)  fica com as mãos apertadas
c) com uma ou  ambas as mãos nos quadris
d) toca ou  empurra a pessoa com quem está falando
e)  brinca com a orelha, toca o queixo ou alisa cabelo

Resposta--> ''')
print('\n')

if (pergunta3=='a'):
  seus_pontos = seus_pontos + 4
elif (pergunta3=='b'):
  seus_pontos = seus_pontos + 2
elif (pergunta3=='c'):
  seus_pontos=seus_pontos + 5
elif (pergunta3=='d'):
  seus_pontos=seus_pontos + 7
else:
  seus_pontos = seus_pontos + 6 
print('\n')

pergunta4 = input('''Quando relaxando,  você se senta:

a) com  os joelhos dobrados e as pernas bem juntas
b)  com as pernas cruzadas
c) com as pernas  estiradas ou retas
d) com uma perna dobrada  embaixo de você

Resposta--> ''')

if (pergunta4=='a'):
  seus_pontos = seus_pontos + 4
elif (pergunta4=='b'):
  seus_pontos = seus_pontos + 6
elif (pergunta4=='c'):
  seus_pontos = seus_pontos + 2
else:  
  seus_pontos=seus_pontos + 1
print('\n')

pergunta5 = input('''Quando algo o diverte de verdade,  você reage com:

a) uma risada alta e satisfeita
b) uma  risada, mas não muito alta
c) com um riso  abafado
d) com um sorriso encabulado

Resposta -->''')
if (pergunta5=='a'):
  seus_pontos = seus_pontos + 6
elif (pergunta5=='b'):
  seus_pontos = seus_pontos + 4
elif (pergunta5=='c'):
  seus_pontos = seus_pontos + 3
else:  
  seus_pontos=seus_pontos + 5
print('\n')

pergunta6 = input('''Quando você vai a uma festa ou encontro social você:

a) Faz uma entrada ruidosa para  que todo mundo perceba
b) faz uma entrada  silenciosa, procurando por um conhecido
c) faz a entrada o mais silenciosa possível, tentando não ser percebido

Resposta--> ''')

if (pergunta6=='a'):
  seus_pontos = seus_pontos + 6
elif (pergunta6=='b'):
  seus_pontos = seus_pontos + 2
elif (pergunta6=='c'):
  seus_pontos = seus_pontos + 4
print('\n')

pergunta7 = input('''Você está trabalhando muito, muito concentrado, e é interrompido, você:

a) aceita bem a interrupção
b) sente-se extremamente irritado
c) varia entre estes extremos

Responda--> ''')

if (pergunta7=='a'):
  seus_pontos = seus_pontos + 6
elif (pergunta7=='b'):
  seus_pontos = seus_pontos + 2
elif (pergunta7=='c'):
  seus_pontos = seus_pontos + 4
print('\n')

pergunta8 = input(''' Qual destas cores você gosta mais?

a) vermelho ou laranja
b) preto
c) amarelo ou azul claro
d) verde
e) azul escuro ou roxo
f) branco
g) marrom ou cinza

Resposta-->''')

if (pergunta8=='a'):
  seus_pontos = seus_pontos + 6
elif (pergunta8=='b'):
  seus_pontos = seus_pontos + 7
elif (pergunta8=='c'):
  seus_pontos = seus_pontos + 5
elif (pergunta8=='d'):
  seus_pontos = seus_pontos + 4
elif (pergunta8== 'e'):
  seus_pontos=seus_pontos + 3
elif (pergunta8 == 'f'):
  seus_pontos = seus_pontos + 2
else:  
  seus_pontos=seus_pontos + 1
print('\n')

pergunta9 = input('''Quando você está na cama, à noite, naqueles minutos finais antes de dormir, você:

a) fica reto de costas
b) fica reto de barriga para baixo
c) fica de lado e ligeiramente curvado
d) com a cabeça em cima do braço
e) com a cabeça sob os lençóis

Resposta--> ''')

if (pergunta9=='a'):
  seus_pontos = seus_pontos + 7
elif (pergunta9=='b'):
  seus_pontos = seus_pontos + 6
elif (pergunta9=='c'):
  seus_pontos = seus_pontos + 4
elif (pergunta9=='d'):
  seus_pontos = seus_pontos + 2
else:
  seus_pontos=seus_pontos + 1
print('\n')  
pergunta10 = input('''Você freqüentemente sonha que está:
a) caindo
b) brigando ou discutindo
c) procurando alguém ou alguma coisa
d) voando ou flutuando
e) você tem um sono sem sonhos
f) seus sonhos são geralmente agradáveis

Resposta--> ''')

if (pergunta8=='a'):
  seus_pontos = seus_pontos + 4
elif (pergunta8=='b'):
  seus_pontos = seus_pontos + 2
elif (pergunta8=='c'):
  seus_pontos = seus_pontos + 3
elif (pergunta8=='d'):
  seus_pontos = seus_pontos + 5
elif (pergunta8== 'e'):
  seus_pontos=seus_pontos + 6
else:
  seus_pontos = seus_pontos + 1

if (seus_pontos > 60):
  print('''
  Os outros o vêem como alguém que eles precisam ter cuidado no convívio.
Você é visto como vaidoso, centrado, e é excessivamente dominador.
Os outros podem até admirá-lo, querendo até mesmo ser um pouco como você, mas não lhe têm confiança e hesitam envolver-se mais profundamente com você.  ''')
elif (seus_pontos >= 51 and seus_pontos <=60):
  print('Os outros o vêem como alguém excitante, altamente volátil, com uma personalidade impulsiva. Um líder natural, que é rápido para tomar decisões, embora nem sempre as decisões acertadas. Eles o enxergam como ousado e aventureiro. Alguém que sempre experimentará algo, uma vez pelo menos. Alguém que corre riscos e aprecia a aventura. As pessoas apreciam estar em sua companhia pelo excitamento que você irradia.')
elif ( seus_pontos >= 41 and seus_pontos <=50):
  print('Os outros o vêem como atrevido, vivaz, charmoso, divertido, prático e sempre interessante. Alguém que está constantemente no centro das atenções, mas suficientemente bem equilibrado para não lhe deixar subir à cabeça. Também o vêem como bondoso, atencioso, delicado, compreensivo. Alguém que sempre os anima e os ajuda.')
elif seus_pontos >= 31 and seus_pontos <=40:
  print('''Os outros o vêem como sensível, cauteloso, cuidadoso e prático.Eles o enxergam como inteligente, capaz, talentoso, mas modesto...Não é uma pessoa que faça amizades rapidamente ou facilmente, mas alguém que é extremamente leal aos amigos que faz, e de quem espera a mesma lealdade de volta. Aqueles que realmente o conhecem compreendem que é difícil abalar a sua lealdade para com os amigos, mas também que leva um bom tempo para superar uma lealdade abalada.''')

elif seus_pontos >= 21 and seus_pontos<= 30:
  print('''Os outros o vêem como meticuloso e exigente.
Eles o enxergam como cauteloso, extremamente cuidadoso e um trabalhador vagaroso e perseverante. Eles ficariam surpresos se você fizesse alguma coisa impulsiva ou de momento, esperando que você examine tudo cuidadosamente, de todos os ângulos, e usualmente vote contra. Eles pensam que esta reação é causada em parte pela sua natureza.''')

else:
  print('''As pessoas o vêem como tímido, nervoso, indeciso.
Alguém de quem precisam tomar conta, que está sempre esperando que os outros tomem as decisões e que não quer se envolver com pessoas ou coisas. Eles o enxergam como uma pessoa preocupada, que sempre vê problemas onde não existem.Algumas pessoas o acham um chato. Somente quem o conhece bem, acha que você não é. ''') 

  
