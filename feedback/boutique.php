<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'message' => 'Method not allowed.']);
    exit;
}

$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
$allowedOrigins = ['https://nexalyplanner.com', 'https://www.nexalyplanner.com'];
if ($origin !== '' && !in_array($origin, $allowedOrigins, true)) {
    http_response_code(403);
    echo json_encode(['ok' => false, 'message' => 'Request not allowed.']);
    exit;
}

session_start();
$now = time();
$recent = array_values(array_filter($_SESSION['boutique_feedback_times'] ?? [], static fn($time) => $time > $now - 3600));
if (count($recent) >= 3) {
    http_response_code(429);
    echo json_encode(['ok' => false, 'message' => 'Please wait before sending another message.']);
    exit;
}

$payload = json_decode(file_get_contents('php://input') ?: '', true);
if (!is_array($payload)) {
    $payload = $_POST;
}

if (trim((string)($payload['website'] ?? '')) !== '') {
    echo json_encode(['ok' => true, 'message' => 'Thank you for your feedback.']);
    exit;
}

$name = trim((string)($payload['name'] ?? ''));
$email = trim((string)($payload['email'] ?? ''));
$type = (string)($payload['type'] ?? 'suggestion');
$message = trim((string)($payload['message'] ?? ''));

if (!in_array($type, ['comment', 'suggestion', 'issue'], true)) {
    $type = 'suggestion';
}
if (strlen($name) > 80 || strlen($email) > 160 || strlen($message) < 5 || strlen($message) > 1500) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'message' => 'Please enter a message between 5 and 1,500 characters.']);
    exit;
}
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'message' => 'Please enter a valid email address.']);
    exit;
}

$record = [
    'id' => bin2hex(random_bytes(8)),
    'created_at' => gmdate('c'),
    'product' => 'boutique-business-planner',
    'type' => $type,
    'name' => $name,
    'email' => $email,
    'message' => $message,
    'status' => 'pending',
    'ip_hash' => hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . '|nexaly-boutique-feedback'),
];

$storageDir = dirname(__DIR__) . '/private-feedback';
if (!is_dir($storageDir) && !mkdir($storageDir, 0750, true) && !is_dir($storageDir)) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'message' => 'Feedback could not be saved right now.']);
    exit;
}

$written = file_put_contents(
    $storageDir . '/boutique-feedback.jsonl',
    json_encode($record, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . PHP_EOL,
    FILE_APPEND | LOCK_EX
);
if ($written === false) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'message' => 'Feedback could not be saved right now.']);
    exit;
}

$recent[] = $now;
$_SESSION['boutique_feedback_times'] = $recent;
echo json_encode(['ok' => true, 'message' => 'Thank you — your feedback was sent for review.']);
