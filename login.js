function toggleForms() {
    const loginForm = document.getElementById("login-form");
    const signupForm = document.getElementById("signup-form");
    const formTitle = document.getElementById("form-title");

    if (loginForm.classList.contains("active")) {
        loginForm.classList.remove("active");
        signupForm.classList.add("active");
        formTitle.textContent = "Create your account";
    } else {
        signupForm.classList.remove("active");
        loginForm.classList.add("active");
        formTitle.textContent = "Good to see you again";
    }
}

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    alert(`Logging in with email: ${email}`);
    // backend login functionality 
}

function signup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("emailSignup").value;
    const password = document.getElementById("passwordSignup").value;
    const age = document.getElementById("age").value;
    const bio = document.getElementById("bio").value;
    alert(`Signing up with name: ${name}, email: ${email}, age: ${age}`);
    // backend signup functionality
}