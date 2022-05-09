<?php
    //header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    //$url = $_REQUEST['url'];
    $url = "https://www.mobile.de/es/Veh%C3%ADculo/Volkswagen-VW-Passat-3BG,-springt-sofort-an/vhc:car,ms1:25200_25_,frn:2000,prx:2000,ful:diesel,dmg:false/pg:vipcar/344688977.html";
    scrape($url);
    // $response = array('url' => $url);
    // echo json_encode($response);

    function scrape($url) {
        $path = dirname(__FILE__);
        $path = join_paths($path, 'pythonScripts', 'pyScraper.py');
        $command = 'python3 '.$path.' "'.$url.'"'.' &';
        $output = shell_exec($command);;
        json_encode($output);
        echo $output;
    }

    function join_paths() {
        $paths = array();
    
        foreach (func_get_args() as $arg) {
            if ($arg !== '') { $paths[] = $arg; }
        }
    
        return preg_replace('#/+#','/',join('/', $paths));
    }

?>