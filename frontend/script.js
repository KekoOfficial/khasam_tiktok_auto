document.getElementById('start').addEventListener('click', () => {
    const titulo = document.getElementById('titulo').value;

    fetch('/start', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({titulo})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('log').innerHTML += data.message + "<br>";
    });
});