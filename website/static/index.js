document.getElementById('signupForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    // Prevent the default form submission
    const form = event.target; const formData = new FormData(form);
    // Convert FormData to JSON
    const formDataJson = {};
    formData.forEach((value, key) => { formDataJson[key] = value; });
    // Send the JSON data to the server
    const response = await fetch('/signup', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formDataJson) }); const result = await response.json(); console.log(result);
});