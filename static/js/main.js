const mobileMenu = document.querySelector(".header__mob");
const mobileButton = document.querySelector(".header__menu.link__hover");
const logoLink = document.querySelector('.header__logo');

const menuItemOne = document.querySelector("#menu-item-1");
const menuLinkOne = document.querySelector("#menu-link-one");

const menuItemTwo = document.querySelector("#menu-item-2");
const menuLinkTwo = document.querySelector("#menu-link-two");

const menuItemThree = document.querySelector("#menu-item-3");
const menuLinkThree = document.querySelector("#menu-link-three");

const menuItemFour = document.querySelector("#menu-item-4");
const menuLinkFour = document.querySelector("#menu-link-four");

const menuItemFive = document.querySelector("#menu-item-5");
const menuLinkFive = document.querySelector("#menu-link-five");

logoLink.addEventListener('click', function (){
    mobileMenu.classList.remove('active');
    mobileButton.classList.remove('link__hover_active');
})

mobileButton.addEventListener('click', function (){
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
})
menuLinkOne.addEventListener('click', function() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
});
menuLinkTwo.addEventListener('click', function() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
});
menuLinkThree.addEventListener('click', function() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
});
menuLinkFour.addEventListener('click', function() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
});
menuLinkFive.addEventListener('click', function() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
});


