<?php
$showAlert = false;
$showError = false;
$errorMsg = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    include __DIR__ . '/../../php/process-form.php';
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogIn</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <link rel="stylesheet" href="../../assets/css/login.css">

</head>

<body>
    <?php if ($showAlert): ?>
        <div class="alert alert-success">
            Entry successful!
        </div>
    <?php endif; ?>

    <?php if ($showError): ?>
        <div class="alert alert-danger">
            <?php echo $errorMsg; ?>
        </div>
    <?php endif; ?>

    <div class="container" id="container">
        <div class="form-container sign-up-container">
            <form action="login.php" method="post">
                <h1>Sign Up</h1>
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Select your College
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#" data-value="The NorthCap University">The NorthCap University</a></li>
                        <li><a class="dropdown-item" href="#" data-value="Delhi University">Delhi University</a></li>
                        <li><a class="dropdown-item" href="#" data-value="Jawaharlal Nehru University">Jawaharlal Nehru University</a></li>
                        <!-- Add more colleges as needed -->
                    </ul>
                </div>
                <input type="text" name="name" placeholder="Name" required />
                <input type="email" name="email" placeholder="Email" required />
                <input type="text" pattern="[789][0-9]{9}" name="phone" placeholder="Phone No." required />
                <input type="password" name="password" placeholder="Password" required />

                <input type="hidden" name="college" id="selectedCollege" />

                <div class="toggle-container">
                    <span class="role-label">Student</span>
                    <label class="toggle">
                        <input type="checkbox" id="roleToggleSignUp">
                        <span class="slider"></span>
                    </label>
                    <span class="role-label">Teacher</span>
                </div>

                <input type="hidden" name="role" id="selectedRoleSignUp" />
                <button type="submit" name="signup">Sign Up</button>
            </form>
        </div>
        <div class="form-container sign-in-container">
            <form action="login.php" method="post">
                <h1>Sign In</h1>
                <?php if (isset($_SESSION['error'])): ?>
                    <div class="alert alert-danger">
                        <?php
                        echo $_SESSION['error'];
                        unset($_SESSION['error']);
                        ?>
                    </div>
                <?php endif; ?>
                <div class="toggle-container">
                    <span class="role-label">Student</span>
                    <label class="toggle">
                        <input type="checkbox" id="roleToggleSignIn">
                        <span class="slider"></span>
                    </label>
                    <span class="role-label">Teacher</span>
                </div>

                <input type="hidden" name="role" id="selectedRoleSignIn" value="Student" />

                <input type="email" name="email" placeholder="Email" required />
                <input type="password" name="password" placeholder="Password" required />
                <a href="#">Forgot your password?</a>
                <button type="submit" name="signin">Sign In</button>
            </form>
        </div>

        <div class="overlay-container">
            <div class="overlay">
                <div class="overlay-panel overlay-left">
                    <h1>Welcome Back!</h1>
                    <p>To keep connected with us please login with your personal info</p>
                    <button class="ghost" id="signIn">Sign In</button>
                </div>
                <div class="overlay-panel overlay-right">
                    <h1>Hello, Friend!</h1>
                    <p>Enter your personal details and start journey with us</p>
                    <button class="ghost" id="signUp">Sign Up</button>
                </div>
            </div>
        </div>
    </div>

    <script src="../../assets/js/login.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
        integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
        integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
        crossorigin="anonymous"></script>
</body>

</html>