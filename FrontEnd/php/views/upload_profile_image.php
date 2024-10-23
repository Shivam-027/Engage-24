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

// Handle image upload
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["profileimage"])) {
    $user_id = $_SESSION['userid'];
    $image = $_FILES['profileimage'];

    // Validate file type and size
    $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
    if (!in_array($image['type'], $allowed_types)) {
        die("Invalid file type. Only JPG, PNG, and GIF are allowed.");
    }

    if ($image['size'] > 800 * 1024) { // Max size 800KB
        die("File size exceeds 800KB.");
    }

    // Create a unique name for the image and move it to the uploads directory
    $target_dir = "uploads/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true); // Create the directory if it doesn't exist
    }

    $imageFileType = strtolower(pathinfo($image["name"], PATHINFO_EXTENSION));
    $new_file_name = $target_dir . "profile_" . $user_id . "_" . time() . "." . $imageFileType;

    // Move uploaded file
    if (move_uploaded_file($image["tmp_name"], $new_file_name)) {
        // Determine the appropriate table to update based on the user role
        if ($_SESSION['role'] == 'Student') {
            // Update profile image for newstudent table
            $sql = "UPDATE newstudent SET profileimage = ? WHERE id = ?";
        } elseif ($_SESSION['role'] == 'Teacher') {
            // Update profile image for newteacher table
            $sql = "UPDATE newteacher SET profileimage = ? WHERE id = ?";
        } else {
            die("Invalid user role.");
        }

        // Prepare and execute the SQL statement
        $stmt = mysqli_stmt_init($conn);
        if (mysqli_stmt_prepare($stmt, $sql)) {
            mysqli_stmt_bind_param($stmt, "si", $new_file_name, $user_id);
            if (mysqli_stmt_execute($stmt)) {
                // Update session variable for profile image
                $_SESSION['profileimage'] = $new_file_name;

                // Redirect to role-based dashboard
                if ($_SESSION['role'] == 'Student') {
                    header("Location: sdashboard.php");
                } elseif ($_SESSION['role'] == 'Teacher') {
                    header("Location: tdashboard.php");
                }
                exit(); // Ensure script stops after redirection
            } else {
                echo "Failed to update profile image in the database.";
            }
            mysqli_stmt_close($stmt);
        } else {
            echo "Database error: " . mysqli_error($conn);
        }
    } else {
        echo "Failed to upload the image.";
    }
}

mysqli_close($conn);
?>
