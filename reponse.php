<?php  
	require_once("require.php");

	// Récuperation du numéro du salarié
	$idS=$_SESSION['id'];
	// Récupération du numéro de la question
	$idQ=$_GET['numQ'];
	// Récupération de la réponse du salarié
	$rep=$_POST['reponse'];

	// Connexion au serveur
	$connexion=new DAOConnexionBD();
	$db=$connexion->getDb();
	// Préparation requete envoyé au serveur
	$requete = $db->prepare("Insert into reponse values (:idS, :idQ, :rep)");
	$requete->bindValue(':idS', $idS);
	$requete->bindValue(':idQ', $idQ);
	$requete->bindValue(':rep', $rep);
	// Execution de la requete
	$requete->execute();
	
?>