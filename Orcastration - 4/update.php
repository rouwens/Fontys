<?php
$ip = $_POST["ip-post"];

$command = escapeshellcmd("python3 /var/www/html/update.py '".$ip."'");
$output = shell_exec($command);
echo $output;
?>

<html>
<head>
  <title>Systeem updaten</title>
</head>
<br>
<br>
<form>
<input type="button" value="Ga terug" onclick="history.back()">
