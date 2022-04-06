$(document).ready(function(){
    $("#songAllSearch").click(function() {
        window.location.href = `/song/all`;
    })

    $(document).on('input', "#songPopularityFind", function() {
        let val = $(this).val();
        $("#songPopularityValFind").html(val);
    })

    $(document).on('input', "#songDancibilityFind", function() {
        let val = $(this).val();
        $("#songDancibilityValFind").html(val);
    })

    $(document).on('input', "#songEnergyFind", function() {
        let val = $(this).val();
        $("#songEnergyValFind").html(val);
    })

    $(document).on('input', "#songSpeechinessFind", function() {
        let val = $(this).val();
        $("#songSpeechinessValFind").html(val);
    })

    $(document).on('input', "#songLivenessFind", function() {
        let val = $(this).val();
        $("#songLivenessValFind").html(val);
    })

    $(document).on('input', "#songTempoFind", function() {
        let val = $(this).val();
        $("#songTempoValFind").html(val);
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