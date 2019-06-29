# coding: windows-1252
import matplotlib.pyplot as plt

horas_disponiveis = [225, 180, 135, 90, 45, 0]
horas_trabalhadas = [225, 184, 145, 100, 30, 7]
dias_disponiveis = [1, 2, 3, 4, 5, 6]

plt.plot(dias_disponiveis, horas_disponiveis, 'go') # Bolinha Verde
plt.plot(dias_disponiveis, horas_disponiveis, 'k:', color='orange', label='Produção Desejada') # linha pontilha laranja

plt.plot(dias_disponiveis, horas_trabalhadas, 'r^') # Triângulo Vermelho
plt.plot(dias_disponiveis, horas_trabalhadas, 'k--', color='blue', label='Produção Realizada')  # linha tracejada azul

plt.legend(loc='upper right')

plt.title("Gráfico de burndown")

plt.grid(True)
plt.ylabel("Horas disponíveis")
plt.xlabel("Dias disponíveis")
plt.savefig('grafico_burndown.png')
