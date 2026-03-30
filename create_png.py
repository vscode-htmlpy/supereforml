from PIL import Image
import numpy as np
import os

os.chdir(r'c:\Users\amand\Downloads\SUPERE')

# Carregar e processar
img = Image.open('supere.jpeg').convert('RGBA')
arr = np.array(img)

# Extrair canais
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# Máscara para vermelho
mask = (r > 120) & (g < 140) & (b < 140)

# Aplicar transparência
new_alpha = np.where(mask, 255, 0)
arr[:,:,3] = new_alpha

# Salvar
Image.fromarray(arr, 'RGBA').save('supere.png')
print('✓ supere.png criado com sucesso!')
