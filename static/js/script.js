$(document).ready(function () {

    // 🔍 Satellite Search
    $("#search").on("keyup", function () {
        let value = $(this).val().toLowerCase();

        $("#satelliteList li").filter(function () {
            $(this).toggle($(this).text().toLowerCase().includes(value));
        });
    });

    // 🧠 Form Validation
    $("form").on("submit", function () {

        let email = $("input[type='email']").val();
        let password = $("input[type='password']").val();

        if (email && !email.includes("@")) {
            alert("Enter valid email");
            return false;
        }

        if (password && password.length < 5) {
            alert("Password must be at least 5 characters");
            return false;
        }

    });

});