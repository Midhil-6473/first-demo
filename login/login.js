document.addEventListener('DOMContentLoaded', () => {
    const roleBtns = document.querySelectorAll('.role-btn');

    roleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            roleBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            // Optional: you can log the selected role or update a hidden input
            const selectedRole = btn.getAttribute('data-role');
            console.log(`Role switched to: ${selectedRole}`);
        });
    });
});
