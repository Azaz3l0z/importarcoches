<?php
    include('simple_html_dom.php');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    
    $url = "https://www.mobile.de/es/Veh%C3%ADculo/Volkswagen-Golf-VII-Lim.-Trendline-BMT/vhc:car,ms1:25200__,dmg:false/pg:vipcar/344493567.html";
    //$url = $_REQUEST["url"]; 
    data($url);
    function data($url){
        $html = file_get_html($url);
        $data = preg_match_all('/<div class="g-row"/', $html);
    }

?>