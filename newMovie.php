<?php
	set_time_limit(0);

	ob_start();
	$oldtime=0;
	while(true){
		$newtime=filemtime("microblog/action.csv");
		if ($newtime>$oldtime){
			$file=file("microblog/action.csv");
			$lastrow=array_pop($file);
			echo $lastrow;
			ob_flush();
			flush();
			//sleep(3);
			$oldtime=$newtime;
		}
	}



?>
