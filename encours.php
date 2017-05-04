<!DOCTYPE html>
<html>
<head>
	<title>Enquêtes en cours</title>
</head>
<body>

<?php 
	require_once("require.php");
?>
<h1>Enquêtes en cours</h1>
<p/>

<?php
	// Récupperation de l'id dans le la session
	$idSal= $_SESSION['id'];
	// Connexion au serveur
	$connexion=new DAOConnexionBD();
	$db=$connexion->getDb();
	// Requete envoyé au serveur
	$resultat = $db->query("Select id, libelle, detail, dateDebut, dateFin from Question where dateDebut<=Current_date() and dateFin>=Current_date() and id not in(select idQuestion from reponse where idSalarie=$idSal)");
?>
<table border="1">
<th>Question</th> 
<?php
	// Listage des questions de la base de données
	while($ligne=$resultat->fetch()){
		$id=$ligne['id'];
		$libelle=$ligne['libelle'];

		echo ("<tr><td><a href='question.php?numQ=$id'>$id) $libelle</a></td></tr>");
	}
?>

</table>