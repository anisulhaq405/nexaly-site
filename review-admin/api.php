<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/feedback/review-lib.php';
require_once dirname(__DIR__) . '/private-feedback/admin-auth.php';
session_start(); header('X-Robots-Tag: noindex, nofollow, noarchive');
function admin_ok(): bool { return !empty($_SESSION['nexaly_review_admin']) && ($_SESSION['nexaly_review_admin_at'] ?? 0) > time() - 7200; }
function csrf_ok(string $token): bool { return isset($_SESSION['nexaly_review_csrf']) && hash_equals($_SESSION['nexaly_review_csrf'], $token); }
$payload = json_decode(file_get_contents('php://input') ?: '', true); if (!is_array($payload)) $payload = $_POST;
$action = (string)($payload['action'] ?? $_GET['action'] ?? 'list');
if ($action === 'login') {
    $password = (string)($payload['password'] ?? '');
    $attempts = array_values(array_filter($_SESSION['nexaly_admin_attempts'] ?? [], static fn($time) => $time > time() - 900));
    if (count($attempts) >= 5) review_json(['ok' => false, 'message' => 'Too many attempts. Please wait 15 minutes.'], 429);
    if (!hash_equals(NEXALY_REVIEW_ADMIN_HASH, crypt($password, NEXALY_REVIEW_ADMIN_HASH))) { $attempts[] = time(); $_SESSION['nexaly_admin_attempts'] = $attempts; usleep(400000); review_json(['ok' => false, 'message' => 'Incorrect password.'], 401); }
    session_regenerate_id(true); $_SESSION['nexaly_review_admin'] = true; $_SESSION['nexaly_review_admin_at'] = time(); $_SESSION['nexaly_review_csrf'] = bin2hex(random_bytes(24));
    review_json(['ok' => true, 'csrf' => $_SESSION['nexaly_review_csrf']]);
}
if ($action === 'logout') { session_destroy(); review_json(['ok' => true]); }
if (!admin_ok()) review_json(['ok' => false, 'message' => 'Sign in required.'], 401);
if ($action === 'list') {
    $requested = (string)($_GET['product'] ?? 'all'); $records = [];
    if ($requested === 'all') { foreach (array_keys(NEXALY_PRODUCTS) as $product) $records = array_merge($records, review_records($product)); }
    else { $product = review_product($requested); $records = review_records($product); }
    usort($records, static fn($a, $b) => strcmp((string)($b['created_at'] ?? ''), (string)($a['created_at'] ?? '')));
    foreach ($records as &$row) unset($row['ip_hash']); unset($row);
    review_json(['ok' => true, 'csrf' => $_SESSION['nexaly_review_csrf'], 'records' => $records]);
}
if ($action === 'moderate') {
    if (!csrf_ok((string)($payload['csrf'] ?? ''))) review_json(['ok' => false, 'message' => 'Security check failed. Refresh and try again.'], 403);
    $product = review_product((string)($payload['product'] ?? '')); $id = preg_replace('/[^a-f0-9]/', '', (string)($payload['id'] ?? '')); $status = (string)($payload['status'] ?? '');
    if (strlen($id) !== 16 || !in_array($status, ['approved', 'rejected'], true)) review_json(['ok' => false, 'message' => 'Invalid moderation request.'], 422);
    $found = false; foreach (review_records($product) as $record) if (($record['id'] ?? '') === $id) { $found = true; break; }
    if (!$found) review_json(['ok' => false, 'message' => 'Submission not found.'], 404);
    if (!review_write_jsonl(review_storage_dir() . '/review-decisions.jsonl', ['feedback_id' => $id, 'product' => $product, 'status' => $status, 'created_at' => gmdate('c')])) review_json(['ok' => false, 'message' => 'Decision could not be saved.'], 500);
    review_json(['ok' => true, 'message' => ucfirst($status) . '.']);
}
review_json(['ok' => false, 'message' => 'Unknown action.'], 404);
