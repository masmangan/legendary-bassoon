<?php
// Arquivo: db_config.php
// Configuração da conexão com o banco de testes

$host = '127.0.0.1';
$db   = 'app_test';
$user = 'app_tester';
$pass = 'Test123!';
$charset = 'utf8mb4';

// DSN = Data Source Name (informações de conexão para o PDO)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "✅ Conexão com o banco de testes bem-sucedida!\n";
} catch (PDOException $e) {
    echo "❌ Erro ao conectar: " . $e->getMessage() . "\n";
}

