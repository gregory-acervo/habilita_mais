// Aguarda todo o HTML da página ser carregado
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. FECHAMENTO AUTOMÁTICO DE ALERTAS DO DJANGO
    // Busca todas as mensagens que geramos no base.html
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Define um tempo de 4 segundos (4000 milissegundos)
        setTimeout(() => {
            // Adiciona um efeito suave de transição mudando a opacidade
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            
            // Remove o elemento do HTML após o efeito visual acabar
            setTimeout(() => {
                alert.remove();
            }, 500);
            
        }, 4000);
    });

    // 2. LOG DE BOAS-VINDAS NO CONSOLE
    // Ótimo para os alunos testarem se o arquivo JS carregou de verdade
    console.log("🛒 [E-Commerce Django] Script main.js carregado com sucesso!");
});