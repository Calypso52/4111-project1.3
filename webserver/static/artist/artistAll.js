// show all data
function getFullArtistTable(data) {
    $.each(data, function(i, item){
        let artist_item= $(`<tr>
                                <th scope="row">${i + 1}</th>
                                <td>${item.name}</td>
                                <td>${item.gender}</td>
                                <td>${item.popularity}</td>
                                <td>${item.genre}</td>
                                <td>${item.follower}</td>
                            </tr>`);
        $("#artistOverviewTbody").append(artist_item);
    })
}

$(document).ready(function(){
    getFullArtistTable(data);
})