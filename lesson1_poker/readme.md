## Poker

* Inicia em main.py, melhor maneira de usar é brincando pelo console

Executar:
````python
    from deal import deal
    from main import poker
````

* ```hands=deal(n)``` saca n mãos e armazena numa lista
* ```poker(hands)``` retorna a mão vencedora (ou as mãos vencedoras em caso de empate)


## Notas

## 

### 6 - Understanding `max`
`print(max([1,2,3]), max([1,2,-3], key=abs))`
Irá retornar `3 -3`.

### 7 - Using max
A função key pode ser, claro, uma função definida por nós:
```python
def poker(hands):
    return max(hands, key=hand_rank)
``` 
Aqui, `hand_rank` é a função que retorna a pontuação de cada mão.

### Controlnado o desempenho com testes
Podemos escrever uma função de teste usando um statement `assert`, que pára o programa e retorna uma mensagem de erro (AssertionError) caso o resultado seja `False`
```python
def test():
    assert funcao(etc) == retorno_esperado
    return "tests pass"
```

