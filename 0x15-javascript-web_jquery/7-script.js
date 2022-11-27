// This script fetches the character name

$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});
