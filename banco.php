<?php
$host = 'localhost';
$db = 'crime_sphere';
$user = 'root';
$pass = 'pipi'; //senha

// Conectando ao banco de dados
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo 'Conexão bem-sucedida';
} catch (PDOException $e) {
    echo 'Falha na conexão: ' . $e->getMessage();
}
?>
