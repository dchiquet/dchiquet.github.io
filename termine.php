<!DOCTYPE html>
<html>
<head>
	<title>Questions Terminées</title>
</head>
<body>

<?php 
	require_once("require.php");
?>
<h1>Statistiques des questions terminées</h1>
<p/>
<?php
	require_once("DAOConnexionBD.php");
	

	$idSal= $_SESSION['id'];
	$connexion=new DAOConnexionBD();
	$db=$connexion->getDb();
	$resultat = $db->query("Select id, libelle, detail, dateDebut, dateFin 
							from Question 
							where dateFin<Current_date()");
?>
<table border="1">
<th>Question</th> 

<?php
	while($ligne=$resultat->fetch()){
		$id=$ligne['id'];
		$libelle=$ligne['libelle'];

		echo ("
			
				<tr><td><a href='stat.php?numQ=$id'>$id) $libelle</a></td></tr>");
	}
?>



</body>
</html>