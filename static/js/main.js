// MENU
const mobileMenu = document.querySelector(".header__mob");
const mobileButton = document.querySelector(".header__menu.link__hover");
const logoLink = document.querySelector('.header__logo');

const menuItemOne = document.querySelector("#menu-item-1");
const menuItemTwo = document.querySelector("#menu-item-2");
const menuItemThree = document.querySelector("#menu-item-3");
const menuItemFour = document.querySelector("#menu-item-4");
const menuItemFive = document.querySelector("#menu-item-5");

const menuLinkOne = document.querySelector("#menu-link-one");
const menuLinkTwo = document.querySelector("#menu-link-two");
const menuLinkThree = document.querySelector("#menu-link-three");
const menuLinkFour = document.querySelector("#menu-link-four");
const menuLinkFive = document.querySelector("#menu-link-five");

function toggleReveal() {
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
}

function toggleMobileMenu() {
    mobileButton.classList.toggle('link__hover_active');
    mobileMenu.classList.toggle('active');
    document.body.classList.toggle('fixed');
    toggleReveal();
}

logoLink.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
    mobileButton.classList.remove('link__hover_active');
    document.body.classList.remove('fixed');
    menuItemOne.classList.remove('reveal');
    menuItemTwo.classList.remove('reveal');
    menuItemThree.classList.remove('reveal');
    menuItemFour.classList.remove('reveal');
    menuItemFive.classList.remove('reveal');
});

mobileButton.addEventListener('click', () =>{
    toggleMobileMenu();
});

menuLinkOne.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkOne.classList.toggle('reveal');
});

menuLinkTwo.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkTwo.classList.toggle('reveal');
});

menuLinkThree.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkThree.classList.toggle('reveal');
});

menuLinkFour.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkFour.classList.toggle('reveal');
});

menuLinkFive.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkFive.classList.toggle('reveal');
});

// Custom form select
const arrowDownServices = document.querySelector("#arrow-down-services");
const selectButtonServices = document.querySelector("#custom-select-services");
const selectionContainerServices = document.querySelector("#container-services");
selectButtonServices.addEventListener('click', () => {
    selectionContainerServices.classList.toggle("open-selection");
    arrowDownServices.classList.toggle("open-arrow");
})

const arrowDownSocials = document.querySelector("#arrow-down-socials");
const selectButtonSocials = document.querySelector("#custom-select-socials");
const selectionContainerSocials = document.querySelector("#container-socials");
selectButtonSocials.addEventListener('click', () => {
    selectionContainerSocials.classList.toggle("open-selection");
    arrowDownSocials.classList.toggle("open-arrow");
})
