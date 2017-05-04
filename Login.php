<!DOCTYPE html>
<html>
<head>
	<title>Connexion</title>
</head>
<body>
Identification

<form action="LoginVerif.php" method="post">
<table>
	<tr>
		<td>login</td>
		<td><input type="text" name="login"/></td>
	</tr>
	<tr>
		<td>password</td>
		<td><input type="password" name="mdp"/></td>
	</tr>
	<tr><td><input type="submit" value="Connexion"></td></tr>
</table>
</form>
<?php
session_start();
if (isset($_GET['mss'])) {
	if ($_GET['mss']==0) {
		echo ('Deconnexion reussi');
	}elseif ($_GET['mss']==1){
		echo "Veuillez vous connecter";
	}elseif ($_GET['mss']==2) {
		echo "Identifiant ou mot de passe incorrect";
	}
}

?>