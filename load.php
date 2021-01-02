<?php
for ($x=1800;$x>0;$x--){
      echo "\r                         \r";
      echo "\r\e[90m[\e[1;91m-\e[90m]\e[1;93mWaiting In 30 Minute\033[1;97m...\e[90m (\033[1;91m". $x."\033[90m)"; 
      sleep (1);
      echo "\r";
}
?>
