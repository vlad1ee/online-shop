const sendData = async (url, data) => {
    
    const response = await fetch(url, {
        method: 'POST',
        body: data,
        headers: {
            "X-Requested-With": "XMLHttpRequest",

          },

    });

    if (!response.ok) {
        throw new Error('Ошибка');
    }
    return await response.json();
}

    const userForm = document.querySelector('.user-form');

    userForm.addEventListener('submit', e => {
        e.preventDefault();

        const formData = new FormData(userForm);

        const url = document.getElementById("url")["value"];

        sendData(url, formData)
            .then(() => {userForm.reset()});
    })
