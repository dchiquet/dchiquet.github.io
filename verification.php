<?php 
if(isset($_SESSION['id'])){
}else{
header('Location: Login.php?mss=1');}