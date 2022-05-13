# Backgrounds

- background-image:
- backgound-repeat:
- background-color:
- background-size:
- background-position:



## Background-image 

 Serve para colocarmos a url da imagem.
Podemos usar `..` para poder voltar para uma pasta onde se encontra o .css.
Nele também podemos por gifs.
**EX:** `background-image: url('image/danki_bg.jpg');`


## Backgound-repeat:

 Serve para evitar a repetição da imagem ou gif.
Há o `repeat`, `no-repeat` e também podemos definir se queremos repetir no angulo **X** ou **Y** usando *repeat-y* e *repeat-x*.
**EX:**`background-repeat: no-repeat;`


## Background-color

 Nele podemos definir a cor do nosso background utilizando `rgb`, `rgba`, `vh(display: grid)`, e `names(ex: red, white)`
**Ex:** background-color: rgba(200, 200, 70, 0.5);


## Background-size:

 Nele podemos utilizar algumas propriedades para determinar se nossa imagem irar cobrir por inteira, ou ficar redimensionavel, como:
- Cover    (preenche os campos vazios do elemento se distorcendo)
- Contain  (Deixa a imagem no tamanho do elemento sem distorcer)
**Ex**: background-size: contain


## Background-position:

 Nele podemos definir a posição da nossa imagem, pondo em `px`, `nomes(center left)`, e `porcetagem(%)`
**Ex:** background-position: center left;
