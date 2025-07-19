import numpy as np
import gc
import sys

# Desativar coleta de lixo temporariamente para evitar interferência
gc.disable()



array_original = np.array([1, 2, 3, 4])
print("ID original:", id(array_original))
print("Referências:", sys.getrefcount(array_original))

print(len(array_original))

# Guardar referência temporária para teste
referencia_extra = array_original

# Criar novo array com append
array_novo = np.append(array_original, [5])
print("\nID novo:", id(array_novo))
print("ID do original ainda é:", id(array_original))

print("Referências ao array original:", sys.getrefcount(array_original))
print("Quem referencia:", gc.get_referrers(array_original))

# Liberar referência
referencia_extra = None

print("\nReferências depois de remover variável:", sys.getrefcount(array_original))

# Reativar coleta de lixo
gc.enable()
