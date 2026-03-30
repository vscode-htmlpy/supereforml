from PIL import Image
import numpy as np

# Carregar imagem
img = Image.open('supere.jpeg')
img_array = np.array(img)

# Converter para RGBA se necessário
if img.mode != 'RGBA':
    img = img.convert('RGBA')
    img_array = np.array(img)

# Detectar área vermelha (valores altos em R, baixos em G e B)
r = img_array[:,:,0]
g = img_array[:,:,1]
b = img_array[:,:,2]

# Critério de vermelho: R > 150, G < 150, B < 150
red_mask = (r > 120) & (g < 140) & (b < 140)

# Criar nova imagem com transparência
result = img.copy()
result_array = np.array(result)

# Aplicar transparência - tudo que não é vermelho fica transparente
alpha = np.ones((img_array.shape[0], img_array.shape[1]), dtype=np.uint8) * 255
alpha[~red_mask] = 0

result_array[:,:,3] = alpha
result = Image.fromarray(result_array, 'RGBA')

# Salvar em PNG (mantém transparência)
result.save('supere.png')
print("Imagem processada! Salva como supere.png")

# Converter de volta para JPEG se preferir (fundo branco)
# Mas PNG é melhor para manter o fundo transparente
