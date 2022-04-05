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
})