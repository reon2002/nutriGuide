document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("addNewFact").addEventListener("click", function(event) {
        event.preventDefault();

        var overallDiv = document.querySelector('.overall');
        var newOverallDiv = overallDiv.cloneNode(true);

        overallDiv.parentNode.insertBefore(newOverallDiv, overallDiv.nextSibling);
    });
});
