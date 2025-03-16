# Projeto: Refatoracao do Nynbot

## Visao Geral
Este repositório documenta a refatoracao do projeto Nynbot utilizando o padrão de projeto Command e Singleton. O objetivo da refatoracao foi melhorar a manutenibilidade, reduzir o acoplamento e aumentar a coesao do código, garantindo que a funcionalidade original fosse preservada.

## Alteracoes Realizadas
### Estruturais
- Separacao de responsabilidades em classes/modulos distintos. Removendo lógica de métodos da clase main e as movendo para commands.


### Codigo
- Remocao de duplicacao de codigo.
- Implementação de uma classe Singleton com a constante que contem o token que permite a integração do código com a API do Discord.

## Consideracoes Finais
A refatoracao resultou em um codigo mais limpo, modular e está fechado para mudanças e aberto a expansões, visto que para adicionar uma nova funcionalidade bastaria criar uma nova classe command. Caso encontre algum problema ou tenha sugestoes de melhorias, abra uma issue ou contribua com um pull request.

## Autores
Miguel Amaral Lessa Xavier 
