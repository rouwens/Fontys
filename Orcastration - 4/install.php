<?php
$software = $_POST["software-post"];
$ip = $_POST["ip-post"];

$command = escapeshellcmd("python3 /var/www/html/install.py '".$ip."' '".$software."'");
$output = shell_exec($command);
echo $output;
?>

<html>
<head>
  <title>Software installeren</title>
</head>
<br>
<br>
<form>
<input type="button" value="Ga terug" onclick="history.back()">
