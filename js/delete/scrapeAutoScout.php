<?php
    header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    
    $url = $_REQUEST["url"]; 
    data($url);

    function data($url) {   
        // Conseguimos el html
        $html = file_get_html($url);
        
        // maps
        $var = array();
        $pattern = '/href="https:\/\/maps\.google\.com(.*?)"/';
        preg_match($pattern, $html, $var);        
        $var = substr($var[0], 6, -1);
        
        // Obtenemos el JSON que define la pagina
        $iniTag = '<script id="__NEXT_DATA__" type="application/json">';
        $endTag = '</script>';
        $iniPos = strpos($html, $iniTag);
        $htmlSlice = substr($html, $iniPos + strlen($iniTag));
    
        $endPos = strpos($htmlSlice, $endTag);
        $htmlSlice = substr($htmlSlice, 0, $endPos);

        $data = json_decode($htmlSlice, TRUE);
        $vehicle = $data['props']['pageProps']['listingDetails']['vehicle']; 
        $images = $data['props']['pageProps']['listingDetails']['images'];

        // Variables
        $marca = $vehicle["make"];
        $model = $vehicle["model"];
        $kms = $vehicle["mileageInKmRaw"];
        $year = $vehicle["firstRegistrationDate"];
        $power = $vehicle["powerInHp"];
        $change = $vehicle["transmissionType"];
        $c02 = $vehicle["co2emissionInGramPerKm"]["formatted"];
        $fuel = $vehicle["fuelCategory"]["formatted"];
        $modelVersion = $vehicle["modelVersionInput"];
    
        // Return
        $response = array(
            'marca' => $marca,
            'model' => $model,
            'kms' => $kms,
            'year' => $year,
            'power' => $power,
            'change' => $change,
            'c02' => $c02,
            'fuel' => $fuel,
            'var' => $var,
            'modelVersion' => $modelVersion,
            'images' => $images
        );
        echo json_encode($response);
    }     
    
?>