document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".btn-add-to-cart").forEach(function (button) {
        button.addEventListener("click", function () {
            button.classList.add("btn-loading");
            setTimeout(function () {
                button.classList.remove("btn-loading");
            }, 600);
        });
    });

    document.querySelectorAll(".quantity-input").forEach(function (input) {
        input.addEventListener("change", function () {
            var value = Number(input.value);
            if (Number.isNaN(value) || value < 1) {
                input.value = 1;
            }
        });
    });
});
