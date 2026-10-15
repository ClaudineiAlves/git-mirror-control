# Grand Theft Auto: San Andreas · gta-reversed (PC)

Repositório: https://github.com/gta-reversed/gta-reversed · Espelho: https://github.com/alves-r/mirror-gta-reversed-gta-reversed

Projeto que reescreve e documenta, função por função, o GTA San Andreas 1.0 dos EUA. O código vira um plugin ASI, carregado dentro do jogo original, que troca as funções originais pelas reescritas.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Não, precisa compilar (sem releases) |
| Precisa de emulador | Não |
| Você precisa fornecer | O GTA San Andreas original de PC, com o executável "Compact", que tem exatamente 5.189.632 bytes. Ele **não é** o executável 1.0 US comum. Com outro executável, o jogo fecha aleatoriamente. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não suportado (o build é só para Windows) |
| Windows | Nativo |
| Estado | Em andamento: estimativa de 50 a 60% do código. É um hobby, sem previsão de término. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

Não suportado: o README só documenta o build no Windows, com Visual Studio 2026.

## Windows

1. Instale os requisitos:
   - Visual Studio 2026;
   - Python 3, marcando **Add to PATH** na instalação;
   - Conan 2: `pip install conan` e, na primeira vez, `conan profile detect`;
   - CMake 4.2 ou mais novo.
2. Clone o repositório e, na pasta dele, rode `python setup.py`. O padrão é `windows-msvc` x86 Debug.
3. Para só compilar, rode `python setup.py --build`. Para editar, abra a pasta no Visual Studio, pela integração nativa com CMake.
4. Como administrador, rode `contrib/install.py` na raiz do repositório. Ele instala o ASI Loader, o Mouse Fix (`dinput8.dll`) e o plugin compilado na pasta do jogo, usando links simbólicos.
5. Abra o jogo.

O README desaconselha usar outros plugins além dos testados e não dá suporte a eles.

## Fontes

- [README › Requirements, Install Python and Conan, Setting up VS e Set up the game and ASI](https://github.com/gta-reversed/gta-reversed#readme)
- [docs/ReversedClasses.md](https://github.com/gta-reversed/gta-reversed/blob/master/docs/ReversedClasses.md)

<!-- verificado: 2026-10-15 -->
