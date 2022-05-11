const btn = document.querySelector(".btn");
const url = "https://suchen.mobile.de/fahrzeuge/details.html?id=334088795&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&pageNumber=1&ref=quickSearch&scopeId=C&action=topOfPage&top=1:1&searchId=11102c5d-a525-03f7-3338-165c87bbe525";

btn.addEventListener("click", function(e){
    e.preventDefault();
    $.ajax({
        url: "http://localhost:8000/scrapeHandler.php",
        data: {
            url: url,
            PDFPath: '/home/azazel/Desktop'
        },
        dataType: "json",
    });
});