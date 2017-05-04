<?php
	$id=$_GET['numQ'];
?>

<!DOCTYPE html>
<html>
<head>
	<title>Question n°<?php echo $id; ?></title>
</head>
<body>
<?php 
	require_once("require.php");
?>
<h1>Question sélectionnée</h1>
<p/>

<?php
	// Connexion au serveur
	$connexion=new DAOConnexionBD();
	$db=$connexion->getDb();
	// Requete envoyé au serveur
	$resultat = $db->query("Select id, libelle, detail, dateDebut, dateFin from Question where id=$id");
	// Lecture du résultat
	while($ligne=$resultat->fetch()){
		echo $ligne['id'].") ".$ligne['libelle'];
	}
?>
<!-- Formulaire de réponse du salarié -->
<form method="post" action="<?php echo ('reponse.php?numQ='.$id)?>">
	<table>
		<tr>
		<td>
			<INPUT type= "radio" name="reponse" value="O"/> Oui
		</td>
		<td>		
			<INPUT type= "radio" name="reponse" value="N"/>	Non
		</td>
		</tr>
		<tr>
		<td>
			<input type="submit" value="Envoyer"/>
		</td>
		</tr>
	</table>
</form>