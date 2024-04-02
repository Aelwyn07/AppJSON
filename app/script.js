document.getElementById('cryptoForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêcher le formulaire de se soumettre normalement

    const cryptoName = document.getElementById('cryptoInput').value.trim().toLowerCase(); // Récupérer le nom de la cryptomonnaie saisie

    if (cryptoName === '') {
        alert('Veuillez saisir le nom d\'une cryptomonnaie.');
        return;
    }

    // Effectuer une requête AJAX à l'API CoinGecko
    fetch(`https://api.coingecko.com/api/v3/coins/${cryptoName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Impossible de trouver des informations sur cette cryptomonnaie.');
            }
            return response.json();
        })
        .then(data => {
            // Afficher les informations récupérées sur la page
            const cryptoInfoElement = document.getElementById('cryptoInfo');
            cryptoInfoElement.innerHTML = `
            <div class="card mt-3">
            <div class="card-body">
                <h2 class="card-title">${data.name} (${data.symbol.toUpperCase()})</h2>
                <p class="card-text">Prix USD : $${data.market_data.current_price.usd}</p>
                <p class="card-text">Prix EUR : €${data.market_data.current_price.eur}</p>
                <p class="card-text">Prix BTC : ฿${data.market_data.current_price.btc}</p>
                <p class="card-text">Capitalisation boursière : $${data.market_data.market_cap.usd}</p>
            </div>
        </div>
            `;
        })
        .catch(error => {
            alert(error.message);
        });
});
