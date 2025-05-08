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

    function showError(input, message) {
        const errorElement = document.createElement("div");
        errorElement.classList.add("error-message");
        errorElement.style.color = "red";
        errorElement.style.fontSize = "12px";
        errorElement.textContent = message;
        input.parentNode.appendChild(errorElement);
    }

    function clearErrors() {
        document.querySelectorAll(".error-message").forEach(error => error.remove());
    }

    signUpForm.addEventListener("submit", function (event) {
        event.preventDefault();
        clearErrors();

        const name = signUpForm.querySelector("input[type='text']");
        const email = signUpForm.querySelector("input[type='email']");
        const password = signUpForm.querySelector("input[type='password']");

        let isValid = true;

        if (name.value.trim() === "") {
            showError(name, "Name is required.");
            isValid = false;
        }
        if (!validateEmail(email.value)) {
            showError(email, "Please enter a valid email address.");
            isValid = false;
        }
        if (!validatePassword(password.value)) {
            showError(password, "Password must be at least 6 characters.");
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
            showError(email, "Please enter a valid email address.");
            isValid = false;
        }
        if (!validatePassword(password.value)) {
            showError(password, "Password must be at least 6 characters.");
            isValid = false;
        }

        if (isValid) {
            signInForm.submit();
        }
    });
});
