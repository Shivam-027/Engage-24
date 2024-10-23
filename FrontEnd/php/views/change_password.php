<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Check if the user is logged in
if (!isset($_SESSION['loggedin'])) {
    header("Location: login.php");
    exit();
}

// Database configuration
$servername = "localhost:3307";
$username = "root";
$password = "";
$dbname = "studymitrr";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Initialize variables for feedback
$showAlert = false;
$showError = false;
$errorMsg = '';

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_id = $_SESSION['userid'];
    $current_password = isset($_POST['current_password']) ? trim($_POST['current_password']) : '';
    $new_password = isset($_POST['new_password']) ? trim($_POST['new_password']) : '';
    $repeat_new_password = isset($_POST['repeat_new_password']) ? trim($_POST['repeat_new_password']) : '';

    // Basic validation for password change
    if (empty($current_password) || empty($new_password) || empty($repeat_new_password)) {
        $showError = true;
        $errorMsg = "All password fields are required.";
    } elseif ($new_password !== $repeat_new_password) {
        $showError = true;
        $errorMsg = "New passwords do not match.";
    } elseif (strlen($new_password) < 8) {
        $showError = true;
        $errorMsg = "New password must be at least 8 characters long.";
    } else {
        // Determine the appropriate table based on user role
        $table = $_SESSION['role'] == 'Student' ? 'newstudent' : 'newteacher';

        // Retrieve the user's current hashed password from the database
        $sql = "SELECT password FROM $table WHERE id = ?";
        $stmt = mysqli_stmt_init($conn);
        if (mysqli_stmt_prepare($stmt, $sql)) {
            mysqli_stmt_bind_param($stmt, "i", $user_id);
            mysqli_stmt_execute($stmt);
            mysqli_stmt_store_result($stmt);

            if (mysqli_stmt_num_rows($stmt) == 1) {
                mysqli_stmt_bind_result($stmt, $hashed_password);
                mysqli_stmt_fetch($stmt);

                // Verify the current password
                if (password_verify($current_password, $hashed_password)) {
                    // Hash the new password
                    $new_hashed_password = password_hash($new_password, PASSWORD_DEFAULT);

                    // Update the password in the database
                    $update_sql = "UPDATE $table SET password = ? WHERE id = ?";
                    $update_stmt = mysqli_stmt_init($conn);
                    if (mysqli_stmt_prepare($update_stmt, $update_sql)) {
                        mysqli_stmt_bind_param($update_stmt, "si", $new_hashed_password, $user_id);
                        if (mysqli_stmt_execute($update_stmt)) {
                            $showAlert = true; // Password updated successfully
                            // Redirect to role-based dashboard
                            if ($_SESSION['role'] == 'Student') {
                                header("Location: sdashboard.php");
                            } elseif ($_SESSION['role'] == 'Teacher') {
                                header("Location: tdashboard.php");
                            }
                            exit(); // Ensure script stops after redirection
                        } else {
                            $showError = true;
                            $errorMsg = "Failed to update the password. Please try again.";
                        }
                    }
                    mysqli_stmt_close($update_stmt);
                } else {
                    $showError = true;
                    $errorMsg = "Current password is incorrect.";
                }
            } else {
                $showError = true;
                $errorMsg = "User not found.";
            }
            mysqli_stmt_close($stmt);
        } else {
            $showError = true;
            $errorMsg = "Database error. Please try again later.";
        }
    }
}

mysqli_close($conn);
?>
