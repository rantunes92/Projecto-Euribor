import numpy as np
import matplotlib.pyplot as plt

def CalculadoraPrestacaoAmor(ValorRemanescente, Prestacao, Amortizacao):
       NovaPrestacao=Prestacao*(ValorRemanescente-Amortizacao)/ValorRemanescente
       print(f"A prestação vai ter o valor de {NovaPrestacao}")
       print(f"É uma redução de {Prestacao-NovaPrestacao}")
       return NovaPrestacao

def CalculadoraPrestacaoInvertida(ValorRemanescente, Prestacao, PrestacaoDesejada):
       Amortizacao=ValorRemanescente-(ValorRemanescente*PrestacaoDesejada)/Prestacao
       print(f"Para ter a prestação desejada é preciso amortizar {Amortizacao}")
       return Amortizacao

def CalcularPrestacaoMensal(valor_remanescente, spread, euribor, prestacoes_faltam):
    taxa_anual = spread + euribor  # Ex: spread 1.0 + euribor 2.116
    taxa_mensal = taxa_anual / 100 / 12  # Converter para taxa mensal

    if taxa_mensal == 0:  # Caso muito raro
        prestacao = valor_remanescente / prestacoes_faltam
    else:
        prestacao = valor_remanescente * (taxa_mensal * (1 + taxa_mensal) ** prestacoes_faltam) / \
                    ((1 + taxa_mensal) ** prestacoes_faltam - 1)
    
    print(f"Com uma Euribor de {euribor}%, Spread de {spread}%, e {prestacoes_faltam} prestações restantes:")
    print(f"A prestação mensal será de: {round(prestacao, 2)} €")
    
    return prestacao

def SubiuOuDesceu(ValorFlag, MediaEuribor):
       if ValorFlag < MediaEuribor:
              print("A prestação vai Subir")
       elif ValorFlag > MediaEuribor:
              print("A prestação vai Descer")
       else:
             print("A prestação vai manter-se")
       

#Media Mensal Outubro 24 3.002
#Valor remanescente 205235.50
#Valor Prestação 890.21

Nov24=[2.822, 2.858, 2.916, 2.923, 2.916, 2.912, 2.831, 2.797, 2.779, 2.765, 2.748, 2.735, 2.743, 2.761, 2.778, 2.770, 2.711, 2.676, 2.694, 2.708, 2.695]
#print(round(np.mean(Nov24), 3))

#Media Mensal Novembro 2024 2.788
#Valor remanescente 205235.50

Dez24=[2.675, 2.634, 2.625, 2.642, 2.654, 2.661, 2.655, 2.654, 2.656, 2.639, 2.655, 2.664, 2.656, 2.639, 2.624, 
2.597, 2.612, 2.577, 2.562, 2.568]
#print(round(np.mean(Dez24), 3))

#Media Dezembro 24 2.632
#Valor remanescente 205028.99

Jan25=[2.562, 2.554, 2.585, 2.631, 2.639, 2.649, 2.641, 2.655, 2.685, 2.657, 2.668, 2.642, 2.619, 2.606, 2.585, 2.586, 2.581,
       2.600, 2.591, 2.598, 2.593, 2.590]
#print(round(np.mean(Jan25), 3))

#Media Janeiro 25 2.614
#Valor remanescente 205028.99

Fev25=[2.536, 2.475, 2.476, 2.466, 2.468, 2.466, 2.481, 2.486, 2.507, 2.514, 2.489, 2.484, 2.474, 2.460, 2.447, 2.421, 2.407,
2.389, 2.389, 2.355]
#print(round(np.mean(Fev25), 3))

#Media Fevereiro 25 2.460
#Valor remanescente 204613.90

Mar25=[2.331, 2.342, 2.353, 2.394, 2.408, 2.390, 2.393, 2.372, 2.386, 2.415, 2.422, 2.422, 2.421, 2.411, 2.404, 2.399, 2.386, 2.375, 2.379, 
       2.354, 2.336]
#print(round(np.mean(Mar25), 3))

#Media Março 25 2.385
#Valor remanescente 204405.32

Abr25=[2.309, 2.320, 2.303, 2.259, 2.275, 2.193, 2.231, 2.190, 2.244, 2.212, 2.214, 2.194, 2.154, 2.173, 2.104, 2.134, 2.141, 2.124, 2.131,
       2.129]
#print(round(np.mean(Abr25), 3))

#Media Abril 25 2.202
#Valor remanescente 204196.05
#Prestação 819.40

