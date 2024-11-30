document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const categoryFilter = document.getElementById("categoryFilter");
    const workoutCards = document.querySelectorAll(".workout-card");

    function filterWorkouts() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCategory = categoryFilter.value;

        workoutCards.forEach(card => {
            const title = card.querySelector("h4").textContent.toLowerCase();
            const category = card.getAttribute("data-category");

            // Check if the card matches the search term and category
            const matchesSearch = title.includes(searchTerm);
            const matchesCategory = selectedCategory === "all" || category === selectedCategory;

            if (matchesSearch && matchesCategory) {
                card.style.display = "flex";
            } else {
                card.style.display = "none";
            }
        });
    }

    // Add event listeners for search and category filter
    searchInput.addEventListener("input", filterWorkouts);
    categoryFilter.addEventListener("change", filterWorkouts);

    // Initial render: ensure all cards are visible
    filterWorkouts();
});
