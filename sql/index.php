<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="gbk">
    <title>开始获取愉快的flag吧</title>
</head>
<h1>HACKER WORLD</h1>
<body style="background-color: #000000;color: #62ff1c;font-size: 20px;">
<?php
$id=@$_GET['id'];
$mysql_server_name = "103.45.250.44";
$mysql_username    = "root";
$mysql_password    = "root";
$mysql_database    = "test";
$conn= mysqli_connect( $mysql_server_name, $mysql_username, $mysql_password,$mysql_database);
if($conn){
    if($id){
        $sql = "select user from test where id=$id";
        $result=mysqli_query($conn,$sql);
        $x=0;
        while ($row=mysqli_fetch_array($result)){
            $x++;
            if($x==1){
                echo "用户:" . $row['user'] . "<br>";
}
if($x==2){
echo "密码:" . $row['user'] . "<br>";
echo "flag >>> flag{ ___fucking_bitch___ }<br>";
}

}
echo "已知用户为:admin 表为test 但不知道密码为何。" . "<br>";
}else{
die("咦惹，操作好像失败了，参数<span style='color: red;'>id</span>为空！");
}
}
?>
<a href="code.txt" target="_blank">代码审计</a>
<br>
</body>
</html>
