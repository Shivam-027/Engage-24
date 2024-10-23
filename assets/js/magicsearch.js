async function searchFiles() {
    const query = document.getElementById("query").value;
    const fileType = document.getElementById("file-type").value;

    if (!query) {
        alert("Please enter a search query.");
        return;
    }

    const data = { query, fileType };

    try {
        // Send data to the Python server using fetch
        const response = await fetch('http://127.0.0.1:5000/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // Handle response from Python
        if (response.ok) {
            const result = await response.json();
            displayResults(result.links);
        } else {
            console.error('Error:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function displayResults(links) {
    const resultContainer = document.getElementById("result-container");
    resultContainer.innerHTML = '';  // Clear any previous results

    if (links.length === 0) {
        resultContainer.innerHTML = '<p>No results found.</p>';
    } else {
        links.forEach(link => {
            const linkElement = document.createElement('div');
            linkElement.classList.add('link');
            linkElement.innerHTML = `<a href="${link}" target="_blank">${link}</a>`;
            resultContainer.appendChild(linkElement);
        });
    }
}

// Show dropdown on hover for Profile button
const profileButton = document.querySelector('.animated-button.link3');
const dropdownContent2 = document.getElementById('dropdown-content2');

// Show the dropdown when hovering over the profile button
profileButton.addEventListener('mouseenter', () => {
    dropdownContent2.style.display = 'block';
});

// Hide the dropdown when not hovering over the profile button
profileButton.addEventListener('mouseleave', () => {
    dropdownContent2.style.display = 'none';
});
