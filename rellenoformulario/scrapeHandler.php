<?php
    //header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    // $url = $_REQUEST['url'];
    // $pdf_folder = $_REQUEST['PDFPath'];
    $url = "https://www.autoscout24.fr/offres/citroen-c4-coupe-hdi-92-pack-ambiance-diesel-blanc-db0326ea-70ea-43c5-8347-570ede1b752d?sort=standard&desc=0&lastSeenGuidPresent=false&cldtsrc=listPage&cldtidx=2&search_id=dnskdjiknc&source=listpage_search-results";
    $pdf_folder = "/home/azazel/Desktop";
    scrape($url, $pdf_folder);

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