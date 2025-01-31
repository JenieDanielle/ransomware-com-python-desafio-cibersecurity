## Ransomware com python desafio cibersecurity

Este repositório contém dois scripts Python, um para criptografar e outro para descriptografar arquivos usando o algoritmo AES no modo CTR. O objetivo é entender como a criptografia e descriptografia de arquivos podem ser feitas de maneira simples utilizando o pyaes no Python.

## Como rodar o script

### 1. Pré-requisitos
Antes de rodar os scripts, é necessário garantir que o Python 3 e a biblioteza 'pyaes' estejam instaladas no sistema.

Para instalar o pyaes use o pip:
pip install pyaes

### 2. Arquivos do projeto
- encrypter.py: Script para criptografar um arquivo de texto.
- decrypter.py: Script para descriptografar um arquivo de texto.
- texte.txt: Arquivo de texto simples para exemplo.

### 3. Como rodar
1. Coloque os arquivos na mesma pasta
2. No terminal ou prompt, navegue até o diretório e execute:
  python encrypter.py

  Isso criará um novo arquivo chamado 'teste.txt.ransomware' com o conteúdo criptografado.
  
4. No terminal ou prompt execute:
   python edecrypter.py

   Isso criará um arquivo chamado 'teste.txt' com o conteúdo original.
