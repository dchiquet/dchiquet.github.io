<!DOCTYPE html>
<html>
<head>
	<title>Connexion</title>
</head>
<body>
<h1>Menu</h1>
<a href="encours.php">Enquetes en cours</a><br>
<a href="termine.php">Enquetes termine</a><br>
<a href="deconnexion.php">Deconnexion</a><br>
<?php
session_start();
echo "Session : ".$_SESSION['prenom'].' '.$_SESSION['nom'];
?>