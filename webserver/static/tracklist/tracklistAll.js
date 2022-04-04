// show all data
function getFullTracklistTable(data) {
    $.each(data, function(i, item){
        let tracklist_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.popularity}</td>
                            </tr>`);
        $("#tracklistOverviewTbody").append(tracklist_item);
    })
}

$(document).ready(function(){
    getFullTracklistTable(data);
})