document.addEventListener('DOMContentLoaded', function() {
    const dropdownItems = document.querySelectorAll('.dropdown-menu .dropdown-item');
    const selectedCollegeInput = document.getElementById('selectedCollege');

    dropdownItems.forEach(item => {
        item.addEventListener('click', function() {
            selectedCollegeInput.value = this.getAttribute('data-value');
            document.querySelector('.dropdown button').innerText = this.innerText;
        });
    });

    // Sign-Up Role Toggle
    const roleToggleSignUp = document.getElementById('roleToggleSignUp');
    const selectedRoleInputSignUp = document.getElementById('selectedRoleSignUp');
    const studentLabelSignUp = document.querySelectorAll('.role-label')[0];
    const teacherLabelSignUp = document.querySelectorAll('.role-label')[1];

    // Set default role to Student for Sign-Up
    if (selectedRoleInputSignUp) {
        selectedRoleInputSignUp.value = 'Student'; // Default to Student
        studentLabelSignUp.classList.add('role-label-active'); // Activate Student label by default
        teacherLabelSignUp.classList.add('role-label-inactive'); // Inactivate Teacher label by default
    }

    if (roleToggleSignUp && selectedRoleInputSignUp) {
        roleToggleSignUp.addEventListener('change', () => {
            const isTeacher = roleToggleSignUp.checked;
            selectedRoleInputSignUp.value = isTeacher ? 'Teacher' : 'Student';

            if (isTeacher) {
                studentLabelSignUp.classList.remove('role-label-active');
                studentLabelSignUp.classList.add('role-label-inactive');
                teacherLabelSignUp.classList.remove('role-label-inactive');
                teacherLabelSignUp.classList.add('role-label-active');
            } else {
                teacherLabelSignUp.classList.remove('role-label-active');
                teacherLabelSignUp.classList.add('role-label-inactive');
                studentLabelSignUp.classList.remove('role-label-inactive');
                studentLabelSignUp.classList.add('role-label-active');
            }

            console.log('Sign Up Role:', selectedRoleInputSignUp.value);
        });
    }

    // Sign-In Role Toggle
    const roleToggleSignIn = document.getElementById('roleToggleSignIn');
    const selectedRoleInputSignIn = document.getElementById('selectedRoleSignIn');
    const studentLabelSignIn = document.querySelectorAll('.role-label')[0];
    const teacherLabelSignIn = document.querySelectorAll('.role-label')[1];

    // Set default role to Student for Sign-In
    if (selectedRoleInputSignIn) {
        selectedRoleInputSignIn.value = 'Student'; // Default to Student
        studentLabelSignIn.classList.add('role-label-active'); // Activate Student label by default
        teacherLabelSignIn.classList.add('role-label-inactive'); // Inactivate Teacher label by default
    }

    if (roleToggleSignIn && selectedRoleInputSignIn) {
        roleToggleSignIn.addEventListener('change', () => {
            const isTeacher = roleToggleSignIn.checked;
            selectedRoleInputSignIn.value = isTeacher ? 'Teacher' : 'Student';

            if (isTeacher) {
                studentLabelSignIn.classList.remove('role-label-active');
                studentLabelSignIn.classList.add('role-label-inactive');
                teacherLabelSignIn.classList.remove('role-label-inactive');
                teacherLabelSignIn.classList.add('role-label-active');
            } else {
                teacherLabelSignIn.classList.remove('role-label-active');
                teacherLabelSignIn.classList.add('role-label-inactive');
                studentLabelSignIn.classList.remove('role-label-inactive');
                studentLabelSignIn.classList.add('role-label-active');
            }

            console.log('Sign In Role:', selectedRoleInputSignIn.value);
        });
    }

    const signInButton = document.getElementById('signIn');
    const signUpButton = document.getElementById('signUp');
    const container = document.getElementById('container');

    signInButton.addEventListener('click', () => {
        container.classList.remove('right-panel-active');
    });

    signUpButton.addEventListener('click', () => {
        container.classList.add('right-panel-active');
    });

    function hideMessages() {
        const alertBox = document.querySelector('.alert');
        if (alertBox) {
            setTimeout(() => {
                alertBox.style.opacity = '0';
                setTimeout(() => {
                    alertBox.style.display = 'none';
                }, 500);
            }, 5000);
        }
    }

    hideMessages();
});