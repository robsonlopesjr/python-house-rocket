import pandas as pd

# Carregar o conjunto de dados .csv
data = pd.read_csv('datasets/kc_house_data.csv')

print('Quantas casas estão disponíveis para compra?')
print(f'R: Estão disponíveis o total de {len(data)} casas')

print('Quantos atributos as casas possuem? (número de quartos, número de garagem, metragem)')
print(f'R: Existem {len(data.columns[2:])} atributos')

print('Quais são esses atributos?')
print(f'R: Os atributos são: {list(data.columns[2:])}')

print('Qual a casa mais cara do portifólio? (casa com maior valor)')
order_most_value = data[['id', 'price']].sort_values('price', ascending=False)
print(f'R: A casa mais cara é: {order_most_value[:1]}')

print('Qual a casa com maior número de quartos?')
order_most_bedrooms = data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False)
print(f'R: A casa com o maior numero de quartos é: {order_most_value[:1]}')

print('Qual a soma total de quartos do conjunto de dados?')
sum_room = data['bedrooms'].sum()
print(f'R: O total de quartos é: {sum_room}')

print('Quantas casas possuem 2 banheiros?')
total_homes_with_2_bathrooms = len(data.query("bathrooms == 2"))
print(f'R: {total_homes_with_2_bathrooms} casas')

print('Qual o preço médio de todas as casas do conjunto de dados?')
print("R: Preço médio: {:.2f}".format(data['price'].sum() / len(data)))

print('Qual o preço médio de casas com 2 banheiros?')
sum_homes_with_2_bathrooms = data.query("bathrooms == 2").sum()
print(total_homes_with_2_bathrooms)
print(sum_homes_with_2_bathrooms)
# print("R: Preço médio: {:.2f}".format(sum_homes_with_2_bathrooms / total_homes_with_2_bathrooms))

# print('Qual o preço mínimo entre as casas com 3 quartos?')

# print('Quantas casas possuem mais de 300m² na sala de estar?')

# print('Quantas casas tem mais de 2 andares?')

# print('Quantas casas tem vista para o mar?')

# print('Das casas com vista para o mar, quantas tem 3 quartos?')

# print('Das casas com mais de 300m² de sala de estar, possuem quantos banheiros?')
