import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# variável aleatória Y ~ Normal(μ=0, σ=1)
y = rng.normal(loc=0, scale=1, size=10000)

# histograma mostra a distribuição empírica
plt.hist(y, bins=50, edgecolor='black', density=True)
plt.title('Distribuição da variável aleatória Y ~ Normal(0, 1)')
plt.xlabel('Valor')
plt.ylabel('Densidade de probabilidade')
plt.grid(True)
plt.show()
