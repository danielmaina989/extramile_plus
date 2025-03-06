document.addEventListener("DOMContentLoaded", function () {
    const deleteBtn = document.getElementById("delete-btn");
    const deleteForm = document.getElementById("delete-form");

    if (deleteBtn && deleteForm) {
        deleteBtn.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default form submission

            Swal.fire({
                title: "Are you sure?",
                text: "This action cannot be undone!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#d33",
                cancelButtonColor: "#6c757d",
                confirmButtonText: "Yes, Delete",
                cancelButtonText: "Cancel"
            }).then((result) => {
                if (result.isConfirmed) {
                    deleteForm.submit();
                }
            });
        });
    }
});
