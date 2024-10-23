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
    // Use isset to avoid undefined key warnings
    $erpname = isset($_POST['erpname']) ? trim($_POST['erpname']) : '';
    $erppass = isset($_POST['erppass']) ? trim($_POST['erppass']) : '';

    // // Hash the ERP password
    // $erp_hashed_pass = password_hash($erppass, PASSWORD_DEFAULT);

    // Determine the appropriate table to update based on the user role
    if ($_SESSION['role'] == 'Student') {
        // Update ERP credentials for newstudent table
        $update_sql = "UPDATE newstudent SET erpname = ?, erppass = ? WHERE id = ?";
    } elseif ($_SESSION['role'] == 'Teacher') {
        // Update ERP credentials for newteacher table
        $update_sql = "UPDATE newteacher SET erpname = ?, erppass = ? WHERE id = ?";
    } else {
        $showError = true;
        $errorMsg = "Invalid user role.";
    }

    // Prepare and execute the SQL statement
    if (isset($update_sql)) {
        $update_stmt = mysqli_stmt_init($conn);
        if (mysqli_stmt_prepare($update_stmt, $update_sql)) {
            mysqli_stmt_bind_param($update_stmt, "ssi", $erpname, $erppass, $user_id);
            if (mysqli_stmt_execute($update_stmt)) {
                $showAlert = true; // ERP credentials updated successfully
                // Redirect to role-based dashboard
                if ($_SESSION['role'] == 'Student') {
                    header("Location: sdashboard.php");
                } elseif ($_SESSION['role'] == 'Teacher') {
                    header("Location: tdashboard.php");
                }
                exit(); // Ensure script stops after redirection
            } else {
                $showError = true;
                $errorMsg = "Failed to update ERP credentials. Please try again.";
            }
            mysqli_stmt_close($update_stmt);
        } else {
            $showError = true;
            $errorMsg = "Database error. Please try again later.";
        }
    }
}

mysqli_close($conn);
?>
