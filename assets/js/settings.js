document.addEventListener('DOMContentLoaded', function () {
    function hideMessages() {
        const alertBoxes = document.querySelectorAll('.alert'); // Select all alert elements (both success and error)
        
        alertBoxes.forEach((alertBox) => {
            if (alertBox) {
                setTimeout(() => {
                    alertBox.style.transition = 'opacity 0.5s ease'; // Smooth fade out
                    alertBox.style.opacity = '0'; // Set opacity to 0 for fade effect

                    setTimeout(() => {
                        alertBox.style.display = 'none'; // Hide the element after fading out
                    }, 500); // Wait for transition to complete
                }, 5000); // 5 seconds delay before fade starts
            }
        });
    }

    hideMessages();
});
