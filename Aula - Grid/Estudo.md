# Grid css
- bimensional
-divisão de toda a página em linhas e colunas
- Colocar elementos onde quiser nessa divisão

## Grid ou Flexbox
- grid: Duas dimensões (colunas e linhas)
- Flexbox - uma dimensão (ou coluna ou linha)
- Um complementa o trabalho do outro


### Container
-display:grid
-grid-template-columns;
-grid-template-rows;
-grid-gap;
    -grid-row-gap;
    -grid-column-gap;
-grid-template-areas;

...e mais 4 propriedades e **alinhamento**

## Item (s)

- grid-column 
    -grid-column-start
    -grid-column-end
-grid-row
    -grid-row-start
    -grid-row-end
- grid-area 

...e mais 2 propriedades e **alinhamentos**

## Grid: Alinhamento

Existem 6 propriedades para alinhamento:
1. `justify-content`
2. `align-content`
3. `justify-items`
4. `align-items`
5. `justift-self`
6. `align-self`

## Vamos separar em 2 grupos
1. `justify` e `align`
2. `content`, `items` e `self`

## Justify e Align
Grid é bidimennsional, temos eixo x e y.
O **eixo x** é o posicionamento horizontal, da esquerda para direita.
O **eixo y** é o posicionamento vertical, de cima para baixo


## Content, items e self

Juntando e `justify`, ou `align`, com esses elementos: `content`, `items` e `self`; nós observamos nossas propriedades

## Content


`justify-content` e `align-content` nos permite alinhar o próprio grid, relativo ao espaço fora do grid.

O uso dessas propriedades são raras, pois só é aplicado caso o grid seja menor que a area definida (por exemplo, quando usamos em px o tamanho do grid, poderemos terminar com um grid pequeno, para o tamanho da area do grid)

Podemos usar **7 valores**
1. start
2. end
3. center
4. stretch
5. space-between
6. space-around
7. space-evenly   (mesmo tanto de espaço para cada)


### Items
 
`justify-items` e `align-items` vai permitir alinhar os items do nosso grid, em qualquer espaço disponível, na célula que ele habilitar

Podemos usar **4 valores**:
1. start
2. end
3. center
4. stretch


### Self
`justify-self` e `align-self` vai nos permitir alinhar os items em si.

Faz a mesma coisa que o `justify-items` e `align-items`, porém, aplicado diretamente no item de um grid
