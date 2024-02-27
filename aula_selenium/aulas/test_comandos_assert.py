assert True

#assert numbers
num_esperado = 1
num_obtido = 2
assert num_esperado == num_obtido, f'Esperado {num_esperado}. Atual {num_obtido}.'
assert num_esperado > num_obtido, f'Esperado {num_esperado}não é maior que o numero atual {num_obtido}.'
assert num_esperado != num_obtido, f'Esperado {num_esperado}não é diferente que o numero atual {num_obtido}.'

# assert text
text_esperado = 'Selenium Webdriver'
text_obtido = 'Selenium webdriver'
assert text_esperado == text_obtido, f'Esperado: {text_esperado}. Atual: {text_obtido}'

# assert text
text_esperado = 'selenium'
text_obtido = 'Selenium webdriver'
assert text_esperado.lower() in text_obtido.lower(), f'Esperado: {text_esperado}. Atual: {text_obtido}'

# assert is_displayed/is_enabled/is_selected
