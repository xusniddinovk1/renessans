$(document).ready(function () {
    $(".grid-gallery").sortable({
        items:".grid-item",
        handle:".grid-link",
        cursor:"grabbing",
        containment: "parent",
        tolerance:"pointer",

    })

    
    $(".grid-gallery").disableSelection();
    
})