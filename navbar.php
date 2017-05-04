<a href="encours.php">Enquetes en cours</a> 
<a href="termine.php">Enquetes termine</a> 
<a href="deconnexion.php">Deconnexion</a>
<?php
session_start();
echo "Session : ".$_SESSION['prenom'].' '.$_SESSION['nom'];
?>