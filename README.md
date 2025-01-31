# Fuja

**Fuja** é um game roguelike desenvolvido usando a biblioteca Pygame Zero. O objetivo do jogo é coletar 6 despertadores para ajudar o fugitivo a escapar de seu pesadelo.

## Organização do Repositório

O repositório está organizado da seguinte forma:

```
fuja  ubuntu  windows
```

### Diretório `fuja`

O diretório `fuja` contém os códigos do game, as imagens e sons do jogo, distribuído da seguinte maneira:

- **fuja.py**: Script principal do jogo.
- **fuja_enemy.py**: Define os inimigos que aparecem no jogo.
- **fuja_object.py**: Objetos que aparecem no cenário.
- **fuja_sounds.py**: Controladores de som do jogo.
- **fuja_intro.py**: Introdução do jogo.
- **fuja_player.py**: A personagem do jogo (fugitivo).
- **fuja_stages.py**: Cenários do jogo.
- **images/**: Contém imagens baixadas de sites com artes livres para games.
- **sounds/**: Contém as músicas e efeitos sonoros livres compartilhados na net.
- **icon.png** e **icon.ico**: Ícones do jogo.

OBS:
Foram utilizadas para o desenvovlimento do game a linguagem de programação Python 3.10.12,
as bibliotecas Pygame Zero, Random e Math. Certifique-se de instalar a biblioteca Pygame Zero
caso você você queira testar os códigos desenvovlvidos,

### Diretório `windows`

O diretório `windows` contém o instalador para instalar o jogo no Windows. Siga os passos abaixo para fazer o download e instalar no Windows:

1. Baixe o instalador `InstaladorFuja.exe` do repositório.
2. Dê um duplo clique no instalador para iniciar a instalação.
3. Siga as instruções do instalador para completar a instalação.

### Diretório `ubuntu`

O diretório `ubuntu` contém o pacote `.deb` para instalar o game no Ubuntu. Siga os passos abaixo para fazer o download, instalar e desinstalar o jogo no Ubuntu:

#### Instalação

1. Baixe o pacote `fuja-1.0.deb` do repositório.
2. Abra o terminal e navegue até o diretório onde o pacote foi baixado.
3. Instale o pacote:

   ```sh
   sudo dpkg -i fuja-1.0.deb
   sudo apt-get install -f  # Corrige quaisquer dependências não satisfeitas
   ```

#### Desinstalação

1. Abra o terminal.
2. Use o seguinte comando para desinstalar o jogo:

   ```sh
   sudo dpkg -r fuja
   ```

## Licença

O jogo **Fuja** é de código aberto, sendo permitido o download para estudo e modificação por qualquer pessoa.

Desenvolvido por **Célio Zagalo**.

- [Instagram](https://www.instagram.com/czagalo/)
- [LinkedIn](https://www.linkedin.com/in/celiozagalo/)

---
