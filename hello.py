#!/usr/bin/env python3
"""Hello Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar: 

Tenha a variável LANG devidamente configurada ex: 

    export LANG=pt_BR

Execução:
    python 3 hello.py
    ou 
    ./hello.py
"""

#Dunders
__version__="0.0.1"
__author__="Andressa Reis"
__license__="Unlicense"

import os

#Este programa imprime uma mensagem

current_language = os.getenv("lang", "en_US")[:5]
msg= "Hello"

if current_language == "pt_BR":
    msg= "Olá"
elif current_language == "it_IT":
    msg = "Ciao"

print (msg)
