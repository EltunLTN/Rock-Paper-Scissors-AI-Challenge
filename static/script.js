document.getElementById("resetBtn").addEventListener("click", () => {
    fetch("/reset")
        .then(res => res.json())
        .then(data => {
            alert("Game Reset!");
        });
});
