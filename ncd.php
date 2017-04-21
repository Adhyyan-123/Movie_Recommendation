<?php
	
	// Set up for SSE
	ob_start();
	
	header("Content-type: text/event-stream");
	
	$oldtime = filemtime("ncd.txt");
	
	while(true)
	{
		clearstatcache();
		$newtime = filemtime("ncd.txt");
		
		if($newtime != $oldtime)
		{
			//The file is modified. That means 'B' typed something.
			//Open and read the last line from the file.
			//Read the file into an array and return the last one
			$msgarr = file("ncd.txt");
			$latestmsg = array_pop($msgarr);
			//echo parent.alert("12132231");
			
			//Send the event
			echo "event:msg\n";
			echo "retry:100\n";
			echo "data: $latestmsg\n\n";
			ob_flush();
			flush();
			
			$oldtime = $newtime;
			$_SESSION["modtime"] = $newtime; 
		}
		
		//We will check every 1 seconds
		sleep(1);
	}

?>