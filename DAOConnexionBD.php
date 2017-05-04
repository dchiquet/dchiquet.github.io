<?php
class DAOConnexionBD{
	private $db;
	
	public function __construct(){
		$this->db = new PDO('mysql:host=localhost;dbname=Enquete', 'root', '');
	}
	public function getDb(){
		return $this->db;
	}
}
?>