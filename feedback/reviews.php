<?php
declare(strict_types=1);
require_once __DIR__ . '/review-lib.php';
if ($_SERVER['REQUEST_METHOD'] !== 'GET') review_json(['ok' => false, 'message' => 'Method not allowed.'], 405);
$product = review_product((string)($_GET['product'] ?? '')); $public = [];
foreach (array_reverse(review_records($product)) as $record) {
    if (($record['type'] ?? '') !== 'review' || ($record['status'] ?? '') !== 'approved' || empty($record['publish_consent'])) continue;
    $public[] = ['id' => $record['id'], 'created_at' => $record['created_at'], 'rating' => (int)$record['rating'], 'title' => (string)($record['title'] ?? ''), 'name' => trim((string)($record['name'] ?? '')) ?: 'Nexaly customer', 'message' => (string)$record['message'], 'verified_buyer' => !empty($record['verified_buyer'])];
    if (count($public) >= 30) break;
}
$average = count($public) ? round(array_sum(array_column($public, 'rating')) / count($public), 1) : 0;
review_json(['ok' => true, 'product' => $product, 'average' => $average, 'count' => count($public), 'reviews' => $public]);
