<?php
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['role'] !== 'Student') {
    header("Location: login.php");
    exit();
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Student DashBoard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
    <link rel="stylesheet" href="../../assets/css/studentdash.css">

</head>

<body>
    <header id="myHeader" class="">
        <img src="../../assets/img/logo.png" alt="logo" id="logo">
        <button class="animated-button link3" onclick="window.location.href='../../php/views/settings.php'" onclick="loginlist()">
            <span><img src="../../assets/img/profile.png" alt="profilelogo" width="30px" height="30px">
            </span>
            <div id="dropdown-content2" class="dropdown-content2">
                <div class="hover-content2">
                    <div class="logout">
                        <ul>
                            <li><a href="/studymitrr/php/views/logout.php">Log Out</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <span></span>
        </button>

        <button class="link1" onclick="location.href='#home';">
            <p>Home</p>
            <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="4">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
            </svg> -->
        </button>
        <button class="link2" id="dropdownButton" onclick="featureList()">
            <p>Features</p>
            <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="4">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
            </svg> -->
        </button>
        <div id="dropdown-content" class="dropdown-content">
            <div class="hover-content">
                <div class="list-1">

                    <ul>
                        <li>
                            <h4>Explore Features</h4>
                        </li>
                        <li><a href="../../php/views/quizpractice.html">Quiz Practice</a></li>
                        <li><a href="../../php/views/qapractice.html">Q/A Practice</a></li>
                        <li><a href="../../php/views/contenthub.html">Content Hub</a></li>
                        <li><a href="../../php/views/magicsearch.html">Magic Search</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <button class="link3" onclick="location.href='#review';">
            <p>Reviews</p>
            <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="4">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
            </svg> -->
        </button>
        <button class="link4" onclick="location.href='#contact';">
            <p>Contact</p>
            <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="4">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
            </svg> -->
        </button>

    </header>

    <!-- <nav>
			
			<a href="#home">Home</a>
			<a href="#feature">Feature</a>
			<a href="#team">Team</a>
			<a href="#contact">Contact</a>
			<button id="openmenu">
				<span></span>
				<span></span>
			</button>
		</nav> -->
    <div id="overlay"></div>
    <div id="page" class="">
        <section id="home">
            <!-- <h1>EduBot.</h1> -->

            <div class="card"></div>
            
        </section>
        <section id="feature">
            <!-- <div class="package">
                <div class="package2"><p class="text">Nitro Style</p></div>
              </div> -->
        </section>
        <section id="review">
            <h1>Reviews.</h1>
        </section>
        <section id="contact">
            <h1>Contact.</h1>
        </section>
    </div>
    <script src="../../assets/js/studentdash.js"></script>

</body>

</html>