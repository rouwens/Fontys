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
  <title> Software Manager - installeren</title>
   <link rel="stylesheet" href="main.css">
</head>
<div class="topnav">
<a class="active" href="index.php">Installeren</a>
<a href="uninstall.php">Verwijderen</a>
<a href="updaten.php">Systeem updaten</a>
<a href="passwd.php">Wachtwoord Veranderen</a>

</div>
<br>
<?php
echo "Je IP adres is: ";
echo $ip_address;
?>
<h4> Vul hier je IP adres in dat hierboven staat </h4>
<form action="install.php" method="post">
    IP adres: <input type="text" name="ip-post"><br>
    <br>
    <h4>Selecteer het softwarepakket </h4>
    VLC <input type="radio" name="software-post" value="vlc"/> <br>
    GIMP <input type="radio" name="software-post" value="gimp"/> <br>
    Visualstudo Code <input type="radio" name="software-post" value="code"/> <br>
    Microsoft Teams <input type="radio" name="software-post" value="teams"/> <br>
    Keepass2 <input type="radio" name="software-post" value="keepass2"/> <br>
    Openshot <input type="radio" name="software-post" value="openshot"/> <br>
    Thunderbird <input type="radio" name="software-post" value="thunderbird"/> <br>
    <br>
    <input type="submit" value="Installeren">
</form>
<br>

</html>