<?php
session_start();
if (!isset($_SESSION['loggedin'])) {
    header("Location: login.php");
    exit();
}

// Retrieve and unset success and error messages

$showAlert = false;
$showError = false;
$errorMsg = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check which form was submitted
    if (isset($_POST['change_password'])) {
        // Include password change logic
        include __DIR__ . '/../../php/views/change_password.php';
    } elseif (isset($_POST['update_erp'])) {
        // Include ERP update logic
        include __DIR__ . '/../../php/views/update_erp.php';
    } elseif (isset($_POST['update_profile'])) {
        // Include profile update logic
        include __DIR__ . '/../../php/views/upload_profile_image.php';
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>settings page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../../assets/css/settings.css">
</head>

<body>
    <div class="container light-style flex-grow-1 container-p-y">
        <h4 class="font-weight-bold py-3 mb-4">
            Account settings
        </h4>

        <!-- Display Success Message -->
        <?php if ($showAlert): ?>
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                Change successful!
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        <?php endif; ?>

        <!-- Display Error Message -->
        <?php if ($showError): ?>
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <?php echo htmlspecialchars($errorMsg); ?>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        <?php endif; ?>


        <div class="card overflow-hidden">
            <div class="row no-gutters row-bordered row-border-light">
                <div class="col-md-3 pt-0">
                    <div class="list-group list-group-flush account-settings-links">
                        <a class="list-group-item list-group-item-action active" data-toggle="list"
                            href="#account-general">General</a>
                        <a class="list-group-item list-group-item-action" data-toggle="list" href="#account-info">Erp
                            Credentials</a>
                        <a class="list-group-item list-group-item-action" data-toggle="list"
                            href="#account-change-password">Change password</a>
                    </div>
                </div>
                <div class="col-md-9">
                    <div class="tab-content">
                        <div class="tab-pane fade active show" id="account-general">
                            <div class="card-body media align-items-center">
                                <img src="<?php echo isset($_SESSION['profileimage']) ? $_SESSION['profileimage'] : 'https://bootdey.com/img/Content/avatar/avatar1.png'; ?>" alt class="d-block ui-w-80">

                                <div class="media-body ml-4">
                                    <form action="settings.php" method="POST" enctype="multipart/form-data">
                                        <input type="hidden" name="update_profile" value="1">

                                        <label class="btn btn-outline-primary">
                                            Upload new photo
                                            <input type="file" class="account-settings-fileinput" name="profileimage" accept=".jpg, .jpeg, .png, .gif" required>
                                        </label> &nbsp;
                                        <button type="submit" class="btn btn-primary">Save</button>
                                    </form>
                                    <div class="text-light small mt-1">Allowed JPG, GIF or PNG. Max size of 800K</div>
                                </div>
                            </div>
                            <hr class="border-light m-0">
                            <div class="card-body">
                                <div class="form-group">
                                    <label class="form-label">Name</label>
                                    <input type="text" class="form-control mb-1" value="<?php echo htmlspecialchars($_SESSION['name']); ?>" readonly>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">Email</label>
                                    <input type="text" class="form-control" value="<?php echo htmlspecialchars($_SESSION['email']); ?>" readonly>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">Contact No.</label>
                                    <input type="text" class="form-control mb-1" value="<?php echo htmlspecialchars($_SESSION['phone']); ?>" readonly>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">College</label>
                                    <input type="text" class="form-control" value="<?php echo htmlspecialchars($_SESSION['college']); ?>" readonly>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="account-change-password">
                            <div class="card-body pb-2">
                                <form method="POST" action="settings.php">
                                    <input type="hidden" name="change_password" value="1">

                                    <div class="form-group">
                                        <label class="form-label">Current Password</label>
                                        <input type="password" class="form-control" name="current_password" required>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">New Password</label>
                                        <input type="password" class="form-control" name="new_password" required>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Repeat New Password</label>
                                        <input type="password" class="form-control" name="repeat_new_password" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Change Password</button>
                                </form>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="account-info">
                            <div class="card-body pb-2">
                                <form action="settings.php" method="POST">
                                    <input type="hidden" name="update_erp" value="1">

                                    <div class="form-group">
                                        <label class="form-label">ERP Username</label>
                                        <input type="text" class="form-control" name="erpname" placeholder="<?php echo htmlspecialchars($_SESSION['erpname']); ?>">
                                    </div>

                                    <div class="form-group">
                                        <label class="form-label">ERP Password</label>
                                        <input type="text" class="form-control" name="erppass" placeholder="<?php echo htmlspecialchars($_SESSION['erppass']); ?>">
                                    </div>

                                    <!-- Submit button -->
                                    <div class="form-group">
                                        <button type="submit" class="btn btn-primary">Update Erp</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="text-right mt-3 mr-4">
            <?php
            $role_dashboard = ($_SESSION['role'] === 'Student') ? 'sdashboard.php' : 'tdashboard.php';
            ?>
            <button type="button" class="btn btn-outline-light" onclick="window.location.href='<?php echo $role_dashboard; ?>'">Cancel</button>
        </div>

        <script src="../../assets/js/settings.js"></script>

        <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
        <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/js/bootstrap.bundle.min.js"></script>
        <!-- <script type="text/javascript"></script> -->
</body>

</html>