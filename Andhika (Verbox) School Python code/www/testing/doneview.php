<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body class="p-4 font-jetbrains bg-gray-100">

<?php include"cfg.php";?>

<div class="mb-4">
<a href="index.php" class="px-4 py-2 bg-blue-500 text-white rounded">+ Add Data</a>
</div>

<?php
$sql="SELECT*FROM tbsiswa";
$rs=mysqli_query($conn,$sql);
if(mysqli_num_rows($rs)>0){
echo"<ul class='bg-white p-3 rounded shadow'>";
while($r=mysqli_fetch_assoc($rs)){
echo"<li class='border-b py-2'>";
echo"<span class='font-bold'>".$r['nama']."</span> - ";
echo"<span>".$r['kelas']."</span>";
echo"<a href='del.php?id=".$r['id']."' class='ml-3 text-red-500'>Hapus</a>";
echo"<a href='updt.php?id=".$r['id']."' class='ml-3 text-green-500'>Update</a>";
echo"</li>";
}
echo"</ul>";
}else{
echo"<p class='text-gray-600'>zero data, zero</p>";
}
mysqli_close($conn);
?>
</body>
</html>
