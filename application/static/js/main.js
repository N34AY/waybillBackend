const baseUrl = window.location.hostname

const menuItems = document.getElementsByClassName('vertical_menu_item')
var currentUrl = window.location.pathname
currentUrl = currentUrl.split('?')[0]

if ((window.location.href).indexOf(currentUrl) != -1) {
    for (let i = 0; i < menuItems.length; i++) {
        var itemUrl = menuItems[i].href
        if (itemUrl.indexOf(currentUrl) != -1) {
            menuItems[i].classList.add('active')
        }
    }
}

function deleteUser(user) {
    var id = user.dataset.id
    var name = user.dataset.name
    var deleteConfirm = confirm("Удалить пользователя " + name + "?")
    if (deleteConfirm) {
        axios.delete(`delete/${id}`)
            .then(response => document.location.reload())
            .catch(error => alert('Ошибка при удалении пользователя!'))
    }
}