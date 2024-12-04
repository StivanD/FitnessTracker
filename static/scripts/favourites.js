function toggleFavourite(button) {
    const workoutId = button.getAttribute("data-pk");
    const icon = button.querySelector("i");

    // Determine whether the workout is already favourited based on the icon
    const isFavourited = icon.classList.contains('fa-solid');

    fetch(`/workouts/${workoutId}/toggle-favourite/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json',
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'added to') {
                icon.classList.remove('fa-regular');
                icon.classList.add('fa-solid');
            } else if (data.status === 'removed from') {
                icon.classList.remove('fa-solid');
                icon.classList.add('fa-regular');
            }
        })
        .catch(error => console.error('Error:', error));
}

function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue || '';
}
