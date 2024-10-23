<?php
// Start the session
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>EduBot Homepage</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
	<link rel="stylesheet" href="../../assets/css/homepage.css">
</head>

<body>
	<header id="myHeader" class="">
		<img src="../../assets/img/logo.png" alt="logo" id="logo">

		<?php if (!isset($_SESSION['loggedin']) || !$_SESSION['loggedin']): ?>
			<button class="animated-button" onclick="window.location.href='/studymitrr/php/views/login.php'">
				<span>Login</span>
				<span></span>
			</button>
		<?php else: ?>
			<button class="animated-button" onclick="window.location.href='/studymitrr/php/views/logout.php'">
				<span>Logout</span>
				<span></span>
			</button>
		<?php endif; ?>

		<nav>

			<a href="#home">Home</a>
			<a href="#feature">Feature</a>
			<a href="#team">Team</a>
			<a href="#contact">Contact</a>
			<button id="openmenu">
				<span></span>
				<span></span>
			</button>
		</nav>
	</header>
	<div id="page" class="">
		<section id="home">
			<h1>EduBot.</h1>
		</section>
		<section id="feature">
			<h1>Features.</h1>
		</section>
		<section id="team">
			<h1>Team.</h1>
		</section>
		<section id="contact">
			<h1>Contact.</h1>
		</section>
	</div>

	<script src="../../assets/js/homepage.js"></script>

</body>

</html>