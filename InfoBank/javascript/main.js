function getCardInfo() {
    localStorage.clear()
    let text = document.querySelector("#card_bin").value.replace((/\s/g),'');
    fetch(`${window.location.href}generate_answer/${text}`).then(function (response) {
        return response.json()
    })
        .then(function (data) {
            localStorage.setItem('info', JSON.stringify(data))
            window.open('bank_info.html','_self')
        })
        .catch(error => window.open('error.html','_self'))
        // .catch(error => alert('Некорректные данные'))
}
