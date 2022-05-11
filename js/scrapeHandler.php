<?php
    //header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    $url = $_REQUEST['url'];
    $pdf_folder = $_REQUEST['PDFPath'];
    // $url = "https://suchen.mobile.de/fahrzeuge/details.html?id=334088795&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&pageNumber=1&ref=quickSearch&scopeId=C&action=topOfPage&top=1:1&searchId=11102c5d-a525-03f7-3338-165c87bbe525";
    // $pdf_folder = "/home/azazel/Desktop";
    scrape($url, $pdf_folder);
    //$response = array('url' => $url);
    //echo json_encode($response);

    function scrape($url, $pdf_folder) {
        $path = dirname(__FILE__);
        $path = join_paths($path, 'pythonScripts', 'pyScraper.sh');
        $command = $path.' "'.$url.'"'.' "'.$pdf_folder.'"';
        $output = shell_exec($command);

        echo json_encode(json_decode($output, true));
    }

    function join_paths() {
        $paths = array();
    
        foreach (func_get_args() as $arg) {
            if ($arg !== '') { $paths[] = $arg; }
        }
    
        return preg_replace('#/+#','/',join('/', $paths));
    }

?>