document.addEventListener("DOMContentLoaded",()=>{
    const searchInput = document.querySelector(".searchbar");
    const suggestionContainer = document.querySelector(".suggestions");

    searchInput.addEventListener("input", ()=>{
        const query=this.value.trim();
        if (query !== ""){
            fetch(`/search-fruits/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionContainer.innerHTML = ""; // Clear previous suggestions
                    data.fruits.forEach(fruit => {
                        const suggestionItem = document.createElement("div");
                        suggestionItem.classList.add("suggestion");
                        suggestionItem.textContent = fruit;
                        suggestionItem.addEventListener("click", function() {
                            window.location.href = `/search-results/?fruit=${fruit}`;
                        });
                        suggestionContainer.appendChild(suggestionItem);
                    });
                })
                .catch(error => console.error("Error fetching fruits:", error));
        } else {
            suggestionContainer.innerHTML = ""; // Clear suggestions if search query is empty
        }
    });
});