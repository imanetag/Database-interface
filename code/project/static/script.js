function addClient() {
    // Get values from the form
    var clientID = document.getElementById('clientID').value;
    var clientName = document.getElementById('clientName').value;

    // Create an XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Set up a POST request to send data to the server
    xhr.open('POST', '/ajouter_client', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Define the data to be sent to the server
    var data = {
        clientID: clientID,
        clientName: clientName
    };

    // Convert data to a JSON string
    var jsonData = JSON.stringify(data);

    // Define what happens on successful data submission
    xhr.onload = function () {
        try {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.status === 'success') {
                    // Display success message
                    document.getElementById('resultMessage').innerHTML = 'Client added successfully!';
                    
                    // Update the UI with the new list of clients
                    displayClients(response.clients);
                } else {
                    // Display error message
                    document.getElementById('resultMessage').innerHTML = response.message || 'Error adding client. Please try again.';
                }
            } else {
                // Display error message for non-200 status
                document.getElementById('resultMessage').innerHTML = 'Error adding client. Please try again.';
            }
        } catch (error) {
            // Display error message for unexpected response
            document.getElementById('resultMessage').innerHTML = 'Error adding client. Please try again.';
        }
    };

    // Send the request with the JSON data
    xhr.send(jsonData);
}

// Function to update the UI with the new list of clients
function displayClients(clients) {
    var listContainer = document.getElementById('clientList');
    listContainer.innerHTML = ''; // Clear existing list

    // Create a new list
    var ul = document.createElement('ul');
    clients.forEach(function (client) {
        var li = document.createElement('li');
        li.textContent = client[1] + ' ' + client[2] + ' - ' + client[4];
        ul.appendChild(li);
    });

    // Append the new list to the container
    listContainer.appendChild(ul);
}
