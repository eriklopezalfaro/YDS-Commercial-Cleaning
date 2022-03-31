// javascript to create onclick functions for the nav menu when screen size becomes small
let navbar = document.querySelector('nav');
let wrapper = document.querySelector('.wrapper');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    wrapper.classList.toggle('active');
    document.querySelector('#menu-btn').classList.toggle('clicked')
}
document.querySelector('nav ul').onclick = () =>{
    navbar.classList.toggle('active', false);
    wrapper.classList.toggle('active', false);
    document.querySelector('#menu-btn').classList.toggle('clicked', false)

}