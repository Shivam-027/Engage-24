window.onbeforeunload = function () {
    window.scrollTo(0, 0); // Scrolls to the top-left corner of the page
};

document.addEventListener('DOMContentLoaded', function () {
    var header = document.getElementById('myHeader');
    var page = document.getElementById('page');
    var openMenuButton = document.getElementById('openmenu');

    window.addEventListener('scroll', function () {
        page.classList.remove('menuopen');
        if (window.scrollY >= 100) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }
    });

    // Event listener to remove the sticky class when the button is clicked
    openMenuButton.addEventListener('click', function () {
        header.classList.remove('sticky');
        page.classList.add('menuopen');
    });

    var links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function (link) {
        link.addEventListener('click', function (event) {
            // Prevent the default action
            event.preventDefault();

            // Get the target element
            var targetId = this.getAttribute('href');
            var targetElement = document.querySelector(targetId);

            // Smooth scroll to target
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});


// for link2 dropdownlist
const button = document.getElementById('dropdownButton');
const dropdownContent = document.getElementById('dropdown-content');

// Show dropdown on mouse enter
button.addEventListener('mouseenter', () => {
    dropdownContent.style.display = 'block';
});

// Hide dropdown on mouse leave
button.addEventListener('mouseleave', () => {
    // Use a small delay to allow hovering on the dropdown content itself
    setTimeout(() => {
        if (!dropdownContent.matches(':hover')) {
            dropdownContent.style.display = 'none';
        }
    }, 200);
});

const overlay = document.getElementById('overlay');
const featurebutton = document.getElementById('dropdownButton');

if (overlay && dropdownContent && dropdownButton) {
    button.addEventListener('mouseenter', () =>{
        overlay.classList.add('show');
        dropdownContent.style.display = 'block';
    })


    dropdownContent.addEventListener('mouseenter', () => {
        overlay.classList.add('show'); 
        dropdownContent.style.display = 'block'; 
    });

    dropdownContent.addEventListener('mouseleave', () => {
        overlay.classList.remove('show'); 
        dropdownContent.style.display = 'none';
    });
} else {
    console.error('Element not found');
}
button.addEventListener('mouseenter', () => {
    overlay.classList.add('show');
    dropdownContent.style.display = 'block';
});

// Hide dropdown and overlay when mouse leaves both the button and dropdown
button.addEventListener('mouseleave', () => {
    setTimeout(() => {
        if (!dropdownContent.matches(':hover')) {
            overlay.classList.remove('show');
            dropdownContent.style.display = 'none';
        }
    }, 200);
});

