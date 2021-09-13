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
</div>
<br>
<?php
echo "Je IP adres is: ";
echo $ip_address;
?>
<h4> Vul hier het IP adres in dat hierboven staat </h4>
<form action="update.php" method="post">
    IP adres: <input type="text" name="ip-post"><br>
    <br>
    <input type="submit" value="Updaten">
</form>
<br>

</html>
