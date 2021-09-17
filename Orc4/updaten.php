<?php
# Voor deze tool is sshpass op de server kant zelf nodig!!!!!!!

if (!empty($_SERVER['HTTP_CLIENT_IP']))
  {
    $ip_address = $_SERVER['HTTP_CLIENT_IP'];
  }
//whether ip is from proxy
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
  {
    $ip_address = $_SERVER['HTTP_X_FORWARDED_FOR'];
  }
//whether ip is from remote address
else
  {
    $ip_address = $_SERVER['REMOTE_ADDR'];
  }
#echo "Je IP adres is: ";
#echo $ip_address;
?>

<html>
<head>
  <title> Software Manager - Updaten</title>
   <link rel="stylesheet" href="main.css">
</head>
<div class="topnav">
<a href="index.php">Installeren</a>
<a href="uninstall.php">Verwijderen</a>
<a class="active" href="updaten.php">Systeem updaten</a>
<a href="passwd.php">Wachtwoord Veranderen</a>
</div>
<br>
<p> Om je systeem te updaten moet je het volgende doen </p> <br>
<p> 1) Open een terminal venster (crtl + alt + t) </p> <br>
<p> 2) Type in het venster system-update en druk op enter </p> <br>

</html>
