// show all data
function getFullSongTable(data) {
    $.each(data, function(i, item){
        let song_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.popularity}</td>
                                <td>${item.dancibility}</td>
                                <td>${item.energy}</td>
                                <td>${item.speechiness}</td>
                                <td>${item.liveness}</td>
                                <td>${item.tempo}</td>
                            </tr>`);
        $("#songOverviewTbody").append(song_item);
    })
}

$(document).ready(function(){
    getFullSongTable(data);

    $("#songAllSearch").click(function() {
        window.location.href = `/song/all`;
    })
})