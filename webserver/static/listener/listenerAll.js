// show all data
function getFullListenerTable(data) {
    $.each(data, function(i, item){
        let listener_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.gender}</td>
                                <td>${item.age}</td>
                            </tr>`);
        $("#listenerOverviewTbody").append(listener_item);
    })
}

$(document).ready(function(){
    getFullListenerTable(data);
})