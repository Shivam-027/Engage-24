window.addEventListener('DOMContentLoaded', () => {
    const filesList = document.getElementById('files-list');
    const optionsContainer = document.getElementById('options-container');
    const optionsContent = document.getElementById('options-content');

    // Fetch and display files
    function fetchFiles() {
        fetch('http://127.0.0.1:5000/files')
            .then(response => response.json())
            .then(files => {
                filesList.innerHTML = ''; // Clear current files
                files.forEach(file => createFileCard(file));
            });
    }

    // Initial file fetch
    fetchFiles();

    // Create a file card
    function createFileCard(fileName) {
        const card = document.createElement('div');
        card.className = 'file-card';
        card.innerHTML = `
            <img src="${getFileIcon(fileName)}" alt="File Icon" class="file-icon">
            <h3>${truncateFileName(fileName)}</h3>
            <div class="options">
                <button class="options-button" onclick="toggleOptions('${fileName}', event, this)">⋮</button>
            </div>
        `;
        filesList.appendChild(card);
    }

    // Show or hide options menu
    window.toggleOptions = function(fileName, event) {
        event.stopPropagation();
    
        // Create the HTML content for the options menu
        const optionsHTML = `
            <a href="#" onclick="handleFileDownload('${fileName}'); return false;">Download</a>
            <a href="#" onclick="handleFileDelete('${fileName}'); return false;">Delete</a>
        `;
        optionsContent.innerHTML = optionsHTML;
    
        // Get the button's position relative to the viewport
        const buttonRect = event.target.getBoundingClientRect();
        const containerRect = document.querySelector('.container').getBoundingClientRect();
    
        // Calculate the top and left positions for the options menu
        optionsContainer.style.display = 'block';
        optionsContainer.style.top = `${buttonRect.top - containerRect.top + buttonRect.height}px`; // Position it just below the button
        optionsContainer.style.left = `${buttonRect.left - containerRect.left}px`; // Align it horizontally with the button
    
        // Ensure the menu closes if clicked outside
        setTimeout(() => {
            document.addEventListener('click', closeOptions);
        }, 0);
    };    

    // Close options menu if clicked outside
    function closeOptions(event) {
        if (!optionsContainer.contains(event.target) && !event.target.classList.contains('options-button')) {
            optionsContainer.style.display = 'none';
            document.removeEventListener('click', closeOptions);
        }
    }

    // Handle file upload
    window.uploadFile = function() {
        const uploadInput = document.getElementById('upload-input');
        const file = uploadInput.files[0];
        if (!file) {
            console.log('No file selected');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            if (result.includes('success')) {
                fetchFiles(); // Reload the file list
            } else {
                alert('Error uploading file');
            }
        })
        .catch(error => {
            console.error('Error uploading file:', error);
            alert('Error uploading file');
        });

        uploadInput.value = ''; // Reset the input
    };

    // Handle file download
    window.handleFileDownload = function(fileName) {
        const url = `http://127.0.0.1:5000/download/${fileName}`;
        const a = document.createElement('a');
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        // Hide the options menu
        optionsContainer.style.display = 'none';
    };

    // Handle file delete
    window.handleFileDelete = function(fileName) {
        fetch(`http://127.0.0.1:5000/delete/${fileName}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                fetchFiles(); // Reload the file list
            } else {
                alert('Error deleting file');
            }

            // Hide the options menu
            optionsContainer.style.display = 'none';
        })
        .catch(error => {
            console.error('Error deleting file:', error);
            alert('Error deleting file');
        });
    };

    // Get file icon based on file extension
    function getFileIcon(fileName) {
        const extension = fileName.split('.').pop().toLowerCase();
        const icons = {
            pdf: '../../assets/img/pdf-icon.png',
            docx: '../../assets/img/word-icon.png',
            txt: '../../assets/img/text-icon.png',
            jpg: '../../assets/img/jpg-icon.png',
            jpeg: '../../assets/img/jpg-icon.png',
            png: '../../assets/img/png-icon.png',
            // Add other file types and icons as needed
        };
        return icons[extension] || '../../assets/img/default-icon.png';
    }

    // Truncate file name to fit within card
    function truncateFileName(fileName) {
        const maxLength = 15; // Adjust as needed
        return fileName.length > maxLength ? fileName.substring(0, maxLength) + '...' : fileName;
    }
});


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