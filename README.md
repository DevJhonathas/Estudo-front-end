
 
 
 
 
# Front end study
`EN-EUA`

### What is this for?

Well, it serves to store my knowledge. Making my studies easier.

### Why decide to create a study repository?

Because I believe it's a great place to keep my studies, in addition to being extremely easy both to consult them later and to add more content at another time.







# Estudo-front-end
`PT-BR`

### Para que serve este repositório?

Bem ele serve para armazenar meus estudos, além de por o meu conhecimento em prática.

### Por que decidi criar um repositório para estudo?

 Pois acredito ser um ótimo local para poder aguardar meu estudos, além de ser extremamente fácil tanto para consultar eles mais tarde quanto para adicionar mais conteudo em outra hora.

  <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>
 
 
# Layout Responsivo
	%
	em
	rem
	fr
	vw
	vh
	vmin
	vmax
	ex
	ch

# Layout Estático
	px

<br><br>
__________________________ 
<br><br>

## Layout Responsivo


#### `%` - Porcetagem <br>
Porcetagem é uma **unidade dinâmica**, ou seja, o **elemento com posicioamento por porcetagem vai variar de acordo com o seu emelento pai.**

<br><br>
#### `em`
**Irar herdar da classe.**
Se definir um elemento no body, todos os elementos no body como divs, h1, e por ai vai... Iram herdar do elemento body.
Ex:
```
body{
	font-size: 14px;
}

div{
	font-size:1.2em;
} /Calculado como 14 1.2, ou 16.9px*/
```
<br><br>
#### `rem`
**Irar se igual a fonte fixada ao elemento raiz(Quase sempre é o HTML)**.
Rem é **bom para grids**. É possível usar em todo um grupo de grids e usar o em para ser escalável.

<br><br>
#### `fr`
**Representa uma fração do espaço disponível no container grid.**
Ex Estás divs vão de 1 a 6. 
```
grid-template-column: 1fr 1fr 1fr
```
Ficará assim:
```
Quadrado | Quadrado | Quadrado
Quadrado | Quadrado | Quadrado
```
<br><br>
#### `vm e vh`
**Servem para o uso de larguras e altura.**

***Vh*** é igual a `1/100 da altura do viewport`. <br>
Ex: **Navegador tem 900px, 1vh é igual a 9px.**

***Vw*** é `usado para questões de largura`, se **definirmos uma página com 750px de largura, 1 vw será igual a 7.5px.**
<br><br>

#### `Vmin e Vmax`
Também **relacionados pela altura e largura**. <br>
Estão relacionados pelos os **valores mínimos e máximos**.  <br>
Ex: O navegador foi ajustado para 1700px de largura, 1vmin seria 7px e vmax seria 11px.

Se a largura fosse 800px e a altura 1080px, vmin seria 8 e o vmax seria 10.8px.

<br><br>
#### `Ex e CH `

***Ex*** (a altura de x da font atual ou metade de 1em). <br>
Unidade ex é a **altura de uma determinada fonte e a altura do caractere "x" em minusculo desta fonte.** <br>
***Usado para micro-ajustes***.
<br><br>

***Ch*** (unidade caractere) <br>
*`Semalhante a em e rem`*, **porém não herdam os valores das fontes**. <br>
*Dada uma fonte com espaçamento uniforme, uma caixa com uma argura "N" como width:40ch, sempre pode conter uma string com 40 caracteres idependente do espaçamento da fonte.*



## Layout Estático
<br>

#### `px`
Unidade de medida estática, **não herdando do seu elemento pai**. <br>
Ao ser posto o valor da fonte, o tamanho permanecerá o mesmo permanentemente. <br>
***Usado em layout estático.***