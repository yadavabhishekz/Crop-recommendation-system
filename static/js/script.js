document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("cropForm");
    form.addEventListener("submit", (e) => {
        const inputs = form.querySelectorAll("input");
        for (const input of inputs) {
            if (input.value.trim() === "") {
                alert("Please fill out all fields!");
                e.preventDefault();
                return;
            }
        }
    });
});
