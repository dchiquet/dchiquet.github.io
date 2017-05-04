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
<h1>Statistiques de la question sélectionnée</h1>
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
	// Recuperation des réponses
	$resultat = $db->query("Select idSalarie, idQuestion, reponseON from Reponse");
	$oui=$non=$tot=0;
	while($ligne=$resultat->fetch()){
		if($ligne['idQuestion']==$id){
			if($ligne['reponseON']=='N')
				$non++;
			else
				$oui++;
			$tot++;
		}
	}
	$oui = $oui/$tot*100;
	$non = $non/$tot*100;

	
?>

<form method="post" action="<?php echo ('reponse.php?numQ='.$id)?>">
	<table>
		<tr>
		<td>
			<?php// Affichage du resultat
				echo (int) $oui; ?> % de Oui
		</td>
		<td>		
			<?php// Affichage du resultat
				echo (int) $non; ?> % de Non
		</td>
		</tr>
		<tr>
		<td>
			
		</td>
		</tr>
	</table>
</form>