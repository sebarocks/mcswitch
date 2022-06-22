function askServer(url){        
    fetch(url)
    .then(response => response.json())
    .then(data => updateView(data)); 
}

function updateView(server){
    window.mcserver = server
    // actualizar estado
    document.getElementById('estado').innerText = estadosEsp[server.state];
    document.getElementById('estado-title').innerText = server.state;
    // ocultar forms
    document.getElementById('form-encendido').style.display = server.state == 'running' ? 'inline' : 'none';
    document.getElementById('form-apagado').style.display = server.state == 'stopped' ? 'inline' : 'none';
    if ( server.state != 'running' && server.state != 'stopped'){            
        document.getElementById('form-other').style.display = 'inline';
    } else {
        document.getElementById('form-other').style.display = 'none';
    }

    // recargar lista players
    document.getElementById('lista-players').innerHTML="";
    let listaplayers = document.getElementById('lista-players')
    server.players.forEach(playerName => {
        let playerNode = document.createElement('li');
        playerNode.innerText = playerName;
        listaplayers.appendChild(playerNode);
    });
}

window.setInterval(askServer,10000,window.state_url)