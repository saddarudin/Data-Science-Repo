document.getElementById('predictionForm').addEventListener('submit', function (e) {
    e.preventDefault();
    if (isNaN(formData.get('duration'))) {
        alert('Please a valid input value! It should be numerical value');
        e.preventDefault();
    }
    const formData = new FormData(this);


    pred_array = [0, x, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    // Log form data for testing purposes
    const data = {};
    formData.forEach((value, key) => { data[key] = value });
    console.log(data);

});
