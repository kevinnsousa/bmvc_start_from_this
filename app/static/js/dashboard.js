document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('btn-acao');
    const statusMsg = document.getElementById('status-message');

    if (btn && statusMsg) {
        btn.addEventListener('click', () => {
            alert('JavaScript estático executado com sucesso!');
            statusMsg.textContent = "Status atualizado em: " + new Date().toLocaleTimeString();
        });
    }
});