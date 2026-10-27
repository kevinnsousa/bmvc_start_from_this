document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('btn-action');
    const statusText = document.getElementById('status-text');

    if (btn && statusText) {
        statusText.textContent = "Sistema BMVC ativo e operacional.";

        btn.addEventListener('click', () => {
            alert('Ação executada com sucesso pelo JavaScript estático!');
            statusText.textContent = "Status atualizado em: " + new Date().toLocaleTimeString();
        });
    }
});