$(document).ready(function(){
    $("#tracklistAllSearch").click(function() {
        window.location.href = `/tracklist/all`;
    })

    $(document).on('input', "#popularity", function() {
        let val = $(this).val();
        $("#rangeval").html(val);
    })
})