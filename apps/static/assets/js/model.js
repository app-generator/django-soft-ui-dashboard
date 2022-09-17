
document.querySelector('.list-group').addEventListener('click' , (e) => {
    if (e.target.nodeName === 'A') {
        if (e.target.className.includes('edit')) {
            editAction(e.target.id)
            requestAction = 'put'
        } else if (e.target.className.includes('delete'))
            deleteAction(e.target.id)

    }
})

const deleteAction = (id) => {
    const modelName = 'books'
    fetch(`/api/${modelName}/${id}/`,{
        method: 'DELETE',
        headers: {
            'Authorization': `token ${token}`
        }
    })
        .then(response => response.json())
        .then(res => {
            location.reload()
            console.log(res)
        })
        .catch(err => {console.log(err)})
}

const editAction =  (id) => {
    // get data from template
    const item = data.filter(d => d.id.toString() === id)[0]
    console.log(item,data)
    document.getElementById('name').value = item.name
    document.getElementById('id').value = item.id

}