const btn = document.querySelector(".btn");
const url = "https://www.mobile.de/es/Veh%C3%ADculo/Volkswagen-Golf-VII-Lim.-Trendline-BMT/vhc:car,ms1:25200__,dmg:false/pg:vipcar/344493567.html";

btn.addEventListener("click", function(e){
    e.preventDefault();
    $.ajax({
        url: "http://localhost:8000/scrapeHandler.php",
        data: {"url": url},
        dataType: "json",
    });
});