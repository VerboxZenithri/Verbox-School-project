<?php
include'cfg.php';
$id=$_GET['id'];
$sql="SELECT*FROM tbsiswa WHERE id='$id'";
$rs=mysqli_query($conn,$sql);
$row=mysqli_fetch_assoc($rs);
?>
<body>
<form action="process_updt.php" method="post">
<input type="hidden" name="id" value="<?php echo$row['id'];?>">
<input type="text" name="nama" value="<?php echo$row['nama'];?>" required>
<input type="text" name="kelas" value="<?php echo$row['kelas'];?>" required>
<input type="date" name="Tanggal" value="<?php echo$row['Tanggal'];?>" required>
<input type="submit" value="Update Data">
</form>
</body>
