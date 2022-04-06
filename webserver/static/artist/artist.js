$(document).ready(function(){
    $("#artistAllSearch").click(function() {
        window.location.href = `/artist/all`;
    })

    // switch bar control
    var triggerTabList = [].slice.call(document.querySelectorAll('#myTab button'))
    triggerTabList.forEach(function (triggerEl) {
        var tabTrigger = new bootstrap.Tab(triggerEl)

        triggerEl.addEventListener('click', function (event) {
            event.preventDefault()
            tabTrigger.show()
        })
    })

    $(document).on('input', "#artistPopularity", function() {
        let val = $(this).val();
        $("#artistRangeval").html(val);
    })

    $(document).on('input', "#artistFollower", function() {
        let val = $(this).val();
        $("#artistFollowerRangeval").html(val);
    })

    $(document).on('input', "#artistPopularityAdd", function() {
        let val = $(this).val();
        $("#artistRangevalAdd").html(val);
    })

    $(document).on('input', "#artistFollowerAdd", function() {
        let val = $(this).val();
        $("#artistRangevalAddFollower").html(val);
    })

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})