<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $host = 'localhost';
    $dbname = 'orders_db';
    $username = 'root';
    $password = 'root';

    $mysqli = new mysqli($host, $username, $password, $dbname);

    if ($mysqli->connect_error) {
        echo 'Errno: ' . $mysqli->connect_errno;
        echo '<br>';
        echo 'Error: ' . $mysqli->connect_error;
        exit();
    }


    $last_name = $_POST['last_name'];
    $first_name = $_POST['first_name'];
    $address = $_POST['address'];
    $phone = $_POST['phone'];
    $product = $_POST['product'];
    $comment = $_POST['comment'];

    $sql = "INSERT INTO orders (last_name, first_name, address, phone, product, comment)
            VALUES (?, ?, ?, ?, ?, ?)";

    $stmt = $mysqli->prepare($sql);

    if ($stmt === false) {
        echo "Ошибка подготовки запроса: " . $mysqli->error;
        exit();
    }

    $stmt->bind_param(
        'ssssss',
        $last_name,
        $first_name,
        $address,
        $phone,
        $product,
        $comment
    );

    if ($stmt->execute()) {
        echo "Форма успешно отправлена!";
    } else {
        echo "Ошибка: " . $stmt->error;
    }
    $stmt->close();
    $mysqli->close();
} else {
    echo "Ошибка";
}