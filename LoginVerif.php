<?php 
	require_once("DAOConnexionBD.php");

	// Connexion au serveur
	$connexion=new DAOConnexionBD();
	$db=$connexion->getDb();
	// Requete envoyé au serveur
	$resultat = $db->query("Select id, prenom, nom, login, mdp from Salarie");
	// Vérification des des logins envoyé
	while($ligne=$resultat->fetch()){
		if (($_POST['login']==$ligne['login'])&&($_POST['mdp']==$ligne['mdp'])) {
			session_start();
			$_SESSION['id'] = $ligne['id'];
			$_SESSION['prenom'] = $ligne['prenom'];
			$_SESSION['nom'] = $ligne['nom'];
			$_SESSION['login'] = $ligne['login'];
		}
	}
	// S'il y a une connexion alors on se dirige au menu
	if(isset($_SESSION['id'])){
		header('Location: menu.php');
	}
	// Sinon message d'erreur et redirection vers la page de connexion
	else{
	header('Location: Login.php?mss=2');}
		
?>