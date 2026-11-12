<?php
$host="localhost";
$users="root";
$pass="";
$db="dbcrud";

$conn=mysqli_connect($host,$users,$pass,$db);
if($conn->connect_error){
	die("connection XXX: ".$conn->connect_error);
}

?>