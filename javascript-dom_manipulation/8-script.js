// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Update the content of the #hello element with the translation
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
      document.querySelector('#hello').textContent = 'Error loading translation';
    });
});
