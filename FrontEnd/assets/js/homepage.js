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
        header.classList.add('sticky'); // Add sticky class on scroll down
      } else {
        header.classList.remove('sticky'); // Remove sticky class on scroll back to top
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
  