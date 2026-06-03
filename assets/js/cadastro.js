const tabs = document.querySelectorAll(".tab");

const loginForm = document.getElementById("loginForm");
const cadastroForm = document.getElementById("cadastroForm");

tabs.forEach(tab => {
    tab.addEventListener("click", () => {

        tabs.forEach(item => item.classList.remove("active"));
        tab.classList.add("active");

        const selectedTab = tab.dataset.tab;

        if (selectedTab === "login") {
            loginForm.classList.add("active");
            cadastroForm.classList.remove("active");
        } else {
            cadastroForm.classList.add("active");
            loginForm.classList.remove("active");
        }
    });
});

loginForm.addEventListener("submit", event => {
    event.preventDefault();

    // Exemplo de navegação para a página principal
    window.location.href = "index.html";
});

cadastroForm.addEventListener("submit", event => {
    event.preventDefault();

    alert("Cadastro realizado com sucesso!");
});