# Form
Server para criacao de formularios.

# Fildset
Serve para criar um grupo de elementos de formularios.

E por padrao se usa o `legend`.


# O que é -Webkit
Essa propriedade do CSS faz referência ao Chorme e ao Safari, depois pode utilizar a a propriedade que deseja. Ajuda no dispostivos mobile/tablets, dizendo que não queremos o padrão e sim queremos personalizado.

Ex: -webkit-appearance:none

#  O que é -moz
Essa propriedade do CSS faz referência ao Mozilla FireFox, depois pode utilizar a a propriedade que deseja. Ajuda no dispostivos mobile/tablets, dizendo que não queremos o padrão e sim queremos personalizado.

Ex: -moz-appearance:none


# O que é ::-ms-expand{
Essa propriedade do CSS faz referência ao Internet Explore, ela evita erros de css para appearance. Ajuda no dispostivos mobile/tablets, dizendo que não queremos o padrão e sim queremos personalizado.

Ex: 

    select::-ms-expand{
    display: none;
    }


# O que siginifica + no css
Siginifica que você quer pegar literalmente o valor que está abaixo no HTML

Ex:

`HTML:`

    <form>
        <input type="checkbox" name="checkbox" id="check1">
        <label for="check1"></label>
        <input type="checkbox" id="check2">
        <label for="check2"></label>
    </form>


`CSS:`

    form{
    text-align: center;
    background-color: #ccc;
    padding: 30px 0;
    }

    input[type=checkbox]{
        display: none;
    }
    label{
        display: inline-block;
        margin: 0 60px;
        width: 30px;
        height: 30px;
        background-color: green;
    }
    input[type=checkbox]:checked + label{
        background-color: red;
    }

