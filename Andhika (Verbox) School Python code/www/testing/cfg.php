<?php
$host="localhost";
$user="root";
$pass="";
$db="dbcrud";

$conn=mysqli_connect($host,$user,$pass,$db);
if($conn->connect_error){
die("connection XXX: ".$conn->connect_error);
}
?>
