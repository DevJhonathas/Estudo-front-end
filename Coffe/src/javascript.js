let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
}

let searchForm = document.querySelector('.search-form');

document.querySelector('#pesquisa-btn').onclick = () =>{
    searchForm.classList.toggle('active');
}

let carteItem = document.querySelector('.cart-items-container');

document.querySelector('#compras-btn').onclick = () =>{
    carteItem.classList.toggle('active');
}