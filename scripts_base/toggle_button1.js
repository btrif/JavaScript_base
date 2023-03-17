const btn = document.getElementById('btn');

btn.addEventListener('click', function onClick(event) {
    const backgroundColor = btn.style.backgroundColor;

    if (backgroundColor === 'salmon') {
        btn.style.backgroundColor = 'green';

        // 👇️ optionally change text color
        // btn.style.color = 'white';
    } else if (backgroundColor === "green") {
        btn.style.backgroundColor = 'salmon';

        // 👇️ optionally change text color
        // btn.style.color = 'blue';
    }

else{
    btn.style.backgroundColor = 'salmon';
}

});