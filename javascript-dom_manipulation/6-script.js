// Fetch character data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Update the content of the #character element
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
    document.querySelector('#character').textContent = 'Error loading character';
  });
