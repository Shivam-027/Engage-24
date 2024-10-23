<?php
$servername = "localhost:3307";
$username = "root";
$password = "";
$dbname = "studymitrr";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$showAlert = false;
$showError = false;
$errorMsg = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Handle Sign Up
    if (isset($_POST['signup'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $password = password_hash($_POST['password'],PASSWORD_DEFAULT);
        $college = $_POST['college'];
        $role = $_POST['role'];

        // Determine the correct table based on the role
        if ($role === 'Student') {
            $sql = "INSERT INTO newstudent (name, email, phone, password, college, role) VALUES (?, ?, ?, ?, ?, ?)";
        } elseif ($role === 'Teacher') {
            $sql = "INSERT INTO newteacher (name, email, phone, password, college, role) VALUES (?, ?, ?, ?, ?, ?)";
        } else {
            $showError = true;
            $errorMsg = "Invalid role selected.";
        }

        if (!$showError) {
            $stmt = mysqli_stmt_init($conn);

            if (!mysqli_stmt_prepare($stmt, $sql)) {
                $showError = true;
                $errorMsg = "Failed to prepare the SQL statement. Please try again later.";
                error_log("SQL Error: " . mysqli_error($conn));
            } else {
                if (!mysqli_stmt_bind_param($stmt, "ssisss", $name, $email, $phone, $password, $college, $role)) {
                    $showError = true;
                    $errorMsg = "Failed to bind parameters. Please try again later.";
                    error_log("Parameter Binding Error: " . mysqli_error($conn));
                } else {
                    try {
                        if (mysqli_stmt_execute($stmt)) {
                            $showAlert = true;
                        }
                    } catch (mysqli_sql_exception $e) {
                        if ($e->getCode() == 1062) { // Duplicate entry error code
                            $showError = true;
                            $errorMsg = "An account with this email already exists. Please use a different email.";
                        } else {
                            $showError = true;
                            $errorMsg = "Failed to execute the statement. Please try again later.";
                            error_log("Execution Error: " . $e->getMessage());
                        }
                    }
                }
            }
        }
    }

    // Handle Sign In
    if (isset($_POST['signin'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];

        // Check both student and teacher tables for the user
        $sqlStudent = "SELECT * FROM newstudent WHERE email=?";
        $sqlTeacher = "SELECT * FROM newteacher WHERE email=?";

        $stmtStudent = mysqli_stmt_init($conn);
        $stmtTeacher = mysqli_stmt_init($conn);

        $userFound = false;

        // Check in newstudent table
        if (mysqli_stmt_prepare($stmtStudent, $sqlStudent)) {
            mysqli_stmt_bind_param($stmtStudent, "s", $email);
            mysqli_stmt_execute($stmtStudent);
            $resultStudent = mysqli_stmt_get_result($stmtStudent);

            if ($resultStudent->num_rows == 1) {
                $row = $resultStudent->fetch_assoc();
                $storedHash = $row['password'];

                // Debugging logs
                error_log("Stored Hash (Student): " . $storedHash);
                error_log("Input Password: " . $password);

                // Combine this as an error message to display on the form (for debugging purposes)
                $errorMsg .= "Stored Hash (Student): " . $storedHash . " Input Password: " . $password . "<br>";

                if (password_verify($password, $storedHash)) {
                    $userFound = true;
                    // Start the session
                    session_start();
                    $_SESSION['loggedin'] = true;
                    $_SESSION['name'] = $row['name'];
                    $_SESSION['email'] = $row['email'];
                    $_SESSION['phone'] = $row['phone'];
                    $_SESSION['college'] = $row['college'];
                    $_SESSION['userid'] = $row['id'];
                    $_SESSION['role'] = $row['role'];
                    $_SESSION['erpname'] = $row['erpname'];
                    $_SESSION['erppass'] = $row['erppass'];

                    // Redirect to student dashboard
                    header("Location: sdashboard.php");
                    exit();
                } else {
                    $showError = true;
                    $errorMsg .= "Invalid password!<br>";
                }
            }
        }

        // Check in newteacher table if not found in students
        if (!$userFound && mysqli_stmt_prepare($stmtTeacher, $sqlTeacher)) {
            mysqli_stmt_bind_param($stmtTeacher, "s", $email);
            mysqli_stmt_execute($stmtTeacher);
            $resultTeacher = mysqli_stmt_get_result($stmtTeacher);

            if ($resultTeacher->num_rows == 1) {
                $row = $resultTeacher->fetch_assoc();
                $storedHash = $row['password'];

                // Debugging logs
                error_log("Stored Hash (Teacher): " . $storedHash);
                error_log("Input Password: " . $password);

                // Combine this as an error message to display on the form (for debugging purposes)
                $errorMsg .= "Stored Hash (Student): " . $storedHash . " Input Password: " . $password . "<br>";

                if (password_verify($password, $storedHash)) {
                    $userFound = true;

                    // Start the session
                    session_start();
                    $_SESSION['loggedin'] = true;
                    $_SESSION['name'] = $row['name'];
                    $_SESSION['email'] = $row['email'];
                    $_SESSION['phone'] = $row['phone'];
                    $_SESSION['college'] = $row['college'];
                    $_SESSION['userid'] = $row['id'];
                    $_SESSION['role'] = $row['role'];
                    $_SESSION['erpname'] = $row['erpname'];
                    $_SESSION['erppass'] = $row['erppass'];

                    // Redirect to teacher dashboard
                    header("Location: tdashboard.php");
                    exit();
                } else {
                    $showError = true;
                    $errorMsg .= "Invalid password!<br>";
                }
            }
        }

        // No user found in either table
        if (!$userFound && !$showError) {
            $showError = true;
            $errorMsg .= "No user found with this email!<br>";
        }

    }
}

$conn->close();
?>
