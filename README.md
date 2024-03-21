# 🪰ING FROGGY - Projeto de IP

## Integrantes

- Adriana Melcop (atmc);
- Ana Lívia (alcp);
- Marcela Raposo (mpr);
- Sarah Lustosa (sccl);
- Sarah Sophia (ssos).

## Descrição do jogo

  🪰ING FROGGY é um jogo 2d do tipo doodle jump feito com a linguagem python e a biblioteca Pygame e Random. Nele, o personagem principal (uma rã) precisa coletar o máximo de moscas, vitórias-régias e vidros de sal que conseguir, isso enquanto salta de plataforma em plataforma em meio as nuvens.

## Capturas de tela

### Tela inicial
<p align="center">
  <img width ="470" src="https://github.com/analiviapessoa/Projeto-IP/assets/159796143/69b18530-16e8-40d8-b787-00ef47b3f428"
</p>

### Jogabilidade
<p align="center">
  <img width ="470" src="https://github.com/analiviapessoa/Projeto-IP/assets/159796143/17049ddc-d41c-426c-988f-2228c05c4cb2"
</p>



### Tela final

<p align="center">
  <img width ="470" src="https://github.com/analiviapessoa/Projeto-IP/assets/159796143/1c186f78-4d61-404f-927b-bde4faa0d950"
</p>

## Ferramentas e bibliotecas utilizadas

 

- Pygame: Fizemos todo o nosso jogo utilizando a biblioteca pygame, que é escrita em python. Voltada para o desenvolvimento de games e interfaces gráficas, foi a base do nosso código.
- Os: A biblioteca os é muito últil quando se trata de interação com o sistema operacional. Utilizamos ela para navegar pelos nossos diretórios.
- Random: Com essa biblioteca, que oferece funções relacionadas à geração de números aleatórios, com ela definimos o tamanho, posição e direção das plataformas e garantimos que as moscas fossem geradas a certa distância das plataformas.
- VS code: Foi o editor de código que nossa equipe utilizou durante o projeto
- Git Hub: É uma plataforma de desenvolvimento colaborativo que aloja projetos na nuvem utilizando o sistema de controle de versões chamado Git. Foi essencial para o sucesso do nosso projeto, com ela pudemos trabalhar no código de forma segura e colaborativa, cada uma da sua casa.
- Canva: Ferramenta online para design, usamos para fazer os slides da apresentação do nosso projeto.
- Figma: Ferramenta online para design, foi utilizada para o design da tela inicial do jogo.
- Remove bg: Ferramenta de IA que utilizamos para remover o fundo de algumas imagens que baixamos da internet para usar no jogo.
- Notion: Ferramenta de organização digital que oferece a possibilidade de criar, colaborar e organizar informações. Foi utilizado para fazer este relatório.

## Divisão do projeto

- Adriana Melcop: Responsável pela física, plataforma(sprites), sapa e slides do projeto;
- Ana Lívia: Responsável pelos efeitos sonoros, movimentação das plataformas, recorde e vidas no jogo.
- Marcela Raposo: Responsável pela música, loop central, moscas e vidas no jogo.
- Sarah Lustosa: Responsável pelo placar, rolagem, tela final, mosca e modularização do jogo.
- Sarah Sophia: Responsável pela tela inicial, sal, contadores e relatório do jogo.

## Conceitos de python utilizados

   Os conceitos de python que aprendemos durante a disciplina de Introdução à Programação e foram usados no desenvolvimento do código foram: Condicionais, laços de repetição e funções.

- Condicionais: Utilizados para checar o recorde do jogador, impedir que a sapa ultrapasse os cantos da tela, determinar direção da sapa de acordo com a tecla do teclado pressionada e etc.
- Laços de repetição: Utilizamos while para manter a tela inicial enquanto a tecla de espaço não fosse pressionada e para o loop principal do jogo. Usamos o for para determinar as ações com os coletáveis durante o  jogo e para as ações caso usuário saísse do jogo.
- Funções: Compõem grande parte do nosso jogo. Temos funções de inicialização, movimentação da sapa, rolagem da tela, painel de game over, vidas da sapa e desenho do plano de fundo.

## Estrutura do projeto

- main.py: É o código principal do jogo. Nele estão as principais junções do jogo, o loop principal e os laços de repetição;
- Coletáveis.py: É o módulos que contem as classes dos coletáveis(mosca, sal e vitória-régia);
- Constantes.py: É o módulo que contem todos os elementos fixos do nosso jogo, como as imagens, dimensões da tela e variáveis;
- Jogador.py: É o módulo com todo o código referente à movimentação do jogador(sapa);
- Imagens: Pasta com todas as imagens utilizadas no jogo;
- Áudios: Pasta com todos os áudios utilizados;
- Placar.txt: Onde sempre fica o maior recorde do jogo até aquele momento;
- README.md: É o arquivo do relatório do jogo.

## Erros e desafios

   Nosso maior erro durante a execução desse projeto foi não ter feito a base do código com poo, o que nós fez ter que reescrever grande parte do código. Nossos maiores desafios foram aprender os conceitos necessários para a realização do projeto, nos familiarizar com o Git Hub e fazer a modularização do código. Superamos esses desafios com muita pesquisa e ajuda dos nossos monitores orientadores.

## Lições aprendidas

   Aprendemos principalmente a importância da comunicação entre as integrantes do grupo e planejamento da execução do projeto, sem uma boa comunicação organização, teríamos muito mais problemas do que tivemos. Aprendemos também a colaborar umas com as outras nas suas funções, tendo humildade para pedir ajuda e ajudar.
