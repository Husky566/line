document.getElementById('lineButton').addEventListener('click', function() {
    const apiUrl = 'http://127.0.0.1:5000/get-line-profile-url';

    // เรียก API
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // เปิด URL ของ Line profile ในแท็บใหม่
            window.open(data.url, '_blank');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error fetching the URL.');
        });
});
