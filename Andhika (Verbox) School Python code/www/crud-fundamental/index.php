<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="proses_input.php" method="post">
        <input type="text" name="nama" placeholder="isi nama anda" required><br>
        <input type="text" name="kelas" placeholder="isi kelas anda" required><br>
        <input type="date" name="tanggal" Placeholder="isi tanggal lahir anda" required><br>
        <input type="submit" value="send">
        <input type="button" onclick="window.location.href='doneview.php'" value="lihat data">
    </form>
</body>
</html>