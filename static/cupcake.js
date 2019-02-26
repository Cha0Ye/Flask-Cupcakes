

async function getAllCupcakes(){
    let response = await $.get('http://localhost:5000/cupcakes');
    return response;
}

async function addCupcake(){
    await $.post('http://localhost:5000/cupcakes',{flavor:''})
}


//wait for DOM to load
$(document).ready(async function(e){
    preventDefault(e);

   
    let $addCupCake = $('#add-cupcake');
    let $listItem = $("#cupcake-list");
    
    
    
    async function updateCupcakeList(){
        let {response} = await getAllCupcakes();
        for (let cupcake of response){
            let newList = `<li> Flavor: ${cupcake.flavor} Size: ${cupcake.size} Rating: ${cupcake.rating} <img src='${cupcake.image}' width='100px'></li>`;
            
            $listItem.append(newList);
        }
    }
})