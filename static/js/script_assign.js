$(document).ready(function(){
    $("button").click(function(){
        /* Set all the cells in columns with THEHEADING in the heading to red */
    columnTh = $("table th:contains('Assign')"); // Find the heading with the text THEHEADING
    columnIndex = columnTh.index() + 1; // Get the index & increment by 1 to match nth-child indexing
    $('table tr td:nth-child(' + columnIndex + ')').css("color", "#F00"); // Set all the elements with that index in a tr red
    columnTh.css("color", "#F00"); // Set the heading red too!
});
});
