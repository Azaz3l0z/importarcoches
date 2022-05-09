<?php
    //header('Content-Type: application/json');
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Methods: GET, OPTIONS");
    //$url = $_REQUEST["url"];
    $url = $_REQUEST['url'];
    scrape($url);
    // $response = array('url' => $url);
    // echo json_encode($response);

    function scrape($url) {
        $path = dirname(__FILE__);
        $path = join_paths($path, 'pyScraper.py');
        $command = 'python3 '.$path.' "'.$url.'"';
        $output = shell_exec($command);;
        json_encode($output);
        echo $command;
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