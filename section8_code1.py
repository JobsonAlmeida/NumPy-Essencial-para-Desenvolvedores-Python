import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# variável aleatória X ~ Binomial(n=10, p=0.3)
x = rng.binomial(n=10, p=0.3, size=10000)

# histograma mostra a distribuição empírica da variável
plt.hist(x, bins=np.arange(12)-0.5, edgecolor='black', density=False)
plt.title('Distribuição da variável aleatória X ~ Binomial(10, 0.3)')
plt.xlabel('Número de sucessos')
plt.ylabel('Probabilidade')
plt.show()
