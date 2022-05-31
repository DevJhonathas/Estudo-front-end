# O que é:
## *nth-of-type()*
**Basicamente ela esta pegando da classe parent a segunda div.**
**Conseguimos estar fazendo com que ela mude um item que está dentro invés da div dela**

**Ex:** **``.parent div:nth-of-type(2)  > div.item{``**
    **``background-color:red;``**
    **``}``**

**Podemos também estar utilizando ele a cada 1 2 ele esteja pondo determinado comando, por exemplo um "background-color:red;".**
**Ex:** **``.parent div:nth-of-type(2n : 1)  > div.item{``**
    **``background-color:red;``**
    **``}``**
  


# O que é:
## First-child e first-of-type
**Basicamente o first-child pegará o primeiro elemento e o fist-of-type pegará o primeiro elemeto do tipo escolhido.**

**Ex:** **``.parent p:first-of-type{``**
    **``background-color:red;``**
    **``}``**

**Ex:** **``.parent p:first-child{``**
**``background-color:red;``**
**``}``**