import emoji
from time import sleep
print('=== CONTAGEM REGRESSIVA ===')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print(emoji.emojize('=== FELIZ ANO NOVO!!! === :fireworks: :sparkler:'))
