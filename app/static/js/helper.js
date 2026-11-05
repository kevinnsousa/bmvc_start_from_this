document.addEventListener('DOMContentLoaded', () => {
    const btnStatus = document.getElementById('btn-status');
    const statusOutput = document.getElementById('status-output');

    btnStatus.addEventListener('click', () => {
        statusOutput.style.backgroundColor = '#EFE8E1';
        statusOutput.style.color = '#8C7A6B';
        statusOutput.innerHTML = 'Consultando servidor...';

        fetch('/api/status')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na resposta da rede');
                }
                return response.json();
            })
            .then(data => {
                statusOutput.style.backgroundColor = '#EFE8E1';
                statusOutput.style.color = '#4A3E3D';
                statusOutput.innerHTML = `
                    <strong>Status:</strong> ${data.status.toUpperCase()}<br>
                    <small>${data.mensagem}</small>
                `;
            })
            .catch(error => {
                console.error('Erro ao buscar status:', error);
                statusOutput.style.backgroundColor = '#FADBD8';
                statusOutput.style.color = '#78281F';
                statusOutput.innerHTML = '<strong>Erro:</strong> Não foi possível conectar ao servidor.';
            });
    });
});