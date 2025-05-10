document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("container");
    const registerBtn = document.getElementById("register");
    const loginBtn = document.getElementById("login");

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

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function validatePassword(password) {
        return password.length >= 6;
    }

    function showError(input) {
        input.classList.add("error"); // Add error class to input
    }

    function clearErrors() {
        document.querySelectorAll(".error").forEach(input => input.classList.remove("error")); // Remove error class from inputs
    }

    signUpForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const name = signUpForm.querySelector("input[type='text']");
        const email = signUpForm.querySelector("input[type='email']");
        const password = signUpForm.querySelector("input[type='password']");

        let isValid = true;

        if (name.value.trim() === "") {
            showError(name); // Highlight name input
            isValid = false;
        }
        if (!validateEmail(email.value)) {
            showError(email); // Highlight email input
            isValid = false;
        }
        if (!validatePassword(password.value)) {
            showError(password); // Highlight password input
            isValid = false;
        }

        if (isValid) {
            signUpForm.submit();
        }
    });

    signInForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const email = signInForm.querySelector("input[type='email']");
        const password = signInForm.querySelector("input[type='password']");

        let isValid = true;

        if (!validateEmail(email.value)) {
            showError(email); // Highlight email input
            isValid = false;
        }
        if (!validatePassword(password.value)) {
            showError(password); // Highlight password input
            isValid = false;
        }

        if (isValid) {
            signInForm.submit();
        }
    });
});
