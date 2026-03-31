const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerNavEl = document.querySelector(".header");

btnNavEl.addEventListener("click", function () {
  headerNavEl.classList.toggle("nav-open");
});
