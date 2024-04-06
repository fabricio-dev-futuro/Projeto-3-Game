# Projeto-3-Game
 Jogo da Forca 
 
 Pseudocódigo (Regras para a construção do Jogo)

1 - O jogo deve conter um numero determidado de tentativas

2 - As tentativas devem ser diminuidas a cada vez que o usuário errar uma letra

3 - A letras que o usuário digitou erradas devem ser armazenadas e mostradas

4 - Enquanto as letras da palavra não forem descobertas exiba ' * ' Bequivalente a palavra toda

5 - As letras acertadas devem ficar ao lado dos ' * ' até a ultima letra ser descoberta

6 - Se o número de tentativas exeder o número de chances, exiba uma mensagem de 'Perdedor' 

7 - Se a palavra for adivinhada exiba uma mensagem de 'Vencedor'



 Desenvolvimento do código:

No início estão as importções dos pacotes que: faz sorteio aleatório (pacote: random) e o pacote de sistema operacional os.

- A primeira função (limpa_tela), é responsável por limpar a tela automaticamente ao final da partida. Ela foi desenvolvida para funcionar em Windows, Mac e Linux.

- O jogo todo é executado pela função "jogo".
- Veja que a primeira ação da função "jogo" é chamar a função "limpa_tela" para certificar que o jogo começa com a tela limpa, sem qualquer resíduo no  início.
- As palavras que o usuário deve acertar são trazidas por uma lista Python chamada: "my_palavras".
- São palavras com no máximo 7 caracteres.
- O sorteio da palavra a ser adivinhada é feito pela função random.choice( ). Veja que o argumento foi posto a lista que contém as palavras do game.
- Por fim, salvo o resultado numa nova variável chamada "my_palavra" 

-> ATENÇÃO: observe que a variável que contém a palavra sorteada está no singular, não a confunda com a variável que recebe a lista!
- Em seguida uma variável responsável por armazenar os caracteres da palavra sorteada é criada e adiciono um loop " for " para que a quantidade de letras que a palavra sorteada tiver, fique preenchida com " * ". Dessa forma o usuário verá a quantidade de letras que a palavra tem logo de início.
- O jogo contém um número determidado de tentativas. O responsável por conter a quantidade de tentativas é a variável "my_chances".
- As letras erradas são armazenadas numa lista vazia atrelada a variável "my_letras_vazias".
- Toda a lógica do jogo está dentro de um loop while. E enquanto o número de chances for maior do que zero, o jogo continua rodando.
- Veja que existe uma sequência de prints, cada uma delas será explicada abaixo:

    1 - O primeiro é responsável por manter os asteriscos e as letras adivinhadas juntas. Isso é possível graças a aplicação da função join( );
  
    2 - O segundo é responsável por indicar o número de chances que restam ao usuário para adivinhas a palavra;
 
    3 - O terceiro é responsável por exibir a lista de letras erradas e as mante-las lado a lado. Também possível graças ao uso da função join( ).

- As tentativas são inseridas e já convertidas para que fique no formato – letras minúsculas – com a função lower( ).
- No primeiro condicional " if ", temos a verificação se a letra digitada está correta. Se estiver, ela será colocada no índice correspondente ao dela. Então temos a letra armazenada na lista de palavras descobertas.

-> OBS: se a letra é acertada, a quantidade de chances restantes não tem alteração.
- Se a letra digitada estiver errada, caimos no condicional else, tendo as chances diminuida de -1 e a letra errada sendo adicionada na lista "my_lista_erradas" e exibida para o usuário ver qual letra ele errou (print 3).

Forma de descobrir que foi vencedor ou perdedor:
- O processo de vencedor funciona com um condicional " if " que verifica se há o caractere " * " na variável que recebe as letras descobertas.
- Se for verificar que não existe mais " * " na variável, então a mensagem de vencedor é exibida.

- Para a versão perdedora, temos um condicional if fora do loop while.
- Então, se a variável "my_chances" chegar a zero, o loop while encerra e caimos nesse condicional " if ". Ele verifica se há '*' na variável responsável por armazenar as palavras certas, havendo, a mensagem de que o usuário perdeu o jogo é exibida!

#
Recursos usados no código:

- Funções def( );
- Pacote random para sorteio aleatório;
- Listas em python "[ ]";
- Loop for;
- Loop while;
- Operadores lógicos: in / not in;
- Join para união de string;
- Condicionais: if / elif / else;
- Ativador __main__
