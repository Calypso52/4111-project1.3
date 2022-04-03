// show all data
function getFullListenerTable(data) {
    $.each(data, function(i, item){
        let listener_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.release_time}</td>
                                <td>${item.popularity}</td>
                            </tr>`);
        $("#listenerOverviewTbody").append(listener_item);
    })
}

$(document).ready(function(){
    getFullListenerTable(data);

    $("#albumAllSearch").click(function() {
        window.location.href = `/listener/all`;
    })
})