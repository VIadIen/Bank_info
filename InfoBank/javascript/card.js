let answer = JSON.parse(localStorage.getItem('info'))
for (let key in answer) {
    let row = document.createElement('th')
    let col = document.createElement('td')
    row.innerHTML = `${key}`
    document.querySelector('.info_card>thead>tr').appendChild(row)
    col.innerHTML = key === 'Bank_Url' ? `<a href="http://${answer[key]}" target="_blank">${answer[key]}</a>` : `${answer[key]}`
    document.querySelector('.info_card>tbody>tr').appendChild(col)
}


