<?php
    //header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    $url = $_REQUEST['url'];
    $pdf_folder = $_REQUEST['PDFPath'];
    // $url = "https://www.autoscout24.es/anuncios/citroen-xsara-2-0-hdi-sx-diesel-a3eb3509-64f3-417b-b451-b7c731f3c180?sort=standard&desc=0&lastSeenGuidPresent=true&cldtsrc=listPage&cldtidx=1&search_id=n5ee1mso4o&source=listpage_search-results";
    // $pdf_folder = "/home/azazel/Desktop";
    scrape($url, $pdf_folder);

    function scrape($url, $pdf_folder) {
        $path = dirname(__FILE__);
        $path = join_paths('python3 '.$path, 'pythonScripts', 'pyScraper.py');
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