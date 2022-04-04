// show all data
function getFullAlbumTable(data) {
    $.each(data, function(i, item){
        let listener_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.release_time}</td>
                                <td>${item.popularity}</td>
                            </tr>`);
        $("#albumOverviewTbody").append(listener_item);
    })
}

$(document).ready(function(){
    getFullAlbumTable(data);
})