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
        const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/; 
        return re.test(password);
    }

    function showError(input, message) {
        input.classList.add("error");
        const errorElement = document.createElement("div");
        errorElement.classList.add("error-message");
        errorElement.textContent = message;
        input.parentNode.appendChild(errorElement);
    }

    function clearErrors() {
        document.querySelectorAll(".error").forEach(input => input.classList.remove("error"));
        document.querySelectorAll(".error-message").forEach(msg => msg.remove());
    }

    signUpForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const name = signUpForm.querySelector("input[name='username']");
        const email = signUpForm.querySelector("input[name='email']");
        const password = signUpForm.querySelector("input[name='password1']");
        const confirmPassword = signUpForm.querySelector("input[name='password2']");

        let isValid = true;

        if (name.value.trim() === "") {
            showError(name);
            isValid = false;
        }

        if (!validateEmail(email.value)) {
            showError(email);
            isValid = false;
        }

        if (!validatePassword(password.value)) {
            showError(password, "Password must be at least 6 characters long, contain a number, a lowercase, and an uppercase letter.");
            isValid = false;
        }

        if (password.value !== confirmPassword.value) {
            showError(confirmPassword, "Passwords do not match.");
            isValid = false;
        }

        if (isValid) {
            signUpForm.submit();
        }
    });

    signInForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const username = signInForm.querySelector("input[name='username']");
        const password = signInForm.querySelector("input[name='password']");

        let isValid = true;

        if (username.value.trim() === "") {
            showError(username);
            isValid = false;
        }
        
        if (password.value.trim() === "") {
            showError(password);
            isValid = false;
        }

        if (isValid) {
            signInForm.submit();
        }
    });
});
