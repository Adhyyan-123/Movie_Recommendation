<?php
	extract($_GET);
	$images=fopen("images.txt","r");
	$lines=fread($images,filesize("images.txt"));
	$lines=explode("\n",$lines);
	$Response="";
	for($i=0;$i<sizeof($lines);$i++){
		$t=explode(":",$lines[$i]);
		if($t[0]==$img){
			$src=explode(" ",$t[1]);
			for($j=0;$j<sizeof($src);$j++){
				$src1=explode("-",$src[$j]);
				if($src1[0]==$section){
					$Response=$src1[1];
				}
			}
		}
	}
	echo $Response
?>
		
