<?php
$software = $_POST["software-post"];
$ip = $_POST["ip-post"];

$command = escapeshellcmd("python3 /var/www/html/remove.py '".$ip."' '".$software."'");
$output = shell_exec($command);
echo $output;
?>

<html>
<head>
  <title>Software Verwijderen</title>
</head>
<br>
<br>
<form>
<input type="button" value="Ga terug" onclick="history.back()">
