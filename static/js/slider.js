const signUpButton1 = document.getElementById('signUp');
const signInButton1 = document.getElementById('signIn');
const container1 = document.getElementById('container1');

signUpButton1.addEventListener('click', () => {
    container1.classList.add('right-panel-active');
});

signInButton1.addEventListener('click', () => {
    container1.classList.remove('right-panel-active');
});