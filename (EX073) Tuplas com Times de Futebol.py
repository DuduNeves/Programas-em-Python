print('=-=' * 20)
times =('Santos', 'Internacional', 'Bragantino', 'Palmeiras', 'Bahia', 'Atlético-GO', 'Ceará', 'América-MG', 'São paulo', 'Ateltico-MG', 'Corinthians', 'Chapecoense', 'Cuiabá', 'Fortaleza', 'Flamengo', 'Fluminense', 'Grêmio', 'Athletico-PR', 'Juventude', 'Sport')
print(f'\033[1;33mListas de times do brasileirão: {times}\033[m')

print('=-=' * 20)
print(f'\033[1;34mLista do G4: {times[0:4]}\033[m')

print('=-=' * 20)
print(f'\033[1;31mLista do Z4: {times[16:20]}\033[m')

print('=-=' * 20)
print(f'\033[1;36mTimes em ordem alfabetica: {sorted(times)}\033[m')

print('=-=' * 20)
print(f'\033[1;40mO time da {times[11]} está na {times.index("Chapecoense") + 1}ª  posição\033[m')
