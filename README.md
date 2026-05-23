# 🍽️ Sabor Express

Sistema de gerenciamento de restaurantes desenvolvido em Python com Programação Orientada a Objetos.

## 📋 Funcionalidades

- Cadastro de restaurantes com nome e categoria
- Listagem de restaurantes em formato de tabela
- Sistema de avaliações com nota de 1 a 5
- Cálculo automático de média de avaliações
- Alternância de status ativo/inativo

## 📁 Estrutura do Projeto

```
Sabor Express/
├── app.py
└── modelos/
    ├── avaliacao.py
    └── restaurante.py
```

## ▶️ Como executar

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sabor-express.git
```

2. Acesse a pasta do projeto
```bash
cd sabor-express
```

3. Execute o projeto
```bash
python app.py
```

> ⚠️ **Atenção:** sempre execute o `app.py` a partir da pasta raiz do projeto, nunca diretamente os arquivos dentro de `modelos/`.

## 🛠️ Tecnologias

- Python 3.14

## 📚 Conceitos de OO aplicados

| Conceito | Onde aparece |
|---|---|
| **Classes e objetos** | `Restaurante`, `Avaliacao` |
| **Encapsulamento** | Atributos com `_` (privados) |
| **Atributo de classe** | `restaurantes = []` |
| **Atributo de instância** | `self._nome`, `self._ativo` |
| **Método de classe** | `@classmethod listar_restaurantes` |
| **Property** | `ativo`, `media_avaliacao` |
| **Composição** | `Restaurante` contém objetos `Avaliacao` |

## 💡 Exemplo de uso

```python
from modelos.restaurante import Restaurante

# Criando restaurantes
restaurante_praca = Restaurante('Praça', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza Place', 'Italiana')

# Adicionando avaliações (notas de 1 a 5)
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 4)

# Alternando status
restaurante_praca.alternar_estado()

# Listando todos os restaurantes
Restaurante.listar_restaurantes()
```

Saída esperada:
```
Nome do restaurante       | Categoria                 | Média de avaliações       | Status
Praça                     | Comida Caseira             | 4.5                       | Ativo
Pizza Place               | Italiana                   | 0                         | Inativo
```
