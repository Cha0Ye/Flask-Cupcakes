

async function getAllCupcakes(){
    let response = await $.get('http://localhost:5000/cupcakes');
    return response;
}


//wait for DOM to load
$(document).ready(async function(e){
    let {response} = await getAllCupcakes();

    let $listItem = $("#cupcake-list");
    for (let cupcake of response){
        let newList = `<li> Flavor: ${cupcake.flavor} Size: ${cupcake.size} Rating: ${cupcake.rating} <img src='${cupcake.image}' width='100px'></li>`;
        
        $listItem.append(newList);
    }
    
})