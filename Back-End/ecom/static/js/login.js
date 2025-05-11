document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("container");
    const registerBtn = document.getElementById("register");
    const loginBtn = document.getElementById("login");

    // Toggle between sign-up and sign-in forms
    registerBtn.addEventListener("click", () => {
        clearErrors();
        container.classList.add("active");
    });

    loginBtn.addEventListener("click", () => {
        clearErrors();
        container.classList.remove("active");
    });

    const signUpForm = document.querySelector(".sign-up form");
    const signInForm = document.querySelector(".sign-in form");

    // Email validation regex
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Password length validation (at least 6 characters)
    function validatePassword(password) {
        return password.length >= 6;
    }

    // Function to add error class to invalid inputs
    function showError(input) {
        input.classList.add("error"); // Add error class to input
    }

    // Function to clear previous error classes
    function clearErrors() {
        document.querySelectorAll(".error").forEach(input => input.classList.remove("error")); // Remove error class from inputs
    }

    // Sign-Up form validation
    signUpForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const name = signUpForm.querySelector("input[type='text']");
        const email = signUpForm.querySelector("input[type='email']");
        const password = signUpForm.querySelector("input[type='password']");

        let isValid = true;

        // Validate name (not empty)
        if (name.value.trim() === "") {
            showError(name); // Highlight name input
            isValid = false;
        }

        // Validate email format
        if (!validateEmail(email.value)) {
            showError(email); // Highlight email input
            isValid = false;
        }

        // Validate password length
        if (!validatePassword(password.value)) {
            showError(password); // Highlight password input
            isValid = false;
        }

        if (isValid) {
            signUpForm.submit(); // Submit form if valid
        }
    });

    // Sign-In form validation
    signInForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const username = signInForm.querySelector("input[type='text']");
        const password = signInForm.querySelector("input[type='password']");

        let isValid = true;

        // Validate username (not empty)
        if (username.value.trim() === "") {
            showError(username); // Highlight username input
            isValid = false;
        }

        // Validate password length
        if (!validatePassword(password.value)) {
            showError(password); // Highlight password input
            isValid = false;
        }

        if (isValid) {
            signInForm.submit(); // Submit form if valid
        }
    });
});
