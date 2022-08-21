let frm = document.querySelector('#frm');
let btn = document.querySelector('#btn');
let url = frm.action;
let token = frm.querySelector('input[name=csrfmiddlewaretoken]').value;

btn.addEventListener("click", function(e){
    e.preventDefault();
    let username = frm.querySelector('#txtusername').value;
    let comment = frm.querySelector('#txtcomment').value;

    fetch( url, {
        method : 'post',
        headers : { "x-csrftoken" : token },
        body : JSON.stringify(
            {
                'username' : username,
                'comment' : comment,
            }
        )
                }
        ).then( response => response.json() )
     
})