Mai25=[2.143, 2.151, 2.145, 2.146, 2.134, 2.111, 2.121, 2.131, 2.156, 2.161, 2.156, 2.120, 2.121, 2.113, 2.118, 2.101, 2.089, 2.056, 
       2.042, 2.056, 2.069]
#print(round(np.mean(Mai25), 3))
ValorFlag=round(np.mean(Mai25), 3)

#Media Maio 25 2.116
#Prestação 809.39
ValorRemanescente=203986.08
PrestacaoFaltam=432


Jun25=[2.063, 2.074, 2.064, 2.046, 2.036, 2.053, 2.044, 2.049, 2.052, 2.056, 2.054, 2.071, 2.061, 2.050, 2.035, 2.036, 2.041, 2.036,
      2.037, 2.036, 2.049]
MediaEuribor=round(np.mean(Jun25), 3)

#Media Junho 25 2.050
#Valor remanescente 203742.30
#Prestação 807.46


Jul25=[2.051, 2.033, 2.031, 2.026, 2.016, 2.019, 2.051, 2.070, 2.072, 2.087, 2.079, 2.069, 2.069, 2.049, 2.051, 2.032, 2.034, 2.037, 
       2.053, 2.101, 2.083, 2.075]
MediaEuribor=round(np.mean(Jul25), 3)
#Media Julho 25 2.054
ValorRemanescente=199742.30
PrestacaoFaltam=431

Ago25=[2.070, 2.077, 2.075, 2.089, 2.087, 2.083, 2.085, 2.098, 2.100, 2.111, 2.112, 2.111, 2.109, 2.093, 2.077, 2.057, 2.070,
      2.064, 2.062, 2.069, 2.074]
MediaEuribor=round(np.mean(Ago25), 3)
#Media Agosto 25 2.084
ValorRemanescente=199500.74
PrestacaoFaltam=430

Set25=[2.086, 2.089, 2.099, 2.103, 2.100, 2.105, 2.106, 2.114, 2.119, 2.108, 2.101, 2.087, 2.083, 2.098, 2.107, 2.109, 2.097,
      2.103, 2.109, 2.123, 2.109, 2.096]
MediaEuribor=round(np.mean(Set25), 3)
#Media Setembro 25 2.102
ValorRemanescente=199258.52
PrestacaoFaltam=429

Out25=[2.079, 2.083, 2.095, 2.103, 2.106, 2.103, 2.104, 2.099, 2.103, 2.106, 2.103, 2.110, 2.113, 2.100, 2.110, 2.099, 2.099,
      2.104, 2.124, 2.126, 2.123, 2.127, 2.138]
MediaEuribor=round(np.mean(Out25), 3)
#Media Outubro 25 2.107
#print(MediaEuribor)
ValorRemanescente=199015.63
PrestacaoFaltam=428

Nov25=[2.142, 2.134, 2.130, 2.129, 2.124, 2.123, 2.127, 2.139, 2.146, 2.141, 2.141, 2.155, 2.149, 2.134, 2.123, 2.120,
      2.121, 2.117, 2.115, 2.110]
MediaEuribor=round(np.mean(Nov25), 3)
#print(MediaEuribor)
ValorRemanescente=198772.07
PrestacaoFaltam=427

ValorFlag=round(np.mean(Nov25), 3)

Dez25=[2.123, 2.121, 2.113, 2.126, 2.147, 2.150, 2.168, 2.165, 2.172, 2.170, 2.168,
      2.164, 2.144, 2.134, 2.126, 2.134, 2.131, 2.119]
MediaEuribor=round(np.mean(Dez25), 3)
print(MediaEuribor)
ValorRemanescente=198527.83
PrestacaoFaltam=426

print(f"Valor flag", ValorFlag)

#CalcularPrestacaoMensal(ValorRemanescente, 1.20, MediaEuribor, PrestacaoFaltam)
#CalculadoraPrestacaoAmor(ValorRemanescente, 795.22, 5000)
#SubiuOuDesceu(ValorFlag, MediaEuribor)


# Graficos da evolução das medias
MesEscolhido=Nov25
"""
x = list(range(1, len(MesEscolhido) + 1))

plt.plot(x, MesEscolhido, marker='o', label='Valores Abr25')
plt.axhline(y=np.mean(MesEscolhido), color='r', linestyle='--', label=f'Média Abril: {round(np.mean(MesEscolhido),3)}')
plt.axhline(y=np.mean(Nov24), color='g', linestyle='--', label=f'Média Novembro: {round(np.mean(Nov24),3)}')
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.title('Gráfico de Fev25')
plt.legend()
plt.grid(True)
plt.show()
"""













