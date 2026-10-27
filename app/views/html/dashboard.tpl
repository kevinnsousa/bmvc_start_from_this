<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Personalizado</title>
    <link rel="stylesheet" type="text/css" href="/static/css/dashboard.css">
</head>
<body>
    <header>
        <h1>Painel Geral de Controlo</h1>
    </header>

    <main>
        <section class="card">
            <h2>Página do Aluno</h2>
            <p id="status-message">Aplicação BMVC a rodar com sucesso.</p>
            <button id="btn-acao">Executar Teste JS</button>
        </section>

        <form action="/logout" method="post" style="margin-top: 20px;">
            <button type="submit">Terminar Sessão (Logout)</button>
        </form>
    </main>

    <script src="/static/js/dashboard.js"></script>
</body>
</html>